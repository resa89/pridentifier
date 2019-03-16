from PyQt5 import QtGui

import pandas as pd
from matplotlib.pyplot import *
import skimage
import skimage.io
import copy

DIRS = ['Brother', 'Canon_Pro', 'HP', 'CanonMX870']

dbimport = False  # True: imgs from ftp server, False: imgs from local folder

# parameter for snippet features
snippet_w = 512
nr_pixels = 10000
scale_fft = False

# method: adding spectra
add_all_fft = True

# method: pca
pca_amount = 20

TRAINING = False  # if False: then generating self.test dataset statistics

col = [i for i in range(1024)]
col_large = [i for i in range(512*512)]
col.append('name')
col_large.append('name')


# every observed snippet (512,512) is reduced to a patch of 1024 (32,32)



class Pridentifier(object):

    def __init__(self):

        self.printer_types = np.array(())

        # self.correctPositiveself.train = [0 for i in xrange(len(dirs))]  statt 5
        self.correctPositiveTrain = [0 for i in range(len(DIRS))]
        self.correctNegativeTrain = [0 for i in range(len(DIRS))]
        self.falsePositiveselfTrain = [0 for i in range(len(DIRS))]
        self.falseNegativeselfTrain = [0 for i in range(len(DIRS))]
        self.correctPositiveselfTrain = [0 for i in range(len(DIRS))]
        self.correctNegativeselfTrain = [0 for i in range(len(DIRS))]
        self.falsePositiveselfTrain = [0 for i in range(len(DIRS))]
        self.falseNegativeselfTrain = [0 for i in range(len(DIRS))]

        self.hitsPerClassOfInspectedSegments = [0 for i in range(len(DIRS))]

        # length of features for each printer
        self.train_feature_length = [0 for i in range(len(DIRS))]
        self.test_feature_length = [0 for i in range(len(DIRS))]

        self.snippet_amount_perPrinter = np.array(())

        # (1) imgs with their class
        self.data = pd.DataFrame(columns=col)
        self.data_merged = pd.DataFrame(columns=col_large)
        #self.data_merged_multi = pd.DataFrame(columns=col_large)
        self.data_detailed = pd.DataFrame(columns=col_large)
        self.questioned = pd.DataFrame()
        self.questioned_detailed = pd.DataFrame()

        self.train = pd.DataFrame()
        self.test = pd.DataFrame()
        ## (2) imgs in feature representation
        # self.train_feature = pd.DataFrame()
        # self.test_feature = pd.DataFrame()
        # (3) descriptor: self.mean and self.std of classes
        #self.mean = pd.DataFrame(columns=[i for i in range(2 * len(DIRS))])
        #self.std = pd.DataFrame(columns=[i for i in range(2 * len(DIRS))])
        self.mean = np.array(())
        self.std = np.array(())
        self.apriori  = np.array(())



    def loadtraining(self, path):

        print('selected path to get data: ', path)

        if path:
            try:
                self.data_merged = pd.read_pickle(path + "/data_merged.pkl")
                # self.data_merged_multi = pd.read_pickle(SUBPATH+"/self.data_merged_multi.pkl")
                self.data_detailed = pd.read_pickle(path + "/data_detailed.pkl")
            except FileNotFoundError:
                print('No folder was selected. Canceled.')
                return

            class_column = self.data_detailed.shape[1] - 1

            self.printer_types = np.unique([printer for printer in self.data_detailed.ix[:, class_column]])

            self.printer_types = self.printer_types[np.argsort(self.printer_types[:])]

            if type(self.printer_types[0]) == np.bytes_:
                self.printer_types = self.printer_types.astype(np.str_)

            #self.printer_types = self.printer_types[np.argsort(self.printer_types[:])]
            self.snippet_amount_perPrinter = np.zeros((len(self.printer_types)))
            for i in range(self.printer_types.shape[0]):
                self.snippet_amount_perPrinter[i] = \
                    self.data_detailed[self.data_detailed.ix[:, class_column] == self.printer_types[i]].shape[0]

            if self.data_merged.empty:
                print("No knowledge found.")
            else:
                print("Got knowledge!")

            self.mean = np.zeros((len(self.printer_types), pca_amount, 2))
            self.std = np.zeros((len(self.printer_types), pca_amount, 2))
            self.apriori  = np.zeros((len(self.printer_types), 2))



    def loadImg(self, filename):

        qimg = QtGui.QImage()
        self.questioned = pd.DataFrame(columns=col)
        self.questioned_detailed = pd.DataFrame(columns=col_large)

        try:
            print((filename), "2. ", (filename))
            qimg.load(filename)
            print("image is loaded.")

            ## pixmap = QtGui.QPixmap.fromImage(qimg) # show loaded image in screen (too large)
            ## lbl2.setPixmap(pixmap) # show loaded image in screen (too large)

            tmp = skimage.io.imread(str(filename))
            #tmp = skimage.io.imread(filename)

        except FileNotFoundError:
                print('No file was selected. Canceled.')
                return

        if tmp.size == 0:
            print("Image could not be load: ")
            print(filename)
            # return False

        if (len(tmp.shape) == 3):
            tmpGrey = tmp[:, :, 0] * 0.0722 + tmp[:, :, 1] * 0.7152 + tmp[:, :, 2] * 0.2126
        # compute FFT spectra for serveral segments
        a = 0
        # number of pixels per segents
        nperseg = [512, 512]

        # number of pixels which overlap
        noverlap = np.empty([2], dtype=int)
        noverlap[0] = 0 # nperseg[0] // 2
        noverlap[1] = 0 # nperseg[1] // 2
        # number of pixels to move each segment
        step = np.empty([len(tmpGrey.shape)], dtype=int)
        step[0] = nperseg[0] - noverlap[0]
        step[1] = nperseg[1] - noverlap[1]

        # number of segments in one scanned image (in both dimensions)
        segment_count = np.empty([len(tmpGrey.shape)], dtype=int)
        segment_count[0] = (tmpGrey.shape[0] - noverlap[0]) // step[0]
        segment_count[1] = (tmpGrey.shape[1] - noverlap[1]) // step[1]

        # if len(imgs) >= 70:
        magnitude_all = np.zeros((snippet_w, snippet_w))
        magnitude_all_multi = np.ones((snippet_w, snippet_w))


        # for(each segment in img): cut of segment
        for i in range(0, segment_count[0] - 1):
            for j in range(0, segment_count[1] - 1):
                # segment as copy of img snippet
                start_i = i * nperseg[0]
                start_j = j * nperseg[1]
                segment = tmpGrey[start_i:(start_i + nperseg[0]), start_j:(start_j + nperseg[1])]#[i:(i + nperseg[0]), j:(j + nperseg[1])]
                segment_hanning = copy.copy(segment)

                # hanning vectors
                u_vector = np.hanning(segment.shape[0])  # eine Zeile
                v_vector = np.hanning(segment.shape[1])  # eine Spalte

                # 2d hanning matrix
                for u in range(0, segment.shape[0] - 1):
                    for v in range(0, segment.shape[1] - 1):
                        segment_hanning[u][v] = np.multiply(u_vector[u], v_vector[v]) * 255

                segment_windowed = copy.copy(segment)

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

                # compute fft for every segment in an image
                f = np.fft.fft2(segment_windowed)
                fshift = np.fft.fftshift(f)
                magnitude_spectrum = 20 * np.log(np.abs(fshift))

                if add_all_fft:
                    # darken region around axis
                    middle = int(magnitude_spectrum.shape[0] / 2)
                    magnitude_spectrum[middle - 5:middle + 5, :] = magnitude_spectrum.min()
                    magnitude_spectrum[:, middle - 5:middle + 5] = magnitude_spectrum.min()

                    # norm: max = 1 (for one segment)
                    # mag_normed = np.divide(magnitude_spectrum,magnitude_spectrum.max())
                    # mag_shift = mag_normed - mag_normed.self.mean()
                    # mag_shift = np.divide(mag_shift, (mag_shift.max() - mag_shift.min()))
                    mag_shift = np.divide(magnitude_spectrum,
                                          segment_count[0] * segment_count[1] )

                    # add and multiply cumulative
                    magnitude_all += mag_shift
                    magnitude_all_multi *= mag_shift
                    # add segment fft to self.data_detailed
                    self.questioned_detailed.loc[a] = magnitude_spectrum.reshape(
                            magnitude_spectrum.size).tolist() + ["Q"]
                else:
                    # add class to list
                    # save spectrum in data (magnitude_spectrum or fshift ?)
                    # range(241,272,1)
                    if not scale_fft:
                        magnitude_cut = magnitude_spectrum[:,
                                        range(96, 160, 1)]  # 192,320,4 for snippet-size 512,512
                        # 64,192,4 for snippet-size: 256,256
                        magnitude_cut = magnitude_cut[range(96, 160, 1),
                                        :]  # 192,320,4 for snippet-size 512,512
                        # 64,192,4 for snippet-size: 256,256
                    else:
                        magnitude_cut = magnitude_spectrum[:, range(96, 160, 1)]
                        magnitude_cut = magnitude_cut[range(96, 160, 1), :]
                        magnitude_cut = magnitude_cut.reshape(1024)

                    magnitude_list = magnitude_cut.tolist() + ["Q"]
                    questioned.loc[a] = magnitude_list


                    # save spectrum in data (magnitude_spectrum or fshift ?)
                    # range(241,272,1)
                    magnitude_cut = magnitude_spectrum[:, range(192, 320, 4)]
                    magnitude_cut = magnitude_cut[range(192, 320, 4), :]
                    magnitude_cut = magnitude_cut.reshape(1024)
                    magnitude_cut = magnitude_cut.tolist() + ["Q"]
                    questioned.loc[a] = magnitude_cut
                a = a + 1

        # after all segments are computed and saved as frequencies
        return qimg

        print("Feature extraction of self.questioned document finished.")
        # lbl2.show() # show loaded image in screen (too large)


    def inspect(self):

        self.printer_types = np.array(DIRS)

        data_normed = np.zeros((self.printer_types.size, snippet_w, snippet_w))
        class_column = self.questioned_detailed.shape[1] - 1
        sum = np.zeros((self.printer_types.size))

        self.printer_types = self.printer_types[np.argsort(self.printer_types[:])]
        if TRAINING == True:
            pass
        else:
            # self.test data
            for p in range(self.printer_types.size):
                data_normed[p] = pd.read_pickle("../knowledge/corr_" + self.printer_types[p] + ".pkl")

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
        # for each segment from one self.questioned print
        for row in range(questioned_list.shape[0]):
            likeliest_class = np.where(questioned_list[row, :] == questioned_list[row, :].max())[0][0]

            self.hitsPerClassOfInspectedSegments[likeliest_class] += 1

        print("training for all printers finished.")
        return self.hitsPerClassOfInspectedSegments


    def saveResult(self):

        result_printer = -1

        for index in np.arange(len(self.hitsPerClassOfInspectedSegments)):

            if self.hitsPerClassOfInspectedSegments[index] == 1:
                result_printer = index
            else:
                pass

        print(self.printer_types[result_printer])




def main():

    identifier = Pridentifier()

    identifier.loadtraining('/Users/resa/Projekte/01_Korensics/02-Pridentifier/trainedData')

    identifier.loadImg('/Users/resa/Projekte/01_Korensics/02-Pridentifier/data/images/id/Canon_Pro/idcard_16.jpg')

    identifier.inspect()

    identifier.saveResult()




if __name__ == '__main__':

    main()
