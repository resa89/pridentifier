import os.path

import numpy as np
import pandas as pd

import config
from .feature_extractor import try_to_load_as_pickled_object_or_None


class Evaluator(object):
    def __init__(self, classes, fingerprints, SNIPPET_WIDTH, train=True):
        self.classes = classes
        self.fingerprints = fingerprints
        self.SNIPPET_WIDTH = SNIPPET_WIDTH
        self.result = []

        if train:
            self.test_on_data(train=True)
        else:
            self.test_on_data(train=False)


    def test_on_data(self, train=True):

        if train:
            loops = self.classes
        else:
            loops = ['Q']

        # for every class
        for i in range(len(loops)):
            # read train data
            if train:
                t_data = self.get_train_data(self.classes[i])
            else:
                t_data = self.get_test_data(self.classes[i])
            # for every sample / snippet
            for index, row in t_data.iterrows():
                prediction, gtd, passed = self.compare_to_fingerprints(row, self.classes,  self.fingerprints) # return (predicted class, GTD, True or False prediction)
                if train:
                    result = [prediction, gtd, passed]
                else:
                    result = [prediction, gtd, 'unknown']
                if len(self.result) == 0:
                    self.result = pd.DataFrame(np.array(result).reshape(1,3), columns=['prediction', 'GTD', 'passed'])
                else:
                    self.result = self.result.append({'prediction': result[0], 'GTD': result[1], 'passed': result[2]},
                                       ignore_index=True)
                if index > t_data.shape[0]:
                    print("ERROR: with index in evaluation!!!!!")
                if train:
                    config.state_evaluation = i*100/(len(self.classes))+\
                                                    (index/t_data.shape[0]*100)//len(self.classes)
                else:
                    # 50+ because the first part of inspection is the analysis
                    config.state_inspection = 50 + (index/t_data.shape[0]*50)



    def get_evaluation(self):

        return(self.result) # self.classes


    def get_train_data(self, class_name):
        unpickled_df = self.get_data(class_name, train=True)
        return(unpickled_df)


    def get_test_data(self, class_name):
        unpickled_df = self.get_data(class_name, train=False)
        return(unpickled_df)


    def get_data(self, class_name, train=True):

        if train:
            folder = config.SUBPATH + '/trained_samples/'
            file_name = folder + class_name + "_train.pkl"

        else:
            folder = config.SUBPATH + '/test_samples/'
            file_name = folder + 'Q' + "_test.pkl"


        if not os.path.exists(folder):
            print("Error: Folder does not exist: ", folder)

        if os.path.isfile(file_name):
            unpickled_df = try_to_load_as_pickled_object_or_None(file_name)

        return(unpickled_df)


    def compare_to_fingerprints(self, sample, classes, fingerprints):
        gtd = sample['class']
        prediction = 0
        prediction_value = 0
        passed = False
        amount_classes = len(classes)
        correlation_values = [0 for i in range(amount_classes)]

        for i in range(amount_classes):
            fi_print = fingerprints[i].get_fingerprint()
            #fi_print_normed = fi_print / fi_print.sum()
            fi_print_sample = np.array(sample)[:-1].reshape(self.SNIPPET_WIDTH,self.SNIPPET_WIDTH).astype(np.float64)


            ######
            #####



            correlation_values[i] = np.dot(fi_print_sample.reshape(fi_print_sample.size),
                                           fi_print.reshape(fi_print.size))



            # TODO: better way to compare int with float64
            if correlation_values[i] > prediction_value:
                prediction_value = correlation_values[i]
                prediction = classes[i]


        if prediction == 0:
            print('ERROR: the correlation values not correct.. still 0 as class!')

        if prediction == gtd:
            passed = True


        return(prediction, gtd, passed)


