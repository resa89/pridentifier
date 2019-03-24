import numpy as np
import pandas as pd

from config import *


class Classifier():

    def __init__(self, path, img_names, number_of_snippets, classes, train=False):
        self.path_to_class = path
        self.img_names = img_names
        self.number_of_snippets = number_of_snippets
        self.number_classes = len(classes)
        self.classes = classes

        self.accumulated_spectra = np.zeros((SNIPPET_WIDTH, SNIPPET_WIDTH))
        self.df_header = []

        self.inspect(train)


    def inspect(self, train):
        data_normed = np.zeros((self.number_classes, SNIPPET_WIDTH, SNIPPET_WIDTH))



        class_column = SNIPPET_WIDTH*SNIPPET_WIDTH - 1 + 1
        sum = np.zeros((self.number_classes))

        if train:
            for printer_id in range(self.number_classes):

                path_to_fingerprint = SUBPATH + '/fingerprint/' + self.classes[printer_id] + "_fingerprint.pkl"
                fingerprint_df = pd.read_pickle(path_to_fingerprint)

                vector = np.array(fingerprint_df[:-1])
                #TODO: Check if -1 or -2 necessary

                data_normed[printer_id, :, :] = np.reshape(vector, (SNIPPET_WIDTH, SNIPPET_WIDTH))
                sum[printer_id] = np.sum(np.sum(data_normed[printer_id]))

                # Training
                pd.DataFrame(data_normed[printer_id]).to_pickle(SUBPATH + "/corr_" + self.classes[printer_id] + ".pkl")
        else:
            # Test data
            for printer_id in range(self.number_classes):
                data_normed[printer_id] = pd.read_pickle("knowledge/corr_" + self.classes[printer_id] + ".pkl")

        nr_segments = self.questioned_detailed.shape[0]
        correlation_list = np.zeros((nr_segments, self.printer_types.size + 1))

        printers_nr = np.arange(self.printer_types.size)

        for i in range(self.questioned_detailed.shape[0]):
            #p_id = self.questioned_detailed.ix[i, class_column]
            #printer_number = np.where(self.printer_types == p_id)[0][0]
            printer_number = -1

            # prove similarity - correlation of segment ffts with additive spcectras
            for p in range(len(self.printer_types)):
                correlation_list[i, p] = np.dot(self.questioned_detailed.ix[i, :class_column],
                                                data_normed[p, :, :].reshape(class_column))

                correlation_list[i, p + 1] = printer_number

        for p in range(len(self.printer_types)):
            self.hitsPerClassOfInspectedSegments[p] = 0

        #for all segments
        questioned_list = correlation_list[correlation_list[:, -1] == -1] # :-1, because without lable and == value -1 because set for questioned
        # for each segment from one questioned print
        for row in range(questioned_list.shape[0]):
            likeliest_class = np.where(questioned_list[row, :] == questioned_list[row, :].max())[0][0]

            self.hitsPerClassOfInspectedSegments[likeliest_class] += 1



        print("Training for all printers finished.")
        return self.hitsPerClassOfInspectedSegments