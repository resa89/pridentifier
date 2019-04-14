import os
import time

import pandas as pd
from PIL import Image
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets

from .fingerprint import Fingerprint
from ..evaluator import Evaluator
from ..feature_extractor import FeatureExtractor
import config

class Pridentifier(QObject):

    # signals
    changedValue = pyqtSignal(int)

    def __init__(self, SNIPPET_WIDTH, NUMBER_PIXELS):

        super(Pridentifier, self).__init__()

        # [1] classifier data
        self.path = ""
        self.classes = []
        self.number_of_classes = 0
        self.fingerprints = []
        self.traindata = []
        self.evaluation_result = pd.DataFrame()
        self.test_result = pd.DataFrame()
        self.SNIPPET_WIDTH = SNIPPET_WIDTH
        self.NUMBER_PIXELS = NUMBER_PIXELS
        #self.changedValue = 0


        # [2] classification configuration


        # [3] results
        # after image load
        self.amount_images_per_class = []
        self.amount_snippets_per_class = []
        # after training
        # after test
        # after inspection


        #self.emit(pyqtSignal('extract_features(int)'), self.extract_features)

        # Setting a connection between slider position change and on_changed_value function
        #self.connect(self.get_thread, pyqtSignal("extract_features(int)"), self.extract_features)

        #self.load_images(self.path)
        #self.extract_features()
        #self.evaluate()

    def update_snippetSize(self, SNIPPET_WIDTH):

        self.SNIPPET_WIDTH = SNIPPET_WIDTH
        #TODO: update through all sub-objects


    def update_pixelSize(self, NUMBER_PIXELS):

        # TODO: inform user that feature amount is larger than snippet size
        if self.SNIPPET_WIDTH*self.SNIPPET_WIDTH < NUMBER_PIXELS:
            self.NUMBER_PIXELS = self.SNIPPET_WIDTH*self.SNIPPET_WIDTH
        else:
            self.NUMBER_PIXELS = NUMBER_PIXELS



    def load_images(self, path):

        self.path = path
        calc = ProgressLoadData(path, self.SNIPPET_WIDTH, self.NUMBER_PIXELS)

        return(calc)

    # to write data from calculation object (signal/slot)
    def write_image_infos(self, args):
        self.classes = args[0]
        self.number_of_classes = args[1]
        self.fingerprints = args[2]
        self.amount_images_per_class = args[3]
        self.amount_snippets_per_class = args[4]
        return()

    # to write data from calculation object (signal/slot)
    def write_training_results(self, args):
        self.fingerprints = args

    def write_evaluation_results(self, args):
        self.evaluator = args[0]
        self.evaluation_result = args[1]

    def write_inspection_results(self, args):
        #self.inspector = args[0]
        self.test_result = args


    def extract_features(self):
        calc = ProgressAnalyzeData(self.fingerprints, self.NUMBER_PIXELS)
        return(calc)




    def evaluate(self):
        calc = ProgressEvaluateData(self.classes, self.fingerprints, self.SNIPPET_WIDTH)
        return(calc)


    def save_fingerprints(self):
        pass


    def get_fingerprints(self, path):
        pass


    def set_inspection_image_path(self, filename):
        self.inspection_path = filename
        return()


    def inspect(self):
        calc = ProgressInspectData(self.inspection_path, self.classes, self.fingerprints, self.SNIPPET_WIDTH,
                                   self.NUMBER_PIXELS)
        return(calc)


    def save_results(self):
        pass


    def get_classes(self):
        return(self.classes)


    def get_numbers_per_printer(self):

        img_amounts = []
        segment_amounts = []

        for fingerprint in self.fingerprints:
            img_no, seg_no = fingerprint.get_numbers()
            img_amounts.append(img_no)
            segment_amounts.append(seg_no)

        return(img_amounts, segment_amounts)


    def get_evaluation_result(self, train=True):
        #TODO: return raw results to GUI or log files
        if train:
            return(self.evaluation_result)
        else:
            return(self.test_result)


    def get_stats(self, train=True):

        if train:
            evaluation = self.evaluation_result.replace({'passed': {'True': True, 'False': False}})

            true_positives = []
            true_negatives = []
            false_positives = []
            false_negatives = []
            accuracy = []

            for class_name in self.classes:
                print(self.evaluation_result[self.evaluation_result['GTD'] == class_name])
                #TODO: print this into a log file
                class_only_in_GTD_df = evaluation[evaluation['GTD'] == class_name]
                class_not_in_GTD_df = evaluation[evaluation['GTD'] != class_name]

                tp = class_only_in_GTD_df[class_only_in_GTD_df['passed']==True].shape[0]
                tp_rate = tp / class_only_in_GTD_df.shape[0]
                tn = class_not_in_GTD_df[class_not_in_GTD_df['prediction']!=class_name].shape[0]
                tn_rate = tn / class_not_in_GTD_df.shape[0]
                fp = class_only_in_GTD_df[class_only_in_GTD_df['passed']==False].shape[0]
                fp_rate = fp / class_only_in_GTD_df.shape[0]
                fn = class_not_in_GTD_df[class_not_in_GTD_df['prediction']==class_name].shape[0]
                fn_rate = fn / class_not_in_GTD_df.shape[0]
                # accuracy = (TP + TN) / (P+N)
                a = (tp + tn) / (class_only_in_GTD_df.shape[0] + class_not_in_GTD_df.shape[0])

                # *100 to get % instead of rate
                true_positives.append(round(tp_rate*100,1))
                true_negatives.append(round(tn_rate*100,1))
                false_positives.append(round(fp_rate*100,1))
                false_negatives.append(round(fn_rate*100,1))
                accuracy.append(round(a*100,1))

            statistics = [true_positives, true_negatives, false_positives, false_negatives, accuracy]


        else:
            evaluation = self.test_result.replace({'passed': {'True': True, 'False': False}})

            classified_as_class = []
            probabilities = []

            for class_name in self.classes:
                print(evaluation)
                classified = evaluation[evaluation['prediction']==class_name].shape[0]
                classified_rate = classified / evaluation.shape[0]

                # *100 to get % instead of rate
                classified_as_class.append(classified)
                probabilities.append(round(classified_rate*100,1))

            statistics = [classified_as_class, probabilities]

        return(statistics)




