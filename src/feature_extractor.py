import os.path
import sys

import pickle
import numpy as np
from PIL import Image
from scipy import misc
import pandas as pd
from scipy import fftpack
from scipy import signal
import imageio

import config


class FeatureExtractor(object):

    def __init__(self, path, img_names, number_of_snippets, classes, SNIPPET_WIDTH, NUMBER_PIXELS, train=True):
        self.path_to_class = path
        self.img_names = img_names
        self.number_of_snippets = number_of_snippets
        self.train = train
        self.classes = classes
        self.SNIPPET_WIDTH = SNIPPET_WIDTH
        self.NUMBER_PIXELS = NUMBER_PIXELS
        self.accumulated_spectra = np.zeros((self.SNIPPET_WIDTH, self.SNIPPET_WIDTH))
        # df header
        self.df_header = [i for i in range(self.SNIPPET_WIDTH*self.SNIPPET_WIDTH)]
        self.df_header = self.df_header  + ['class']
        # allocate memory
        #self.fingerprint_df = pd.DataFrame(index=[0], columns=self.df_header, dtype=float)
        #self.fingerprint_df = pd.DataFrame(columns=self.df_header)
        self.fingerprint_df = pd.DataFrame()


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
        step[0] = self.SNIPPET_WIDTH
        step[1] = self.SNIPPET_WIDTH

        segment_count = np.empty([2], dtype=int)

        first_image = True

        overall_sample_no = 0

        for image in self.img_names:
            img_path = self.path_to_class + '/' + image
            img = imageio.imread(img_path)

            grey_img = self.greyscale(img)

            # number of segments in one scanned image (in both dimensions)
            segment_count[0] = grey_img.shape[0] // step[0]
            segment_count[1] = grey_img.shape[1] // step[1]

            sample_no = 0

            # for(each segment in img): cut of segment
            for i in range(0, segment_count[0]):
                for j in range(0, segment_count[1]):
                    # segment as copy of img snippet
                    start_i = i * self.SNIPPET_WIDTH
                    start_j = j * self.SNIPPET_WIDTH
                    segment = grey_img[start_i:(start_i + self.SNIPPET_WIDTH), start_j:(start_j + self.SNIPPET_WIDTH), 0]

                    # fft only with numpy
                    #segment_windowed = self.compute_window(segment)
                    #spectrum =self.compute_spectrum(segment_windowed)

                    window = signal.windows.hann(segment.shape[0])
                    # fft with scipy
                    spectrum = fftpack.fft2(segment*window*window.T)
                    shift = fftpack.fftshift(spectrum)
                    spectrum = 20 * np.log( np.abs(shift))

                    spectrum = self.darken_region(spectrum)

                    mag_shift = np.divide(spectrum, self.number_of_snippets)

                    # compute the accumulated fingerprint
                    self.accumulated_spectra = np.add(self.accumulated_spectra, mag_shift)

                    # save sampled spectra for training analysis later
                    self.add_train_data(spectrum, class_name, sample_no)
                    sample_no += 1
                    overall_sample_no += 1

                    if train:
                        index_of_class = self.classes.index(class_name)
                        config.state_analysis = index_of_class*100/len(self.classes)+\
                                                (overall_sample_no/self.number_of_snippets*100)//len(self.classes)
                    else:
                        # //2 because the second step is the evaluation of the inspected image
                        config.state_inspection = (overall_sample_no/self.number_of_snippets*100)//2


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
            folder = config.SUBPATH + '/trained_samples/'
            file_name = folder + class_name + "_train.pkl"
        else:
            folder = config.SUBPATH + '/test_samples/'
            file_name = folder + class_name + "_test.pkl"

        if not os.path.exists(folder):
            os.makedirs(folder)

        if not first: # and os.path.isfile(file_name)
            unpickled_df = try_to_load_as_pickled_object_or_None(file_name)
            df_all_segments = unpickled_df.append(df_all_segments, ignore_index=True)
            save_as_pickled_object(df_all_segments, file_name)
        else:
            save_as_pickled_object(df_all_segments, file_name)





    def save_fingerprint(self, magnitude_all, class_name, sample_amount, train):

        # add class and add one per printer to pandas dataframes
        # norm additive + multiplied spectras
        # magnitude_all = np.divide(magnitude_all, magnitude_all.max())
        # magnitude_all = magnitude_all - magnitude_all.mean()
        # magnitude_all = np.divide(magnitude_all, (magnitude_all.max()-magnitude_all.min()))

        # norm the accumulated_spectra
        idx = np.argsort(magnitude_all.flatten())
        b = magnitude_all.flatten()[idx]

        # feature count can only be as large as snippet pixels amount
        #TODO: return message to inform user
        if b.size <= self.NUMBER_PIXELS:
            features = b.size-1
        else:
            features = b.size - self.NUMBER_PIXELS

        threshold = b[features]

        min = magnitude_all.min()
        # select only 1000 brightest pixel
        magnitude_all[magnitude_all < threshold] = min
        # magnitude_all_multi[magnitude_all_multi<threshold] = min

        magnitude_all = magnitude_all - magnitude_all.min()
        magnitude_all = magnitude_all / magnitude_all.sum() # divide by sum, to make fingerprints comparable

        # self.fingerprint_df.fillna() or something to refill all values with NANs
        #self.fingerprint_df.loc[0] = magnitude_all.reshape(magnitude_all.size).tolist() + [class_name]
        #self.fingerprint_df.append(magnitude_all.reshape(magnitude_all.size).tolist() + [class_name])
        feature_vector = np.array(magnitude_all.reshape(magnitude_all.size).tolist() + [class_name])
        feature_vector = feature_vector.reshape(magnitude_all.size+1, 1)
        self.fingerprint_df = pd.DataFrame(feature_vector.T, columns=self.df_header)


        # save image: merged frequency spectrum by addition
        f_add = Image.fromarray(np.divide(magnitude_all, magnitude_all.max()) * 255).convert('RGB')

        # save image: merged frequency spectrum by addition
        path = config.SUBPATH + '/fingerprint/'

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





def save_as_pickled_object(obj, filepath):
    """
    This is a defensive way to write pickle.write, allowing for very large files on all platforms
    """
    print(sys.platform)
    if sys.platform == "darwin": # OS X
        max_bytes = 2**31 - 1
        bytes_out = pickle.dumps(obj)
        n_bytes = sys.getsizeof(bytes_out)
        with open(filepath, 'wb') as f_out:
            for idx in range(0, n_bytes, max_bytes):
                f_out.write(bytes_out[idx:idx+max_bytes])
    else:
        obj.to_pickle(filepath)



def try_to_load_as_pickled_object_or_None(filepath):
    """
    This is a defensive way to write pickle.load, allowing for very large files on all platforms
    """
    print(sys.platform)
    if sys.platform == "darwin": # OS X
        max_bytes = 2**31 - 1
        try:
            input_size = os.path.getsize(filepath)
            bytes_in = bytearray(0)
            with open(filepath, 'rb') as f_in:
                for _ in range(0, input_size, max_bytes):
                    bytes_in += f_in.read(max_bytes)
            obj = pickle.loads(bytes_in)
        except:
            return None
    else:
        obj = pd.read_pickle(filepath)

    return obj

