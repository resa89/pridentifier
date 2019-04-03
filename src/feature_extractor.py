import os.path

import numpy as np
from PIL import Image
from scipy import misc
import pandas as pd
from scipy import fftpack
from scipy import signal

from config import *


class FeatureExtractor(object):

    def __init__(self, path, img_names, number_of_snippets, train=True):
        self.path_to_class = path
        self.img_names = img_names
        self.number_of_snippets = number_of_snippets
        self.accumulated_spectra = np.zeros((SNIPPET_WIDTH, SNIPPET_WIDTH))
        # df header
        self.df_header = [i for i in range(SNIPPET_WIDTH*SNIPPET_WIDTH)]
        self.df_header = self.df_header  + ['class']
        # allocate memory
        #self.fingerprint_df = pd.DataFrame(index=[0], columns=self.df_header, dtype=float)
        #self.fingerprint_df = pd.DataFrame(columns=self.df_header)
        self.fingerprint_df = pd.DataFrame()


        # for all segments needed for evaluation later
        max_snippet_amount_per_image = 0
        #snippets_over_all = 0
        for image in self.img_names:
            img_path = self.path_to_class + '/' + image
            img = misc.imread(img_path)
            x, y, z = img.shape
            #snippets_over_all += x//SNIPPET_WIDTH * y//SNIPPET_WIDTH
            snippet_amount = x//SNIPPET_WIDTH * y//SNIPPET_WIDTH
            if snippet_amount > max_snippet_amount_per_image:
                max_snippet_amount_per_image = snippet_amount

        #self.train_data = pd.DataFrame(index=np.arange(0, max_snippet_amount_per_image), columns=self.df_header )
        self.train_data = pd.DataFrame()

        #check if all are NANs

        self.compute_accumulated_spectra(train)


        #if snippets_over_all == self.number_of_snippets:
        #    return("TEST: True. The snippet amount computed in advance is the same than after feature computation.")
        #else:
        #    return("TEST: Failed. The snippet amount computed in advance is NOT the same than after feature computation.")



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

        first_image = True

        for image in self.img_names:
            img_path = self.path_to_class + '/' + image
            img = misc.imread(img_path)

            grey_img = self.greyscale(img)

            # number of segments in one scanned image (in both dimensions)
            segment_count[0] = grey_img.shape[0] // step[0]
            segment_count[1] = grey_img.shape[1] // step[1]

            sample_no = 0

            # for(each segment in img): cut of segment
            for i in range(0, segment_count[0]):
                for j in range(0, segment_count[1]):
                    # segment as copy of img snippet
                    start_i = i * SNIPPET_WIDTH
                    start_j = j * SNIPPET_WIDTH
                    segment = grey_img[start_i:(start_i + SNIPPET_WIDTH), start_j:(start_j + SNIPPET_WIDTH), 0]

                    # fft only with numpy
                    #segment_windowed = self.compute_window(segment)
                    #spectrum =self.compute_spectrum(segment_windowed)

                    window = signal.windows.hann(segment.shape[0])
                    # fft with scipy
                    spectrum = fftpack.fft2(segment*window*window.T)
                    shift = fftpack.fftshift(spectrum)
                    spectrum = 20 * np.log( np.abs(shift))

                    # compute the accumulated fingerprint
                    self.accumulated_spectra = np.add(self.accumulated_spectra, np.divide(spectrum, self.number_of_snippets))

                    self.accumulated_spectra = self.darken_region(self.accumulated_spectra)

                    # save sampled spectra for training analysis later
                    self.add_train_data(spectrum, class_name, sample_no)
                    sample_no += 1

            sample_amount += segment_count[0] * segment_count[1]

            self.save_train_data(self.train_data, class_name, train, first=first_image)
            self.train_data = pd.DataFrame()
            #self.train_data.loc[:,:] = np.NaN
            first_image=False
            #TODO: test with more images in folder

        self.save_fingerprint(self.accumulated_spectra, class_name, sample_amount, train)



    def greyscale(self, img):

        if len(img.shape) == 3 and img.shape[2] == 3:
            weight = [0.2,0.5,0.3] # weights
            weighted_mean = np.tensordot(img,weight, axes=((-1,-1)))[...,None]
        return(weighted_mean)

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

        # preallocate df
        # create dataframe
        df = pd.DataFrame(index=np.arange(0, number_of_rows), columns=self.df_header )
        # TODO: check if is initilized with 0 or NAN

        return(df)


    def add_train_data(self, spectrum, class_name, sample_no):

        # add segment fft to data_detailed
        new_sample = np.array(spectrum.reshape(spectrum.size).tolist())
        new_sample = new_sample.reshape(spectrum.size, 1)
        new_df = pd.DataFrame(new_sample.T, columns=self.df_header[:-1])
        new_df['class'] = class_name

        #df.append(new_sample, ignore_index = True)

        #self.train_data.loc[sample_no] = new_sample
        if self.train_data.empty:
            self.train_data = new_df
        else:
            #self.train_data.loc[len(self.train_data)] = new_sample
            self.train_data = self.train_data.append(new_df, ignore_index=True)


        return()



    def save_train_data(self, df_all_segments, class_name, train, first=False):

        if train:
            folder = SUBPATH + '/trained_samples/'
            file_name = folder + class_name + "_train.pkl"
        else:
            folder = SUBPATH + '/test_samples/'
            file_name = folder + class_name + "_test.pkl"

        if not os.path.exists(folder):
            os.makedirs(folder)

        if os.path.isfile(file_name) and not first:
            unpickled_df = pd.read_pickle(file_name)
            df_all_segments = unpickled_df.append(df_all_segments.dropna(axis=0), ignore_index=True)
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
        magnitude_all = magnitude_all / magnitude_all.max() #sum()
        #TODO: check what was meant with sum()?
        # self.fingerprint_df.fillna() or something to refill all values with NANs
        #self.fingerprint_df.loc[0] = magnitude_all.reshape(magnitude_all.size).tolist() + [class_name]
        #self.fingerprint_df.append(magnitude_all.reshape(magnitude_all.size).tolist() + [class_name])
        feature_vector = np.array(magnitude_all.reshape(magnitude_all.size).tolist() + [class_name])
        feature_vector = feature_vector.reshape(magnitude_all.size+1, 1)
        self.fingerprint_df = pd.DataFrame(feature_vector.T, columns=self.df_header)


        # save image: merged frequency spectrum by addition
        f_add = Image.fromarray(np.divide(magnitude_all, magnitude_all.max()) * 255).convert('RGB')

        # save image: merged frequency spectrum by addition
        path = SUBPATH + '/fingerprint/'

        if not os.path.exists(path):
            os.makedirs(path)

        if train:
            img_path = path + class_name + "_fingerprint.png"
            data_path = path + class_name + "_fingerprint.pkl"
        else:
            img_path = path + "test_" + class_name + "_fingerprint.png"
            data_path = path + "test_" + class_name + "_fingerprint.pkl"

        f_add.save(img_path, "PNG")

        magnitude_df = pd.DataFrame(magnitude_all.reshape(magnitude_all.size).tolist() + [class_name])

        magnitude_df.to_pickle(data_path)

        self.fingerprint_png = f_add
        self.accumulated_spectra = magnitude_all
        #TODO: check if accumulated spectra is better before this function computations



    def get_accumulated_spectra(self):
        return(self.accumulated_spectra)





