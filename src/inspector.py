import copy
import math

import pandas as pd
import skimage
import skimage.io
from PIL import Image
from PyQt5 import QtGui, QtWidgets

from src import hka

from config import *


class Inspector(object):
    def __init__(self):
        # every observed snippet (512,512) is reduced to a patch of 1024 (32,32)
        self.printer_types = np.array(())
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
        # (3) descriptor: mean and std of classes
        #self.mean = pd.DataFrame(columns=[i for i in range(2 * len(DIRS))])
        #self.std = pd.DataFrame(columns=[i for i in range(2 * len(DIRS))])
        self.mean = np.array(())
        self.std = np.array(())
        self.apriori = np.array(())

        self.printer_types = np.array(())

        # correctPositiveTrain = [0 for i in xrange(len(dirs))]  statt 5
        self.correctPositiveTrain = [0 for i in range(len(DIRS))]
        self.correctNegativeTrain = [0 for i in range(len(DIRS))]
        self.falsePositiveTrain = [0 for i in range(len(DIRS))]
        self.falseNegativeTrain = [0 for i in range(len(DIRS))]
        self.correctPositiveTest = [0 for i in range(len(DIRS))]
        self.correctNegativeTest = [0 for i in range(len(DIRS))]
        self.falsePositiveTest = [0 for i in range(len(DIRS))]
        self.falseNegativeTest = [0 for i in range(len(DIRS))]

        self.hitsPerClassOfInspectedSegments = [0 for i in range(len(DIRS))]

        # length of features for each printer
        self.train_feature_length = [0 for i in range(len(DIRS))]
        self.test_feature_length = [0 for i in range(len(DIRS))]




    def loadData(self, path):

        try:
            DIRS = os.listdir(path)
        except FileNotFoundError:
            print('No folder was selected. Canceled.')
            return

        print('DIRS: ', DIRS)
        print('path: ', path)

        a = 0
        self.printer_types = np.array(())
        for printer in DIRS:
            if printer == '.DS_Store':
                pass
            else:
                self.printer_types = np.append(self.printer_types, printer)
                print('Printer', printer)

        print('self.printer_types: ', self.printer_types)
        self.snippet_amount_perPrinter = np.zeros((len(self.printer_types)))

        self.mean = np.zeros((len(self.printer_types), pca_amount, 2))
        self.std = np.zeros((len(self.printer_types), pca_amount, 2))
        self.apriori = np.zeros((len(self.printer_types), 2))

        self.printer_types = self.printer_types[np.argsort(self.printer_types[:])]

        for curr in self.printer_types:
            if os.path.isdir(path + '/' + curr):
                print(curr)
                imgs = os.listdir(path + '/' + curr)
                printer_number = np.where(self.printer_types == curr)[0][0]
                # if len(imgs) >= 70:
                magnitude_all = np.zeros((SNIPPET_WIDTH, SNIPPET_WIDTH))
                magnitude_all_multi = np.ones((SNIPPET_WIDTH, SNIPPET_WIDTH))

                for img in imgs:
                    if img == '.DS_Store':
                        print('DS_Store files has not been removed.')
                    else:
                        # read image
                        img_path = path + '/' + curr + '/' + img
                        print("img path: " + img_path)
                        # /Users/resa/Studium Master/2. Semester - WiSe2014/Projekt/ipython/printers/canon/005_Canon_L02.tif
                        # tmp = skimage.io.imread(path + '/' + curr + '/' + img, plugin='tifffile')
                        tmp = skimage.io.imread(img_path)
                        # use only piece of image
                        if (tmp.shape[0] <= 1536 and tmp.shape[1] <= 1536):
                            tmp = tmp[0:1535, 0:1535]
                        # convert to grey valued image
                        if (len(tmp.shape) == 3):
                            # tmp = skimage.io.MultiImage(path + '/' + curr + '/' + img)
                            tmpGrey = tmp[:, :, 0] * 0.0722 + tmp[:, :, 1] * 0.7152 + tmp[:, :, 2] * 0.2126
                            # tmpGrey = cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY)#include opencv as cv2
                        else:
                            continue

                        # number of pixels per segents
                        nperseg = [SNIPPET_WIDTH, SNIPPET_WIDTH]  # [512,512]

                        # number of pixels which overlap
                        noverlap = np.empty([2], dtype=int)
                        noverlap[0] = 0  # nperseg[0] // 2
                        noverlap[1] = 0  # nperseg[1] // 2

                        # number of pixels to move each segment
                        step = np.empty([len(tmpGrey.shape)], dtype=int)
                        step[0] = nperseg[0] - noverlap[0]
                        step[1] = nperseg[1] - noverlap[1]

                        # number of segments in one scanned image (in both dimensions)
                        segment_count = np.empty([len(tmpGrey.shape)], dtype=int)
                        segment_count[0] = (tmpGrey.shape[0] - noverlap[0]) // step[0]
                        segment_count[1] = (tmpGrey.shape[1] - noverlap[1]) // step[1]

                        # for(each segment in img): cut of segment
                        for i in range(0, segment_count[0]):
                            for j in range(0, segment_count[1]):
                                # segment as copy of img snippet
                                start_i = i * nperseg[0]
                                start_j = j * nperseg[1]
                                segment = tmpGrey[start_i:(start_i + nperseg[0]), start_j:(start_j + nperseg[1])]
                                # cut relevant data out of scanned image
                                # tmpGreySegment = tmpGrey[:,range(96,160,2)]
                                # tmpGreySegment = tmpGreySegment[range(80,176,3),:]
                                # tmpGreySegment = tmpGreySegment.reshape(1024)
                                # tmpGreySegment = tmpGreySegment.tolist() + [curr]

                                # windowing function on segment
                                # build 1d window
                                segment_hanning = copy.copy(segment)

                                # hanning vectors
                                u_vector = np.hanning(segment.shape[0])  # eine Zeile
                                v_vector = np.hanning(segment.shape[1])  # eine Spalte

                                # 2d hanning matrix
                                for u in range(0, segment.shape[0] - 1):
                                    for v in range(0, segment.shape[1] - 1):
                                        segment_hanning[u][v] = np.multiply(u_vector[u], v_vector[v]) * 255

                                segment_windowed = copy.copy(segment)

                                # img.astype(float64)
                                # np.int8(z)

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

                                # darken region around axis
                                middle = int(magnitude_spectrum.shape[0] / 2)
                                magnitude_spectrum[middle - 5:middle + 5, :] = magnitude_spectrum.min()
                                magnitude_spectrum[:, middle - 5:middle + 5] = magnitude_spectrum.min()

                                # norm: max = 1 (for one segment)
                                # mag_normed = np.divide(magnitude_spectrum,magnitude_spectrum.max())
                                # mag_shift = mag_normed - mag_normed.mean()
                                # mag_shift = np.divide(mag_shift, (mag_shift.max() - mag_shift.min()))
                                mag_shift = np.divide(magnitude_spectrum,
                                                      segment_count[0] * segment_count[1] * len(imgs))

                                # add and multiply cumulative
                                magnitude_all += mag_shift
                                magnitude_all_multi *= mag_shift
                                # add segment fft to data_detailed
                                data_merged

                # add class and add one per printer to pandas dataframes
                # norm additive + multiplied spectras
                # magnitude_all = np.divide(magnitude_all, magnitude_all.max())
                # magnitude_all = magnitude_all - magnitude_all.mean()
                # magnitude_all = np.divide(magnitude_all, (magnitude_all.max()-magnitude_all.min()))
                idx = np.argsort(magnitude_all.flatten())
                b = magnitude_all.flatten()[idx]

                threshold = b[b.size - NUMBER_PIXELS]

                min = magnitude_all.min()
                # select only 1000 brightest pixel
                magnitude_all[magnitude_all < threshold] = min
                # magnitude_all_multi[magnitude_all_multi<threshold] = min

                magnitude_all = magnitude_all - magnitude_all.min()
                magnitude_all = magnitude_all / magnitude_all.sum()

                self.data_merged.loc[printer_number] = magnitude_all.reshape(magnitude_all.size).tolist() + [curr]
                # self.data_merged_multi.loc[printer_number] = magnitude_all_multi.reshape(magnitude_all_multi.size).tolist() + [curr]

                # save image: merged frequency spectrum by addition
                f_add = Image.fromarray(np.divide(magnitude_all, magnitude_all.max()) * 255).convert('RGB')

                # save image: merged frequency spectrum by addition

                # use a threshold (only for visualization)
                self.snippet_amount_perPrinter[printer_number] = segment_count[0] * segment_count[1] * len(imgs)
                mean = np.divide(magnitude_all_multi.mean(), self.snippet_amount_perPrinter[printer_number])

                # do the same for multiplied
                idx = np.argsort(magnitude_all_multi.flatten())
                c = magnitude_all.flatten()[idx]

                threshold = c[c.size - NUMBER_PIXELS]
                min = magnitude_all_multi.min()
                magnitude_all_multi[magnitude_all_multi < threshold] = min

                magnitude_all_multi = magnitude_all_multi - min
                magnitude_all_multi = magnitude_all_multi / magnitude_all_multi.sum()

                # self.data_merged_multi.loc[printer_number] = magnitude_all_multi.reshape(magnitude_all_multi.size).tolist() + [curr]

                f_multi = Image.fromarray(magnitude_all_multi).convert('RGB')
                f_add.save(curr + "_merged_add.png", "PNG")
                f_multi.save(curr + "_merged_multi.png", "PNG")


        print("load and prepare data finished!")
        # self.statusBar().showMessage('images are loaded.')
        print('images are loaded.')

    def saveSpectra(self):

        filter = "Folder which contains the data_detailed.pkl and data_merged.pkl files. (*.*)"
        path = QtWidgets.QFileDialog.getExistingDirectory(directory='..', options=QtWidgets.QFileDialog.ShowDirsOnly)
        print('selected path to save data: ', path)

        if ACCUMULATED_SPECTRA:
            if self.data_merged.empty == False:
                try:
                    self.data_merged.to_pickle(path + "/data_merged.pkl")
                    # self.data_merged_multi.to_pickle(SUBPATH,"/data_merged_multi.pkl")
                    self.data_detailed.to_pickle(path + "/data_detailed.pkl")
                    print("Saved computed data!")
                except FileNotFoundError:
                    print('No folder was selected. Canceled.')
                    return

            else:
                print("Data is still empty, press load first.")
        else:
            if self.data.empty == False:
                try:
                    self.data.to_pickle(path + "/spectra.pkl")
                    print("Saved computed!")
                except FileNotFoundError:
                    print('No folder was selected. Canceled.')
                    return

            else:
                print("Data is still empty, press load first.")

    def getSpectra(self, path):

        if ACCUMULATED_SPECTRA:
            try:
                self.data_merged = pd.read_pickle(path + "/data_merged.pkl")
                # self.data_merged_multi = pd.read_pickle(SUBPATH+"/data_merged_multi.pkl")
                self.data_detailed = pd.read_pickle(path + "/data_detailed.pkl")
            except FileNotFoundError:
                print('No folder was selected. Canceled.')
                return

            class_column = self.data_detailed.shape[1] - 1
            self.printer_types = np.unique([printer for printer in self.data_detailed.ix[:, class_column]])
            #self.printer_types = self.printer_types
            self.snippet_amount_perPrinter = np.zeros((len(self.printer_types)))
            for i in range(self.printer_types.shape[0]):
                self.snippet_amount_perPrinter[i] = \
                    self.data_detailed[self.data_detailed.ix[:, class_column] == self.printer_types[i]].shape[0]

            if self.data_merged.empty:
                print("No data found.")
            else:
                print("Got data!")

        else:
            self.data = pd.read_pickle("B_additiveCorrelation_id_w512_1000px/spectra.pkl")
            self.printer_types = np.unique([printer for printer in self.data.ix[:, 1024]])
            self.printer_types = self.printer_types[np.argsort(self.printer_types[:])]
            self.snippet_amount_perPrinter = np.zeros((len(self.printer_types)))
            if self.data.empty:
                print("No data found.")
            else:
                print("Got data!")

        self.mean = np.zeros((len(self.printer_types), pca_amount, 2))
        self.std = np.zeros((len(self.printer_types), pca_amount, 2))
        self.apriori = np.zeros((len(self.printer_types), 2))

    def training(self):
        if ACCUMULATED_SPECTRA:
            data_normed = np.zeros((self.printer_types.size, SNIPPET_WIDTH, SNIPPET_WIDTH))
            class_column = self.data_detailed.shape[1] - 1
            sum = np.zeros((self.printer_types.size))

            self.printer_types = self.printer_types[np.argsort(self.printer_types[:])]

            if TRAINING == True:
                for p in range(self.printer_types.size):
                    # vector = np.array(np.divide(self.data_merged.ix[p,:-1],self.snippet_amount_perPrinter[p]))
                    vector = np.array(self.data_merged.ix[p, :-1])
                    data_normed[p, :, :] = np.reshape(vector, (SNIPPET_WIDTH, SNIPPET_WIDTH))
                    sum[p] = np.sum(np.sum(data_normed[p]))
                    # data_normed[p,:,:] = np.divide(data_normed[p,:,:],sum[p])
                    # Training
                    pd.DataFrame(data_normed[p]).to_pickle(SUBPATH + "/corr_" + str(self.printer_types[p]) + ".pkl")
            else:
                # Test data
                for p in range(self.printer_types.size):
                    data_normed[p] = pd.read_pickle("knowledge/corr_" + self.printer_types[p] + ".pkl")

            nr_segments = self.data_detailed.shape[0]
            correlation_list = np.zeros((nr_segments, self.printer_types.size + 1))

            printers_nr = np.arange(self.printer_types.size)

            for i in range(self.data_detailed.shape[0]):
                p_id = self.data_detailed.ix[i, class_column]
                printer_number = np.where(self.printer_types == p_id.astype(np.str_))[0][0]

                # prove similarity - correlation of segment ffts with additive spcectras
                for p in range(len(self.printer_types)):
                    correlation_list[i, p] = np.dot(self.data_detailed.ix[i, :class_column],
                                                    data_normed[p, :, :].reshape(class_column))

                    correlation_list[i, p + 1] = printer_number

            for p in range(len(self.printer_types)):

                printer_list = correlation_list[correlation_list[:, -1] == p]
                # for each segment from one printer
                for row in range(printer_list.shape[0]):
                    # printer_list[row,:].max()
                    likeliest_class = np.where(printer_list[row, :] == printer_list[row, :].max())[0][0]

                    if likeliest_class == p:
                        print(p, ": TRUE classification.")
                        self.correctPositiveTrain[p] += 1

                        li = np.delete(printers_nr, p)
                        for l in li:
                            self.correctNegativeTrain[l] += 1
                    else:
                        # falseClassification:
                        self.falseNegativeTrain[p] += 1  # printer p was not identified
                        self.falsePositiveTrain[likeliest_class] += 1  # printer likeliest_class was wrongly detected
                        li = np.delete(printers_nr, p)
                        li = np.delete(li, likeliest_class - 1)
                        for l in li:
                            self.correctNegativeTrain[l] += 1

                        print(p, ": False.")

            # for p in range(len(self.printer_types)):
            pd.DataFrame(np.array(self.correctPositiveTrain)).to_pickle(SUBPATH + "/correctPositive.pkl")
            pd.DataFrame(np.array(self.correctNegativeTrain)).to_pickle(SUBPATH + "/correctNegative.pkl")
            pd.DataFrame(np.array(self.falsePositiveTrain)).to_pickle(SUBPATH + "/falsePositive.pkl")
            pd.DataFrame(np.array(self.falseNegativeTrain)).to_pickle(SUBPATH + "/falseNegative.pkl")

        else:
            self.train = pd.DataFrame()
            self.test = pd.DataFrame()

            # randomly reorder data
            data_rand = self.data.reindex(np.random.permutation(self.data.index))
            data_rand.index = range(0, len(data_rand))

            self.printer_types = self.printer_types[np.argsort(self.printer_types[:])]
            # chose same amount of data from each class
            for printer in self.printer_types:
                printer_data = data_rand[data_rand['name'] == printer].copy()
                printer_data.index = range(0, len(printer_data))
                splitpoint = int(round(printer_data.shape[0] * 0.6))

                self.train = self.train.append(printer_data.ix[0:splitpoint, :])
                self.train.index = range(0, len(self.train))
                self.test = self.test.append(printer_data.ix[splitpoint + 1:, :])
                self.test.index = range(0, len(self.test))

            # PCA
            self.axis, self.eigenData, s = hka.hka(self.train.transpose().ix[:1024, :])

            # export hka
            name_eigen = SUBPATH + "/eigenData.pkl"
            pd.DataFrame(self.eigenData).to_pickle(name_eigen)

            print("pca finished!")
            # Eigen-Spektren
            # for i in range(7):
            #     self.pic = self.eigenData[:,i].reshape(32,32)
            # plt.figure()
            # plt.imshow(pic, cmap=plt.cm.gray)
            # plt.show()

            # split up into train and test set
            z = 0

            self.printer_types = self.printer_types[np.argsort(self.printer_types[:])]
            for printer in self.printer_types:
                print("Start learning ", printer)
                printer_number = np.where(self.printer_types == printer)[0][0]
                # Feature Extraction
                train_feature = pd.DataFrame()
                for j in range(len(self.train)):
                    feature = np.zeros(pca_amount + 1)
                    if self.train['name'].ix[j] == printer:
                        feature[pca_amount] = 1
                    else:
                        feature[pca_amount] = -1

                    for i in range(pca_amount):
                        feature[i] = self.eigenData[:, i].T * np.matrix(self.train.ix[j, :1024]).T
                    train_feature[j] = feature

                test_feature = pd.DataFrame()
                for j in range(len(self.test)):
                    feature = np.zeros(pca_amount + 1)
                    if self.test['name'].ix[j] == printer:
                        feature[pca_amount] = 1
                    else:
                        feature[pca_amount] = -1

                    for i in range(pca_amount):
                        feature[i] = self.eigenData[:, i].T * np.matrix(self.test.ix[j, :1024]).T
                    test_feature[j] = feature

                train_feature = train_feature.transpose()
                test_feature = test_feature.transpose()

                train_feature.rename(columns={pca_amount: 'label'}, inplace=True)
                test_feature.rename(columns={pca_amount: 'label'}, inplace=True)

                # Gaussian Naive Bayes - Training
                mean = pd.DataFrame()
                mean[0] = np.matrix(train_feature[train_feature['label'] == 1].mean()[0:pca_amount]).tolist()[0]
                mean[1] = np.matrix(train_feature[train_feature['label'] == -1].mean()[0:pca_amount]).tolist()[0]

                std = pd.DataFrame()
                std[0] = np.matrix(train_feature[train_feature['label'] == 1].std()[0:pca_amount]).tolist()[0]
                std[1] = np.matrix(train_feature[train_feature['label'] == -1].std()[0:pca_amount]).tolist()[0]

                apriori = np.array([len(train_feature[train_feature['label'] == 1]) / float(len(train_feature)),
                                    len(train_feature[train_feature['label'] == -1]) / float(len(train_feature))])

                self.mean[printer_number, :, :] = mean
                self.std[printer_number, :, :] = std
                self.apriori[printer_number, :] = apriori

                # export gaussian naive bayes
                name_mean = SUBPATH + "/" + printer + "_mean.pkl"
                mean.to_pickle(name_mean)
                name_std = SUBPATH + "/" + printer + "_std.pkl"
                std.to_pickle(name_std)
                name_apriori = SUBPATH + "/" + printer + "_apriori.pkl"
                a = pd.DataFrame(apriori)
                a.to_pickle(name_apriori)

                # Train Set
                [self.correctPositiveTrain[z], self.correctNegativeTrain[z], self.falsePositiveTrain[z], self.falseNegativeTrain[z], tmp,
                 tmp] = GNBMatch(train_feature, mean, std, apriori, 1)
                self.train_feature_length[z] = len(train_feature)
                # Test Set
                [self.correctPositiveTest[z], self.correctNegativeTest[z], self.falsePositiveTest[z], self.falseNegativeTest[z], tmp,
                 tmp] = GNBMatch(test_feature, mean, std, apriori, 1)
                self.test_feature_length[z] = len(test_feature)
                print("GNB training finished.")
                z = z + 1

        print("Training for all printers finished.")


    def getCorrelation(self, path):

        try:
            self.data_merged = pd.read_pickle(path + "/data_merged.pkl")
            # self.data_merged_multi = pd.read_pickle(SUBPATH+"/data_merged_multi.pkl")
            self.data_detailed = pd.read_pickle(path + "/data_detailed.pkl")
        except FileNotFoundError:
            print('No folder was selected. Canceled.')
            return

        class_column = self.data_detailed.shape[1] - 1
        self.printer_types = []
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
        self.apriori = np.zeros((len(self.printer_types), 2))

        self.training()


    def saveCorrelation(self):

        filter = "Folder which contains the data_detailed.pkl and data_merged.pkl files. (*.*)"
        path = QtWidgets.QFileDialog.getExistingDirectory(directory='..', options=QtWidgets.QFileDialog.ShowDirsOnly)
        print('selected path to save data: ', path)

        if self.data_merged.empty == False:
            try:
                self.data_merged.to_pickle(path + "/data_merged.pkl")
                # self.data_merged_multi.to_pickle(SUBPATH,"/data_merged_multi.pkl")
                self.data_detailed.to_pickle(path + "/data_detailed.pkl")
                print("saved merged spectra!")
            except FileNotFoundError:
                print('No folder was selected. Canceled.')
                return

        else:
            print("Data is still empty, press load first.")



    def saveStat(self):

        pass


    def loadImg(self, filename):
        qimg = QtGui.QImage()
        self.questioned = pd.DataFrame(columns=col)
        self.questioned_detailed = pd.DataFrame(columns=col_large)

        try:
            print((filename[0]), "2. ", (filename[0]))
            qimg.load(filename[0])
            print("image is loaded.")

            ## pixmap = QtGui.QPixmap.fromImage(qimg) # show loaded image in screen (too large)
            ## self.lbl2.setPixmap(pixmap) # show loaded image in screen (too large)

            tmp = skimage.io.imread(str(filename[0]))
            #tmp = skimage.io.imread(filename)

        except FileNotFoundError:
                print('No file was selected. Canceled.')
                return

        if tmp.size == 0:
            print("Image could not be load: ")
            print(filename[0])
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
        magnitude_all = np.zeros((SNIPPET_WIDTH, SNIPPET_WIDTH))
        magnitude_all_multi = np.ones((SNIPPET_WIDTH, SNIPPET_WIDTH))


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

                # darken region around axis
                middle = int(magnitude_spectrum.shape[0] / 2)
                magnitude_spectrum[middle - 5:middle + 5, :] = magnitude_spectrum.min()
                magnitude_spectrum[:, middle - 5:middle + 5] = magnitude_spectrum.min()

                # norm: max = 1 (for one segment)
                # mag_normed = np.divide(magnitude_spectrum,magnitude_spectrum.max())
                # mag_shift = mag_normed - mag_normed.mean()
                # mag_shift = np.divide(mag_shift, (mag_shift.max() - mag_shift.min()))
                mag_shift = np.divide(magnitude_spectrum,
                                      segment_count[0] * segment_count[1] )

                # add and multiply cumulative
                magnitude_all += mag_shift
                magnitude_all_multi *= mag_shift
                # add segment fft to data_detailed
                self.questioned_detailed.loc[a] = magnitude_spectrum.reshape(
                        magnitude_spectrum.size).tolist() + ["Q"]

                a = a + 1

        # after all segments are computed and saved as frequencies
        return qimg

        print("Feature extraction of questioned document finished.")
        # self.lbl2.show() # show loaded image in screen (too large)

    def inspection(self):
        data_normed = np.zeros((self.printer_types.size, SNIPPET_WIDTH, SNIPPET_WIDTH))
        class_column = self.questioned_detailed.shape[1] - 1
        sum = np.zeros((self.printer_types.size))

        self.printer_types = self.printer_types[np.argsort(self.printer_types[:])]
        if TRAINING == True:
            for p in range(self.printer_types.size):
                # vector = np.array(np.divide(self.data_merged.ix[p,:-1],self.snippet_amount_perPrinter[p]))
                vector = np.array(self.data_merged.ix[p, :-1])
                data_normed[p, :, :] = np.reshape(vector, (SNIPPET_WIDTH, SNIPPET_WIDTH))
                sum[p] = np.sum(np.sum(data_normed[p]))
                # data_normed[p,:,:] = np.divide(data_normed[p,:,:],sum[p])
                # Training
                pd.DataFrame(data_normed[p]).to_pickle(SUBPATH + "/corr_" + self.printer_types[p] + ".pkl")
        else:
            # Test data
            for p in range(self.printer_types.size):
                data_normed[p] = pd.read_pickle("knowledge/corr_" + self.printer_types[p] + ".pkl")

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



    def saveResult(self):

        print(self.hitsPerClassOfInspectedSegments)



