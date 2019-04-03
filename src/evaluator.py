import os.path

import numpy as np
import pandas as pd

from config import SUBPATH, SNIPPET_WIDTH


class Evaluator(object):
    def __init__(self, classes, fingerprints):
        self.classes = classes
        self.fingerprints = fingerprints
        self.result = []

        self.test_on_train_data()


    def test_on_train_data(self):

        # for every class
        for i in range(len(self.classes)):
            # read train data
            train_data = self.get_train_data(self.classes[i])

            # for every sample / snippet
            for index, row in train_data.iterrows():
                prediction, gtd, passed = self.compare_to_fingerprints(row, self.classes,  self.fingerprints) # return (predicted class, GTD, True or False prediction)
                result = [prediction, gtd, passed]
                if len(self.result) == 0:
                    self.result = pd.DataFrame(np.array(result).reshape(1,3), columns=['prediction', 'GTD', 'passed'])
                else:
                    self.result = self.result.append({'prediction': result[0], 'GTD': result[1], 'passed': result[2]},
                                       ignore_index=True)



    def get_evaluation(self):

        return(self.result, self.classes)


    def get_train_data(self, class_name):

        folder = SUBPATH + '/trained_samples/'
        file_name = folder + class_name + "_train.pkl"

        if not os.path.exists(folder):
            print("Error: Folder does not exist: ", folder)

        if os.path.isfile(file_name):
            unpickled_df = pd.read_pickle(file_name)

        return(unpickled_df)



    def compare_to_fingerprints(self, sample, classes, fingerprints):
        gtd = sample['class']
        prediction = 0
        prediction_value = 0
        passed = False
        amount_classes = len(classes)
        correlation_values = [0 for i in range(amount_classes)]

        for i in range(amount_classes):
            correlation_values[i] = np.dot(np.array(sample)[:-1].reshape(SNIPPET_WIDTH,SNIPPET_WIDTH).astype(np.float64),
                                           fingerprints[i].get_fingerprint()).sum()
            # TODO: better way to compare int with float64
            if correlation_values[i] > prediction_value:
                prediction_value = correlation_values[i]
                prediction = classes[i]


        if prediction == 0:
            print('ERROR: the correlation values not correct.. still 0 as class!')

        if prediction == gtd:
            passed = True


        return(prediction, gtd, passed)


