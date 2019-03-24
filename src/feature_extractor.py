import os.path

import numpy as np
from PIL import Image
from scipy import misc
import pandas as pd

from config import *


class FeatureExtractor(object):

    def __init__(self, path, img_names, number_of_snippets, train=True):
        self.path_to_class = path
        self.img_names = img_names
        self.number_of_snippets = number_of_snippets
        self.accumulated_spectra = np.zeros((SNIPPET_WIDTH, SNIPPET_WIDTH))
        self.df_header = []

        self.compute_accumulated_spectra(train)



    def compute_accumulated_spectra(self, train):

        sample_amount =  0
        if train:
            class_name = os.path.basename(os.path.normpath(self.path_to_class))
        else:
            class_name = 'Q' # for Questioned

        # number of pixels to move each segment
        step = np.empty([2], dtype=int)
        step[0] = SNIPPET_WIDTH
        step[1] = SNIPPET_WIDTH

        segment_count = np.empty([2], dtype=int)

        for image in self.img_names:
            img_path = self.path_to_class + '/' + image
            img = misc.imread(img_path)

            grey_img = self.greyscale(img)

            # number of segments in one scanned image (in both dimensions)
            segment_count[0] = grey_img.shape[0] // step[0]
            segment_count[1] = grey_img.shape[1] // step[1]

            df_all_segments = self.initalize_train_data(segment_count[0]*segment_count[1])
            sample_no = 0

            # for(each segment in img): cut of segment
            for i in range(0, segment_count[0]):
                for j in range(0, segment_count[1]):
                    # segment as copy of img snippet
                    start_i = i * SNIPPET_WIDTH
                    start_j = j * SNIPPET_WIDTH
                    segment = grey_img[start_i:(start_i + SNIPPET_WIDTH), start_j:(start_j + SNIPPET_WIDTH)]

                    segment_windowed = self.compute_window(segment)
                    spectrum =self.compute_spectrum(segment_windowed)

                    # compute the accumulated fingerprint
                    np.add(self.accumulated_spectra, np.divide(spectrum, self.number_of_snippets))

                    self.accumulated_spectra = self.darkenregion(self.accumulated_spectra)

                    # save sampled spectra for training analysis later
                    df_all_segments = self.add_train_data(df_all_segments, spectrum, class_name, sample_no)
                    sample_no += 1

            sample_amount += segment_count[0] * segment_count[1]

            self.save_train_data(df_all_segments, class_name, train)

        self.save_fingerprint(self.accumulated_spectra, class_name, sample_amount, train)



    def greyscale(self, img):

        if len(img.shape) == 3 and img.shape[2] == 3:
            weight = [0.2,0.5,0.3] # weights
            weighted_mean = np.tensordot(img,weihgt, axes=((-1,-1)))[...,None]
            img[:] = weighted_mean.astype(img.dtype)

        return(img)

    def compute_window(self, segment):
        # windowing function on segment
        # build 1d window
        segment_hanning = segment.copy()

        # hanning vectors
        u_vector = np.hanning(segment.shape[0])  # eine Zeile
        v_vector = np.hanning(segment.shape[1])  # eine Spalte

        # 2d hanning matrix
        for u in range(0, segment.shape[0] - 1):
            for v in range(0, segment.shape[1] - 1):
                segment_hanning[u][v] = np.multiply(u_vector[u], v_vector[v]) * 255

        segment_windowed = segment.copy()

        ## multiply hanning window to image
        for u in range(0, segment.shape[0] - 1):
            # img_hanning[u] = np.multiply(u_vector[u], v_vector)
            t_max = np.float64(0)
            for v in range(0, segment.shape[1] - 1):
                t = np.float64(segment_hanning[u][v]) / 255
                segment_windowed[u][v] = t * np.float64(segment[u][v]) + (1 - t) * 255
                # segment_windowed[u][v] = np.multiply(np.float64(img[u][v]), img_hanning[u][v])/255
                if t > t_max:
                    t_max = np.float64(t)

        return(segment_windowed)

    def compute_spectrum(self, window):
        f = np.fft.fft2(window)
        fshift = np.fft.fftshift(f)
        magnitude_spectrum = 20 * np.log(np.abs(fshift))
        return(magnitude_spectrum)

    def darken_region(self, magnitude_spectrum):
        # darken region around axis
        middle = int(magnitude_spectrum.shape[0] / 2)
        magnitude_spectrum[middle - 5:middle + 5, :] = magnitude_spectrum.min()
        magnitude_spectrum[:, middle - 5:middle + 5] = magnitude_spectrum.min()
        return(magnitude_spectrum)


    def initalize_train_data(self, number_of_rows):
        # df header
        df_header = [i for i in range(SNIPPET_WIDTH*SNIPPET_WIDTH)]
        self.df_header = df_header  + ['class']

        # preallocate df
        # create dataframe
        df = pd.DataFrame(index=np.arange(0, number_of_rows), columns=df_header )
        # TODO: check if is initilized with 0 or NAN

        return(df)


    def add_train_data(self, df, train_data, spectrum, sample_no):

        # add segment fft to data_detailed
        new_sample = spectrum.reshape(spectrum.size).tolist() + [self.class_name]

        #df.append(new_sample, ignore_index = True)

        self.data_detailed.loc[sample_no] = new_sample



    def save_train_data(self, df_all_segments, class_name, train):

        if train:
            folder = SUBPATH + '/trained_samples/'
            file_name = folder + class_name + "_train.pkl"
        else:
            folder = SUBPATH + '/test_samples/'
            file_name = folder + class_name + "_test.pkl"

        if not os.path.exists(folder):
            os.mkdir(folder)

        if os.path.isfile(file_name):
            unpickled_df = pd.read_pickle(file_name)
            df_all_segments = unpickled_df.append(df_all_segments, ignore_index=True)
            df_all_segments.to_pickle(file_name)
        else:
            df_all_segments.to_pickle(file_name)



    def save_fingerprint(self, magnitude_all, class_name, sample_amount, train):

        # add class and add one per printer to pandas dataframes
        # norm additive + multiplied spectras
        # magnitude_all = np.divide(magnitude_all, magnitude_all.max())
        # magnitude_all = magnitude_all - magnitude_all.mean()
        # magnitude_all = np.divide(magnitude_all, (magnitude_all.max()-magnitude_all.min()))

        # norm the accumulated_spectra
        idx = np.argsort(magnitude_all.flatten())
        b = magnitude_all.flatten()[idx]

        threshold = b[b.size - NUMBER_PIXELS]

        min = magnitude_all.min()
        # select only 1000 brightest pixel
        magnitude_all[magnitude_all < threshold] = min
        # magnitude_all_multi[magnitude_all_multi<threshold] = min

        magnitude_all = magnitude_all - magnitude_all.min()
        magnitude_all = magnitude_all / magnitude_all.sum()

        fingerprint_df = pd.DataFrame(index=[0], columns=self.df_header)
        fingerprint_df.loc[0] = magnitude_all.reshape(magnitude_all.size).tolist() + [class_name]

        # save image: merged frequency spectrum by addition
        f_add = Image.fromarray(np.divide(magnitude_all, magnitude_all.max()) * 255).convert('RGB')

        # save image: merged frequency spectrum by addition
        path = SUBPATH + '/fingerprint/'

        if not os.path.exists(path):
            os.mkdir(path)

        if train:
            img_path = path + class_name + "_fingerprint.png"
            data_path = path + class_name + "_fingerprint.pkl"
        else:
            img_path = path + "test_" + class_name + "_fingerprint.png"
            data_path = path + "test_" + class_name + "_fingerprint.pkl"

        f_add.save(img_path, "PNG")

        magnitude_all.to_pickle(data_path)



    def get_accumulated_spectra(self):
        return(self.accumulated_spectra)





