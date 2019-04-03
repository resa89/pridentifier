import os

from .fingerprint import Fingerprint
from ..evaluator import Evaluator
from ..inspector import Inspector


class Pridentifier(object):
    def __init__(self, path):
        # [1] classifier data
        self.path = path
        self.classes = []
        self.number_of_classes = 0
        self.fingerprints = []
        self.traindata = []

        # [2] classification configuration


        # [3] results
        # after image load
        self.amount_images_per_class = []
        self.amount_snippets_per_class = []
        # after training
        # after test
        # after inspection

        self.load_images(self.path)
        self.extract_features()
        self.evaluate()


    def load_images(self, path):

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
        self.evaluator = Evaluator(self.classes,self.fingerprints)
        result = self.evaluator.get_evaluation()

        print(result)


    def inspect(self):
        self.inspector = Inspector()
        pass