def GNB(x, mean, std):
    return 1 / math.sqrt(2 * math.pi * std) * math.exp(-1 / 2.0 * (x - mean) ** 2 / std ** 2)


def GNBMatch(matchData, mean, std, apriori, c):
    correctPositive = 0
    correctNegative = 0
    falsePositive = 0
    falseNegative = 0
    gMin = 10
    gMax = 0

    for k in range(0, len(matchData)):
        w1Prob = 1
        w2Prob = 1
        for j in range(pca_amount):
            w1Prob = w1Prob * GNB(matchData.ix[k, j], mean.ix[j, 0], std.ix[j, 0])
            w2Prob = w2Prob * GNB(matchData.ix[k, j], mean.ix[j, 1], std.ix[j, 1])

        g = (apriori[0] * w1Prob) / (apriori[1] * w2Prob)
        if g < gMin:
            gMin = g
        if g > gMax:
            gMax = g

        g = g * c - 1

        if g > 0:
            if matchData['label'][k] == 1:
                correctPositive = correctPositive + 1
            else:
                falsePositive = falsePositive + 1
        else:
            if matchData['label'][k] == 1:
                falseNegative = falseNegative + 1
            else:
                correctNegative = correctNegative + 1

    return [correctPositive, correctNegative, falsePositive, falseNegative, gMin, gMax]
