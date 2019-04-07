import os
import pandas as pd
from PIL import Image


from .fingerprint import Fingerprint
from ..evaluator import Evaluator
from ..feature_extractor import FeatureExtractor

from config import SNIPPET_WIDTH


class Pridentifier(object):
    def __init__(self):
        # [1] classifier data
        self.path = ""
        self.classes = []
        self.number_of_classes = 0
        self.fingerprints = []
        self.traindata = []
        self.evaluation_result = pd.DataFrame()
        self.test_result = pd.DataFrame()


        # [2] classification configuration


        # [3] results
        # after image load
        self.amount_images_per_class = []
        self.amount_snippets_per_class = []
        # after training
        # after test
        # after inspection

        #self.load_images(self.path)
        #self.extract_features()
        #self.evaluate()


    def load_images(self, path):

        self.path = path

        # get classes information
        try:
            self.classes = os.listdir(path)
        except FileNotFoundError:
            print('No folder was selected. Canceled.')
            return

        # remove hidden folders and only count folders
        self.classes = [folder for folder in self.classes if not folder.startswith('.') and os.path.isdir(path + '/' + \
                                                                                                          folder)]
        # sort classes alphabetically
        self.classes.sort()

        print('classes: ', self.classes)
        print('path: ', path)

        self.number_of_classes = len(self.classes)

        for class_name in self.classes:
            class_path = path + '/' + class_name
            fingerprint = Fingerprint(class_path)
            self.fingerprints.append(fingerprint)
            amount_images, amount_snippets = fingerprint.get_numbers()
            self.amount_images_per_class.append(amount_images)
            self.amount_snippets_per_class.append(amount_snippets)




    def extract_features(self):

        for fingerprint in self.fingerprints:
            fingerprint.extract_fingerprint()




    def evaluate(self):
        self.evaluator = Evaluator(self.classes,self.fingerprints, train=True)
        self.evaluation_result = self.evaluator.get_evaluation()

        return()
        #print(result)


    def save_fingerprints(self):
        pass


    def get_fingerprints(self, path):
        pass


    def set_inspection_image_path(self, filename):
        self.inspection_path = filename
        return()


    def inspect(self):
        path, file = os.path.split(self.inspection_path)
        #TODO: Allow image or folder

        # compute snippet_amount
        img = Image.open(self.inspection_path)
        width, height = img.size
        # TODO: check order of width and height
        amount_snippets_x_axis = width // SNIPPET_WIDTH
        amount_snippets_y_axis = height // SNIPPET_WIDTH
        amount_snippets = amount_snippets_x_axis * amount_snippets_y_axis

        # extract features of test sample
        self.inspector = FeatureExtractor(path, [file], amount_snippets, train=False)

        inspection_evaluator = Evaluator(self.classes,self.fingerprints, train=False)
        self.test_result = inspection_evaluator.get_evaluation()


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