class ProgressLoadData(QtCore.QThread, QtCore.QObject):
    """
    Runs a counter object.
    """
    imageUploadStatusChanged = pyqtSignal(int, object)

    def __init__(self, path, SNIPPET_WIDTH, NUMBER_PIXELS):
        super(ProgressLoadData, self).__init__()
        self.path = path
        self.SNIPPET_WIDTH = SNIPPET_WIDTH
        self.NUMBER_PIXELS = NUMBER_PIXELS

    def run(self):
        fingerprints = []
        amount_images_per_class = []
        amount_snippets_per_class = []

        count = 0
        # get classes information
        try:
            classes = os.listdir(self.path)
        except FileNotFoundError:
            print('No folder was selected. Canceled.')
            return

        # remove hidden folders and only count folders
        classes = [folder for folder in classes if not folder.startswith('.') and os.path.isdir(self.path
                                                                                                          + '/' +
                                                                                                          folder)]
        # sort classes alphabetically
        classes.sort()

        count += 10
        self.imageUploadStatusChanged.emit(count, None)


        print('classes: ', classes)

        number_of_classes = len(classes)

        for class_name in classes:
            class_path = self.path + '/' + class_name
            fingerprint = Fingerprint(class_path, classes, self.SNIPPET_WIDTH, self.NUMBER_PIXELS)
            fingerprints.append(fingerprint)
            amount_images, amount_snippets = fingerprint.get_numbers()
            amount_images_per_class.append(amount_images)
            amount_snippets_per_class.append(amount_snippets)

            #count += 90 //number_of_classes
            #self.imageUploadStatusChanged.emit(count, None)
            #config.state_loading = count

        args = classes, number_of_classes, fingerprints, amount_images_per_class, amount_snippets_per_class
        self.imageUploadStatusChanged.emit(count, args)



class ProgressAnalyzeData(QtCore.QThread, QtCore.QObject):
    """
    Runs a counter object.
    """
    analyzeDataStatusChanged = pyqtSignal(int, object)

    def __init__(self, fingerprints, NUMBER_PIXELS):
        super(ProgressAnalyzeData, self).__init__()
        self.fingerprints = fingerprints
        self.NUMBER_PIXELS = NUMBER_PIXELS

    def run(self):

        count = 0

        for fingerprint in self.fingerprints:
            fingerprint.update_pixelSize(self.NUMBER_PIXELS)
            fingerprint.extract_fingerprint()
            count += 100//len(self.fingerprints)
            #self.analyzeDataStatusChanged.emit(count, None)
            config.state_analysis = count

        args = self.fingerprints
        self.analyzeDataStatusChanged.emit(count, args)



class ProgressEvaluateData(QtCore.QThread, QtCore.QObject):
    """
    Runs a counter object.
    """
    evaluateDataStatusChanged = pyqtSignal(int, object)

    def __init__(self, classes, fingerprints, SNIPPET_WIDTH):
        super(ProgressEvaluateData, self).__init__()
        self.classes = classes
        self.fingerprints = fingerprints
        self.SNIPPET_WIDTH = SNIPPET_WIDTH

    def run(self):

        count = 0

        config.state_analysis = 0

        evaluator = Evaluator(self.classes,self.fingerprints, self.SNIPPET_WIDTH, train=True)
        evaluation_result = evaluator.get_evaluation()

        count = 100

        args = evaluator, evaluation_result
        self.evaluateDataStatusChanged.emit(count, args)





class ProgressInspectData(QtCore.QThread, QtCore.QObject):
    """
    Runs a counter object.
    """
    inspectDataStatusChanged = pyqtSignal(int, object)

    def __init__(self, inspection_path, classes, fingerprints, SNIPPET_WIDTH, NUMBER_PIXELS):
        super(ProgressInspectData, self).__init__()
        self.inspection_path = inspection_path
        self.classes = classes
        self.fingerprints = fingerprints
        self.SNIPPET_WIDTH = SNIPPET_WIDTH
        self.NUMBER_PIXELS = NUMBER_PIXELS

    def run(self):

        count = 0

        path, file = os.path.split(self.inspection_path)
        #TODO: Allow image or folder

        # compute snippet_amount
        img = Image.open(self.inspection_path)
        width, height = img.size
        # TODO: check order of width and height
        amount_snippets_x_axis = width // self.SNIPPET_WIDTH
        amount_snippets_y_axis = height // self.SNIPPET_WIDTH
        amount_snippets = amount_snippets_x_axis * amount_snippets_y_axis

        # extract features of test sample
        inspector = FeatureExtractor(path, [file], amount_snippets, self.classes,
                                     self.SNIPPET_WIDTH, self.NUMBER_PIXELS, train=False)

        inspection_evaluator = Evaluator(self.classes,self.fingerprints, self.SNIPPET_WIDTH, train=False)
        test_result = inspection_evaluator.get_evaluation()


        count = 100

        args = test_result
        self.inspectDataStatusChanged.emit(count, args)


