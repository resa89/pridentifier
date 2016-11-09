#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Drop Matrix Inspector

This application is to explore, research and inspect
printed documents and their printers.

author: Theresa Kocher
last edited: August 2015
"""

#import sys
#sys.path.append('/usr/local/lib/python2.7/site-packages')
from PyQt4 import QtGui, QtCore

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import os
import skimage
import skimage.io
import copy
import math
import hka
from ftplib import FTP
from PIL import Image

from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar

# configuration
dbimport = False    #True: imgs from ftp server, False: imgs from local folder
pca_amount = 20
snippet_w = 512
scale_fft = False
add_all_fft = True
nr_pixels = 10000


if dbimport:
    setupDB()
    ROOTDIR = FTP.pwd()
    DIRS = FTP.nlst()
else:
    pwd = os.getcwd()
    ROOTDIR = pwd + '/images/idcards_all' #id #idcards_all
    DIRS = os.listdir(ROOTDIR)

#correctPositiveTrain = [0 for i in xrange(len(dirs))]  statt 5
correctPositiveTrain = [0 for i in xrange(len(DIRS))]
correctNegativeTrain = [0 for i in xrange(len(DIRS))]
falsePositiveTrain = [0 for i in xrange(len(DIRS))]
falseNegativeTrain = [0 for i in xrange(len(DIRS))]
correctPositiveTest = [0 for i in xrange(len(DIRS))]
correctNegativeTest = [0 for i in xrange(len(DIRS))]
falsePositiveTest = [0 for i in xrange(len(DIRS))]
falseNegativeTest = [0 for i in xrange(len(DIRS))]
# length of features for each printer
train_feature_length = [0 for i in xrange(len(DIRS))]
test_feature_length = [0 for i in xrange(len(DIRS))]

class Inspector(pg.Qt.QtGui.QMainWindow):

    def __init__(self):
        super(Inspector, self).__init__()
        print("Number of Pixels: ", nr_pixels)
        # every observed snippet (512,512) is reduced to a patch of 1024 (32,32)
        col = range(1024)
        col_large = range(snippet_w*snippet_w)
        col.append('name')
        col_large.append('name')
        self.printer_types = np.array(())
        self.snippet_amount_perPrinter = np.array(())

        # (1) imgs with their class
        self.data = pd.DataFrame(columns=col)
        self.data_merged = pd.DataFrame(columns=col_large)
        self.data_merged_multi = pd.DataFrame(columns=col_large)
        self.data_detailed = pd.DataFrame(columns=col_large)
        self.train = pd.DataFrame()
        self.test = pd.DataFrame()
        ## (2) imgs in feature representation
        # self.train_feature = pd.DataFrame()
        # self.test_feature = pd.DataFrame()
        # (3) descriptor: mean and std of classes
        #self.mean = pd.DataFrame(columns=range(2 * len(DIRS)))
        #self.std = pd.DataFrame(columns=range(2 * len(DIRS)))
        self.mean = np.array(())
        self.std = np.array(())
        self.apriori = np.array(())

        # debugging option
        #self.pic = np.zeros(shape=(32,32,7))

        # set UI app
        self.initUI()

    def initUI(self):
        # set other GUI elements
        btn0 = QtGui.QPushButton("loadDB", self)
        btn1 = QtGui.QPushButton("export spectra", self)
        btn2 = QtGui.QPushButton("import spectra", self)

        btn3 = QtGui.QPushButton("Training", self)
        # btn4 = QtGui.QPushButton("export feature", self)
        # btn5 = QtGui.QPushButton("import feature", self)

        # btn6 = QtGui.QPushButton("GNB classification", self)
        #btn7 = QtGui.QPushButton("show PC spectra", self)
        #btn8 = QtGui.QPushButton("show naive Bayes", self)
        btn9 = QtGui.QPushButton("show statistics", self)
        #btn10 = QtGui.QPushButton("show ROC", self)

        btn11 = QtGui.QPushButton("load document", self)
        btn12 = QtGui.QPushButton("inspect", self)

        #self.scra1 = QtGui.QScrollArea(self)
        #self.scra1.move(200, 600)

        #self.lbl1 = QtGui.QLabel('TestLabel', self.scra1)
        self.lbl1 = QtGui.QLabel('', self)
        self.lbl2 = QtGui.QLabel('', self)

        # main layout
        centralWidget = QtGui.QWidget(self)
        self.setCentralWidget( centralWidget )
        layout = QtGui.QGridLayout( centralWidget )

        ##set plot widget
        #self.pl1 = pg.PlotWidget()
        #x = np.random.normal(size=1000)
        #y = np.random.normal(size=1000)
        #self.pl1.plot(x, y, pen=None, symbol='o')

        layout.addWidget(btn0, 0, 0)
        layout.addWidget(btn1, 1, 0)
        layout.addWidget(btn2, 2, 0)
        layout.addWidget(btn3, 3, 0)
        # layout.addWidget(btn4, 4, 0)
        # layout.addWidget(btn5, 5, 0)
        # layout.addWidget(btn6, 6, 0)
        #layout.addWidget(btn7, 7, 0)
        #layout.addWidget(btn8, 8, 0)
        layout.addWidget(btn9, 5, 0)
        #layout.addWidget(btn10, 10, 0)
        layout.addWidget(btn11, 10, 0)
        layout.addWidget(btn12, 11, 0)

        #layout.addWidget(self.pl1, 0, 7, 6,10)
        layout.addWidget(self.lbl2, 0, 7, 6,10)
        layout.addWidget(self.lbl1, 8, 10, 6,10)
        #layout.addWidget(self.scra1, 8, 10, 6,10)

        btn0.clicked.connect(self.loadDB)
        btn1.clicked.connect(self.saveSpectra)
        btn2.clicked.connect(self.getSpectra)
        btn3.clicked.connect(self.PCA)
        # btn4.clicked.connect(self.exportFeature)
        # btn5.clicked.connect(self.importFeature)
        # btn6.clicked.connect(self.classGNB)
        #btn7.clicked.connect(self.showPC)
        #btn8.clicked.connect(self.showBayes)
        btn9.clicked.connect(self.showStat)
        #btn10.clicked.connect(self.showROC)
        btn11.clicked.connect(self.loadimg)
        btn12.clicked.connect(self.inspect)

        centralWidget.setLayout(layout)

        self.setGeometry(1200, 750, 1150, 700)
        self.setWindowTitle('Inspector')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def saveSpectra(self):

        if add_all_fft:
            if self.data_merged.empty==False:
                self.data_merged.to_pickle("data_merged.pkl")
                self.data_merged_multi.to_pickle("data_merged_multi.pkl")
                self.data_detailed.to_pickle("data_detailed.pkl")
                print("saved merged spectra!")
            else:
                print("Data is still empty, press loadDB first.")
        else:
            if self.data.empty==False:
                self.data.to_pickle("spectra.pkl")
                print("saved spectra!")
            else:
                print("Data is still empty, press loadDB first.")

    def getSpectra(self):

        if add_all_fft:
            self.data_merged = pd.read_pickle("data_merged.pkl")
            self.data_merged_multi = pd.read_pickle("data_merged_multi.pkl")
            self.data_detailed = pd.read_pickle("data_detailed.pkl")
            class_column = self.data_detailed.shape[1]-1
            self.printer_types = np.unique([printer for printer in self.data_detailed.ix[:,class_column]])
            self.snippet_amount_perPrinter = np.zeros((len(self.printer_types)))
            for i in range(self.printer_types.shape[0]):
                self.snippet_amount_perPrinter[i] = self.data_detailed[self.data_detailed.ix[:,class_column]==self.printer_types[i]].shape[0]

            if self.data_merged.empty:
                print("No merged spectra on memory.")
            else:
                print("got spectra!")

        else:
            self.data = pd.read_pickle("spectra.pkl")
            self.printer_types = np.unique([printer for printer in self.data.ix[:,1024]])
            self.snippet_amount_perPrinter = np.zeros((len(self.printer_types)))
            if self.data.empty:
                print("No Spectra on memory.")
            else:
                print("got spectra!")

        self.mean = np.zeros((len(self.printer_types),pca_amount,2))
        self.std = np.zeros((len(self.printer_types),pca_amount,2))
        self.apriori = np.zeros((len(self.printer_types),2))


    def loadDB(self):
        a=0
        self.printer_types = np.array(())
        for printer in DIRS:
            if printer == '.DS_Store':
                pass
            else:
                self.printer_types = np.append(self.printer_types, printer)

        self.snippet_amount_perPrinter = np.zeros((len(self.printer_types)))

        self.mean = np.zeros((len(self.printer_types),pca_amount,2))
        self.std = np.zeros((len(self.printer_types),pca_amount,2))
        self.apriori = np.zeros((len(self.printer_types),2))

        for curr in self.printer_types:
            if os.path.isdir(ROOTDIR + '/' + curr):
                print(curr)
                imgs = os.listdir(ROOTDIR + '/' + curr)
                printer_number = np.where(self.printer_types==curr)[0][0]
                #if len(imgs) >= 70:
                magnitude_all = np.zeros((snippet_w,snippet_w))
                magnitude_all_multi = np.ones((snippet_w,snippet_w))

                for img in imgs:
                    if img == '.DS_Store':
                        print('DS_Store files has not been removed.')
                    else:
                        # read image
                        print("img path: " + ROOTDIR + '/' + curr + '/' + img)
                        #/Users/resa/Studium Master/2. Semester - WiSe2014/Projekt/ipython/printers/canon/005_Canon_L02.tif
                        #tmp = skimage.io.imread(rootdir + '/' + curr + '/' + img, plugin='tifffile')
                        tmp = skimage.io.imread(ROOTDIR + '/' + curr + '/' + img)
                        # use only piece of image
                        if(tmp.shape[0]<=1536 and tmp.shape[1]<=1536 ):
                            tmp = tmp[0:1535,0:1535]
                        # convert to grey valued image
                        if(len(tmp.shape) == 3):
                            #tmp = skimage.io.MultiImage(rootdir + '/' + curr + '/' + img)
                            tmpGrey = tmp[:,:,0]*0.0722 + tmp[:,:,1]*0.7152 + tmp[:,:,2]*0.2126
                            #tmpGrey = cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY)#include opencv as cv2
                        else:
                            continue

                        # number of pixels per segents
                        nperseg=[snippet_w,snippet_w]#[512,512]

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
                        segment_count[0] = (tmpGrey.shape[0]-noverlap[0])//step[0]
                        segment_count[1] = (tmpGrey.shape[1]-noverlap[1])//step[1]

                        # for(each segment in img): cut of segment
                        for i in range(0, segment_count[0]):
                            for j in range(0, segment_count[1]):
                                # segment as copy of img snippet
                                start_i = i*nperseg[0]
                                start_j = j*nperseg[1]
                                segment = tmpGrey[start_i:(start_i+nperseg[0]),start_j:(start_j+nperseg[1])]
                                # cut relevant data out of scanned image
                                #tmpGreySegment = tmpGrey[:,range(96,160,2)]
                                #tmpGreySegment = tmpGreySegment[range(80,176,3),:]
                                #tmpGreySegment = tmpGreySegment.reshape(1024)
                                #tmpGreySegment = tmpGreySegment.tolist() + [curr]

                                # windowing function on segment
                                # build 1d window
                                segment_hanning = copy.copy(segment)

                                # hanning vectors
                                u_vector = np.hanning(segment.shape[0])#eine Zeile
                                v_vector = np.hanning(segment.shape[1])#eine Spalte

                                # 2d hanning matrix
                                for u in range(0,segment.shape[0]-1):
                                    for v in range(0,segment.shape[1]-1):
                                        segment_hanning[u][v] = np.multiply(u_vector[u], v_vector[v])*255

                                segment_windowed = copy.copy(segment)

                                #img.astype(float64)
                                #np.int8(z)

                                ## multiply hanning window to image
                                for u in range(0,segment.shape[0]-1):
                                    #img_hanning[u] = np.multiply(u_vector[u], v_vector)
                                    t_max = np.float64(0)
                                    for v in range(0,segment.shape[1]-1):
                                        t = np.float64(segment_hanning[u][v])/255
                                        segment_windowed[u][v] = t * np.float64(segment[u][v]) + (1-t) * 255
                                        #segment_windowed[u][v] = np.multiply(np.float64(img[u][v]), img_hanning[u][v])/255
                                        if t>t_max:
                                            t_max=np.float64(t)

                                # compute fft for every segment in an image
                                f = np.fft.fft2(segment_windowed)
                                fshift = np.fft.fftshift(f)
                                magnitude_spectrum = 20*np.log(np.abs(fshift))


                                if add_all_fft:
                                    # darken region around axis
                                    middle = int(magnitude_spectrum.shape[0]/2)
                                    magnitude_spectrum[middle-5:middle+5,:] = magnitude_spectrum.min()
                                    magnitude_spectrum[:,middle-5:middle+5] = magnitude_spectrum.min()

                                    # norm: max = 1 (for one segment)
                                    #mag_normed = np.divide(magnitude_spectrum,magnitude_spectrum.max())
                                    #mag_shift = mag_normed - mag_normed.mean()
                                    #mag_shift = np.divide(mag_shift, (mag_shift.max() - mag_shift.min()))
                                    mag_shift = np.divide(magnitude_spectrum, segment_count[0]*segment_count[1]*len(imgs))

                                    # add and multiply cumulative
                                    magnitude_all += mag_shift
                                    magnitude_all_multi *= mag_shift
                                    # add segment fft to data_detailed
                                    self.data_detailed.loc[a] = magnitude_spectrum.reshape(magnitude_spectrum.size).tolist() + [curr]
                                else:
                                    # add class to list
                                    # save spectrum in data (magnitude_spectrum or fshift ?)
                                    #range(241,272,1)
                                    if not scale_fft:
                                        magnitude_cut = magnitude_spectrum[:,range(96,160,1)] #192,320,4 for snippet-size 512,512
                                        #64,192,4 for snippet-size: 256,256
                                        magnitude_cut = magnitude_cut[range(96,160,1),:] #192,320,4 for snippet-size 512,512
                                        #64,192,4 for snippet-size: 256,256
                                    else:
                                        magnitude_cut = magnitude_spectrum[:,range(96,160,1)]
                                        magnitude_cut = magnitude_cut[range(96,160,1),:]
                                        magnitude_cut = magnitude_cut.reshape(1024)

                                    magnitude_list = magnitude_cut.tolist() + [curr]
                                    self.data.loc[a] = magnitude_list
                                a=a+1

                if add_all_fft:
                    # add class and add one per printer to pandas dataframes
                    # norm additive + multiplied spectras
                    #magnitude_all = np.divide(magnitude_all, magnitude_all.max())
                    #magnitude_all = magnitude_all - magnitude_all.mean()
                    #magnitude_all = np.divide(magnitude_all, (magnitude_all.max()-magnitude_all.min()))
                    idx = np.argsort(magnitude_all.flatten())
                    b = magnitude_all.flatten()[idx]

                    threshold = b[b.size - nr_pixels]

                    min = magnitude_all.min()

                    magnitude_all[magnitude_all<threshold] = min
                    magnitude_all_multi[magnitude_all_multi<threshold] = min

                    magnitude_all = magnitude_all - magnitude_all.min()
                    magnitude_all = magnitude_all/magnitude_all.sum()

                    self.data_merged.loc[printer_number] = magnitude_all.reshape(magnitude_all.size).tolist() + [curr]
                    self.data_merged_multi.loc[printer_number] = magnitude_all_multi.reshape(magnitude_all_multi.size).tolist() + [curr]

                    #save image: merged frequency spectrum by addition
                    f_add = Image.fromarray(np.divide(magnitude_all,magnitude_all.max())*255).convert('RGB')

                    #save image: merged frequency spectrum by addition

                    #use a threshold (only for visualization)
                    self.snippet_amount_perPrinter[printer_number] = segment_count[0]*segment_count[1]*len(imgs)
                    mean = np.divide(magnitude_all_multi.mean(),self.snippet_amount_perPrinter[printer_number])

                    temp = magnitude_all_multi.copy()
                    temp[magnitude_all_multi>mean] = 255
                    temp[magnitude_all_multi<=mean] = 0
                    f_multi = Image.fromarray(temp).convert('RGB')
                    f_add.save(curr+"_merged_add.png","PNG")
                    f_multi.save(curr+"_merged_multi.png","PNG")

        print("load and prepare data finished!")
        self.statusBar().showMessage('images are loaded.')


    def PCA(self):
        if add_all_fft:
            data_normed = np.zeros((self.printer_types.size, snippet_w,snippet_w))
            class_column = self.data_detailed.shape[1]-1
            sum = np.zeros((self.printer_types.size))

            for p in range(self.printer_types.size):
                #vector = np.array(np.divide(self.data_merged.ix[p,:-1],self.snippet_amount_perPrinter[p]))
                vector = np.array(self.data_merged.ix[p,:-1])
                data_normed[p,:,:] = np.reshape(vector, (snippet_w,snippet_w))
                sum[p] = np.sum(np.sum(data_normed[p]))
                #data_normed[p,:,:] = np.divide(data_normed[p,:,:],sum[p])

            nr_segments = self.data_detailed.shape[0]
            correlation_list = np.zeros((nr_segments, self.printer_types.size+1))

            printers_nr = np.arange(self.printer_types.size)

            for i in range(self.data_detailed.shape[0]):
                p_id = self.data_detailed.ix[i,class_column]
                printer_number = np.where(self.printer_types==p_id)[0][0]

                # prove similarity - correlation of segment ffts with additive spcectras
                for p in range(len(self.printer_types)):

                    correlation_list[i,p] = np.dot(self.data_detailed.ix[i,:class_column], data_normed[p,:,:].reshape(class_column))

                    correlation_list[i,p+1] = printer_number


            for p in range(len(self.printer_types)):

                printer_list = correlation_list[correlation_list[:,-1] == p]

                for row in range(printer_list.shape[0]):
                    printer_list[row,:].max()
                    likeliest_class = np.where(printer_list[row,:]==printer_list[row,:].max())[0][0]

                    if likeliest_class == p:
                        print(p, ": TRUE classification.")
                        correctPositiveTrain[p] += 1

                        li = np.delete(printers_nr,p)
                        for l in li:
                            correctNegativeTrain[l] += 1
                    else:
                        # falseClassification:
                        falseNegativeTrain[p] += 1                  # printer p was not identified
                        falsePositiveTrain[likeliest_class] += 1    # printer likeliest_class was wrongly detected
                        li = np.delete(printers_nr,p)
                        li = np.delete(li,likeliest_class-1)
                        for l in li:
                            correctNegativeTrain[l] += 1

                        print(p, ": False.")




        else:
            self.train = pd.DataFrame()
            self.test = pd.DataFrame()

            #randomly reorder data
            data_rand = self.data.reindex(np.random.permutation(self.data.index))
            data_rand.index = range(0,len(data_rand))


            # chose same amount of data from each class
            for printer in self.printer_types:
                printer_data = data_rand[data_rand['name']==printer].copy()
                printer_data.index = range(0,len(printer_data))
                splitpoint = int(round(printer_data.shape[0]*0.6))

                self.train = self.train.append(printer_data.ix[0:splitpoint,:])
                self.train.index = range(0,len(self.train))
                self.test = self.test.append(printer_data.ix[splitpoint+1:,:])
                self.test.index = range(0,len(self.test))

            #PCA
            self.axis, self.eigenData, s = hka.hka(self.train.transpose().ix[:1024,:])

            # export hka
            name_eigen = "eigenData.pkl"
            pd.DataFrame(self.eigenData).to_pickle(name_eigen)

            print("pca finished!")
            #Eigen-Spektren
            # for i in range(7):
            #     self.pic = self.eigenData[:,i].reshape(32,32)
                #plt.figure()
                #plt.imshow(pic, cmap=plt.cm.gray)
            #plt.show()

            #split up into train and test set
            z = 0
            for printer in self.printer_types:
                print("Start learning ", printer)
                printer_number = np.where(self.printer_types==printer)[0][0]
                #Feature Extraction
                train_feature = pd.DataFrame()
                for j in range(len(self.train)):
                    feature = np.zeros(pca_amount+1)
                    if self.train['name'].ix[j] == printer:
                        feature[pca_amount] = 1
                    else:
                        feature[pca_amount] = -1

                    for i in range(pca_amount):
                        feature[i] = self.eigenData[:,i].T*np.matrix(self.train.ix[j,:1024]).T
                    train_feature[j] = feature

                test_feature = pd.DataFrame()
                for j in range(len(self.test)):
                    feature = np.zeros(pca_amount+1)
                    if self.test['name'].ix[j] == printer:
                        feature[pca_amount] = 1
                    else:
                        feature[pca_amount] = -1

                    for i in range(pca_amount):
                        feature[i] = self.eigenData[:,i].T*np.matrix(self.test.ix[j,:1024]).T
                    test_feature[j] = feature

                train_feature = train_feature.transpose()
                test_feature = test_feature.transpose()

                train_feature.rename(columns={pca_amount: 'label'}, inplace=True)
                test_feature.rename(columns={pca_amount: 'label'}, inplace=True)

                #Gaussian Naive Bayes - Training
                mean = pd.DataFrame()
                mean[0] = np.matrix(train_feature[train_feature['label']==1].mean()[0:pca_amount]).tolist()[0]
                mean[1] = np.matrix(train_feature[train_feature['label']==-1].mean()[0:pca_amount]).tolist()[0]

                std = pd.DataFrame()
                std[0] = np.matrix(train_feature[train_feature['label']==1].std()[0:pca_amount]).tolist()[0]
                std[1] = np.matrix(train_feature[train_feature['label']==-1].std()[0:pca_amount]).tolist()[0]

                apriori = np.array([len(train_feature[train_feature['label']==1])/float(len(train_feature)),len(train_feature[train_feature['label']==-1])/float(len(train_feature))])

                self.mean[printer_number,:,:] = mean
                self.std[printer_number,:,:] = std
                self.apriori[printer_number,:] = apriori

                # export gaussian naive bayes
                name_mean = printer +"_mean.pkl"
                mean.to_pickle(name_mean)
                name_std = printer +"_std.pkl"
                std.to_pickle(name_std)
                name_apriori = printer +"_apriori.pkl"
                a = pd.DataFrame(apriori)
                a.to_pickle(name_apriori)

                # Train Set
                [correctPositiveTrain[z], correctNegativeTrain[z], falsePositiveTrain[z], falseNegativeTrain[z], tmp, tmp] = GNBMatch(train_feature, mean, std, apriori, 1)
                train_feature_length[z] = len(train_feature)
                # Test Set
                [correctPositiveTest[z], correctNegativeTest[z], falsePositiveTest[z], falseNegativeTest[z], tmp, tmp] = GNBMatch(test_feature, mean, std, apriori, 1)
                test_feature_length[z] = len(test_feature)
                print("GNB training finished.")
                z = z+1

        print("Training for all printers finished.")


    def showStat(self):
        newstr = []
        if add_all_fft:
            for i in range(0, len(self.printer_types)):
                #print("TRAIN SET")
                print(self.printer_types[i], "############################")
                print("Hit Rate: %d %s" % (100*correctPositiveTrain[i] / (correctPositiveTrain[i] + falseNegativeTrain[i]), "%"))
                print("Miss Rate: %d %s" % (100*falseNegativeTrain[i] / (correctNegativeTrain[i] + falseNegativeTrain[i]), "%"))
                print("Fallout: %d %s" % (100*falsePositiveTrain[i] / (falsePositiveTrain[i] + correctNegativeTrain[i]), "%"))
                print("-------------------------------")
                print("Accuracy: %d %s" % (100*(correctPositiveTrain[i]+correctNegativeTrain[i]) / (correctPositiveTrain[i] + correctNegativeTrain[i] + falsePositiveTrain[i] + falseNegativeTrain[i]), "%"))
                print("Classification Failure: %d %s" % (100*(falsePositiveTrain[i] + falseNegativeTrain[i]) / (correctPositiveTrain[i] + correctNegativeTrain[i] + falsePositiveTrain[i] + falseNegativeTrain[i]), "%"))


                #line6 = "TEST SET"
                #line7 = self.printer_types[i]
                #line111 = "Hit Rate: %d %s" % (100*correctPositiveTest[i] / (correctPositiveTest[i] + falseNegativeTest[i]), "%")
                #line112 = "Accuracy: %d %s" % (100*correctPositiveTest[i] / (correctPositiveTest[i] + falsePositiveTest[i]), "%")
                #line113 = "Fallout: %d %s" % (100*falsePositiveTest[i] / (falsePositiveTest[i] + correctNegativeTest[i]), "%")
                #newstr.append("\n".join(("                                                            ".join((line0)),"                                                            ".join((line1)),"          ".join((line2)),"         ".join((line3)),"                    ".join((line4)),"                    ".join((line5)),"                                                        ".join((line6)),"                                                        ".join((line7)))))

        else:
            for i in range(0, len(self.printer_types)):
                line0 = "TRAIN SET"
                line1 = self.printer_types[i]
                line2 = "%d documents - %d %s" % (correctPositiveTrain[i], 100*correctPositiveTrain[i]/train_feature_length[i], '% correctPositive classifications')
                line3 = "%d documents - %d %s" % (correctNegativeTrain[i], 100*correctNegativeTrain[i]/train_feature_length[i], '% correctNegative classifications')
                line4 = "%d documents - %d %s" % (falsePositiveTrain[i], 100*falsePositiveTrain[i]/train_feature_length[i], '% falsePositive classifications')
                line5 = "%d documents - %d %s" % (falseNegativeTrain[i], 100*falseNegativeTrain[i]/train_feature_length[i], '% falseNegative classifications')

                line51 = "Hit Ratio: %d %s" % (100*correctPositiveTrain[i] / (correctPositiveTrain[i] + falseNegativeTrain[i]), "%")
                line52 = "Accuracy: %d %s" % (100*correctPositiveTrain[i] / (correctPositiveTrain[i] + falsePositiveTrain[i]), "%")
                line53 = "Fallout: %d %s" % (100*falsePositiveTrain[i] / (falsePositiveTrain[i] + correctNegativeTrain[i]), "%")

                line6 = "TEST SET"
                line7 = self.printer_types[i]
                line8 = "%d documents - %d %s" % (correctPositiveTest[i], 100*correctPositiveTest[i]/test_feature_length[i], '% correctPositive classifications')
                line9 = "%d documents - %d %s" % (correctNegativeTest[i], 100*correctNegativeTest[i]/test_feature_length[i], '% correctNegative classifications')
                line10 = "%d documents - %d %s" % (falsePositiveTest[i], 100*falsePositiveTest[i]/test_feature_length[i], '% falsePositive classifications')
                line11 = "%d documents - %d %s" % (falseNegativeTest[i], 100*falseNegativeTest[i]/test_feature_length[i], '% falseNegative classifications')

                line111 = "Hit Ratio: %d %s" % (100*correctPositiveTest[i] / (correctPositiveTest[i] + falseNegativeTest[i]), "%")
                line112 = "Accuracy: %d %s" % (100*correctPositiveTest[i] / (correctPositiveTest[i] + falsePositiveTest[i]), "%")
                line113 = "Fallout: %d %s" % (100*falsePositiveTest[i] / (falsePositiveTest[i] + correctNegativeTest[i]), "%")
                newstr.append("\n".join(("                                                            ".join((line0,line6)),"                                                            ".join((line1,line7)),"          ".join((line2,line8)),"         ".join((line3,line9)),"                    ".join((line4,line10)),"                    ".join((line5,line11)),"                                                        ".join((line51,line111)),"                                                        ".join((line52,line112)),"                                                        ".join((line53,line113)))))

        self.lbl1.setText("\n".join((newstr)))


    def loadimg(self):
        qimg = QtGui.QImage()
        col = range(1024)
        col.append('name')
        questioned = pd.DataFrame(columns=col)
        filename = QtGui.QFileDialog.getOpenFileName(
                   self, 'Open File', '', 'Images (*.png *.xpm *.jpg)')
        qimg.load(filename)
        print("image is loaded.")

        #pixmap = QtGui.QPixmap.fromImage(qimg) # show loaded image in screen (too large)
        #self.lbl2.setPixmap(pixmap) # show loaded image in screen (too large)

        tmp = skimage.io.imread(str(filename))

        if tmp.size == 0:
            print("Image could not be load: ")
            print(filename)
            #return False

        if(len(tmp.shape) == 3):
            tmpGrey = tmp[:,:,0]*0.0722 + tmp[:,:,1]*0.7152 + tmp[:,:,2]*0.2126
        # compute FFT spectra for serveral segments
        a=0
        # number of pixels per segents
        nperseg=[512,512]

        # number of pixels which overlap
        noverlap = np.empty([2], dtype=int)
        noverlap[0] = nperseg[0] // 2
        noverlap[1] = nperseg[1] // 2
        # number of pixels to move each segment
        step = np.empty([len(tmpGrey.shape)], dtype=int)
        step[0] = nperseg[0] - noverlap[0]
        step[1] = nperseg[1] - noverlap[1]

        # number of segments in one scanned image (in both dimensions)
        segment_count = np.empty([len(tmpGrey.shape)], dtype=int)
        segment_count[0] = (tmpGrey.shape[0]-noverlap[0])//step[0]
        segment_count[1] = (tmpGrey.shape[1]-noverlap[1])//step[1]

        # for(each segment in img): cut of segment
        for i in range(0, segment_count[0]-1):
            for j in range(0, segment_count[1]-1):
                # segment as copy of img snippet
                segment = tmpGrey[i:(i+nperseg[0]),j:(j+nperseg[1])]
                # cut relevant data out of scanned image
                #tmpGreySegment = tmpGrey[:,range(96,160,2)]
                #tmpGreySegment = tmpGreySegment[range(80,176,3),:]
                #tmpGreySegment = tmpGreySegment.reshape(1024)
                #tmpGreySegment = tmpGreySegment.tolist() + [curr]
                # windowing function on segment
                # build 1d window
                segment_hanning = copy.copy(segment)

                # hanning vectors
                u_vector = np.hanning(segment.shape[0])#eine Zeile
                v_vector = np.hanning(segment.shape[1])#eine Spalte

                # 2d hanning matrix
                for u in range(0,segment.shape[0]-1):
                    for v in range(0,segment.shape[1]-1):
                        segment_hanning[u][v] = np.multiply(u_vector[u], v_vector[v])*255

                segment_windowed = copy.copy(segment)

                #img.astype(float64)
                #np.int8(z)
                threshold = 200
                # then break (but for later average computation remove 1 from valid_segments or something)
                average_brightness = 0
                ## multiply hanning window to image
                for u in range(0,segment.shape[0]-1):
                    #img_hanning[u] = np.multiply(u_vector[u], v_vector)
                    t_max = np.float64(0)
                    for v in range(0,segment.shape[1]-1):
                        average_brightness += np.float64(segment[u][v])
                        t = np.float64(segment_hanning[u][v])/255
                        segment_windowed[u][v] = t * np.float64(segment[u][v]) + (1-t) * 255
                        #segment_windowed[u][v] = np.multiply(np.float64(img[u][v]), img_hanning[u][v])/255
                        if t>t_max:
                            t_max=np.float64(t)
                average_brightness *= 1/segment.size
                if average_brightness >= threshold:
                    print("over threshold")
                else:
                    # compute fft for every segment in an image
                    f = np.fft.fft2(segment_windowed)
                    fshift = np.fft.fftshift(f)
                    magnitude_spectrum = 20*np.log(np.abs(fshift))

                    # save spectrum in data (magnitude_spectrum or fshift ?)
                    #range(241,272,1)
                    magnitude_cut = magnitude_spectrum[:,range(192,320,4)]
                    magnitude_cut = magnitude_cut[range(192,320,4),:]
                    magnitude_cut = magnitude_cut.reshape(1024)
                    magnitude_cut = magnitude_cut.tolist() + ["Q"]
                    questioned.loc[a] = magnitude_cut
                    a=a+1

        # feature extraction (PCA + GNB)
        questioned.index = range(0,len(questioned))

        questioned_feature = pd.DataFrame()
        for j in range(len(questioned)):
            feature = np.zeros(pca_amount+1)
            feature[pca_amount] = 0

            for i in range(pca_amount):
                feature[i] = self.eigenData[:,i].T*np.matrix(questioned.ix[j,:1024]).T
            questioned_feature[j] = feature

        questioned_feature = questioned_feature.transpose()
        questioned_feature.rename(columns={pca_amount: 'label'}, inplace=True)
        # export features
        name_test = "QuestionedFeature.pkl"
        questioned_feature.to_pickle(name_test)

        print("Feature extraction of questioned document finished.")
        #self.lbl2.show() # show loaded image in screen (too large)


    def inspect(self):
        z=0
        newstr = []
        for printer in self.printer_types:
            print(printer)
            printer_number = np.where(self.printer_types==printer)[0][0]
            # read features
            col = range(1024)
            col.append('name')
            questioned_feature = pd.DataFrame(columns=col)

            name_test = "QuestionedFeature.pkl"
            questioned_feature = pd.read_pickle(name_test)


            mean = pd.DataFrame(self.mean[printer_number,:,:], columns=[0,1])
            std = pd.DataFrame(self.std[printer_number,:,:], columns=[0,1])
            apriori = self.apriori[printer_number,:]

            name_test = "QuestionedFeature.pkl"
            questioned_feature = pd.read_pickle(name_test)

            # import gaussian naive bayes
            mean = pd.read_pickle(printer +"_mean.pkl")
            std = pd.read_pickle(printer +"_std.pkl")
            apriori = np.array(pd.read_pickle(printer +"_apriori.pkl")).T.flatten()

            ## Train Set
            #[correctPositiveTrain[z], correctNegativeTrain[z], falsePositiveTrain[z], falseNegativeTrain[z], tmp, tmp] = GNBMatch(train_feature, self.mean.ix[:,2*z:2*z+1], self.std.ix[:,2*z:2*z+1], apriori, 1)
            #train_feature_length[z] = len(train_feature)
            # Test Set
            [correctPositiveQ, correctNegativeQ, falsePositiveQ, falseNegativeQ, tmp, tmp] = GNBMatch(questioned_feature, mean, std, apriori, 1)

            if(falsePositiveQ+correctPositiveQ >= correctNegativeQ+falseNegativeQ):
                newstr1 = "POSITIVE: "
                quote_pos = "%d %s" % (100*(falsePositiveQ+correctPositiveQ)/len(questioned_feature), '% agreement ------')
                newstr.append("  ".join((newstr1, printer, quote_pos)))
            else:
                newstr2 = "Negative: "
                quote_neg = "%d %s" % (100*(falsePositiveQ+correctPositiveQ)/len(questioned_feature), '% agreement')
                newstr.append("  ".join((newstr2, printer, quote_neg)))
            # Zugehörigkeit:       Espon (zu 99%)
            # Nicht-Zugehörigkeit: Canon (zu 94%), HP(zu 100%), Brother (zu 99%)
            #z = z+1
            # if(falsePositiveQ >= falseNegativeTest[z]):
            #     newstr = "Positive: "
            #     quote_pos = "%d %s" % (100*falsePositiveTest[i]/len(questioned_feature), '%')
            #     newstr.append("  ".join((printer, quote_pos)))
            # else:
            #     newstr = "Negative: "
            #     quote_neg = "%d %s" % (100*falseNegativeTest[i]/len(questioned_feature), '%')
            #     newstr.append("  ".join((printer, quote_neg)))
            ## Zugehörigkeit:       Espon (zu 99%)
            ## Nicht-Zugehörigkeit: Canon (zu 94%), HP(zu 100%), Brother (zu 99%)
            self.lbl1.setText("\n".join((newstr)))
            print("GNB training finished.")
            z = z+1

def GNB(x, mean, std):
    return 1/math.sqrt(2*math.pi*std)*math.exp(-1/2.0*(x-mean)**2 / std**2)

def GNBMatch(matchData, mean, std, apriori, c):
    correctPositive = 0
    correctNegative = 0
    falsePositive = 0
    falseNegative = 0
    gMin = 10
    gMax = 0

    for k in range(0,len(matchData)):
        w1Prob = 1
        w2Prob = 1
        for j in range(pca_amount):
            w1Prob = w1Prob * GNB(matchData.ix[k,j], mean.ix[j,0], std.ix[j,0])
            w2Prob = w2Prob * GNB(matchData.ix[k,j], mean.ix[j,1], std.ix[j,1])

        g = (apriori[0]*w1Prob)/(apriori[1]*w2Prob)
        if g<gMin:
            gMin = g
        if g>gMax:
            gMax = g
        
        g=g*c-1
        
        if g>0:
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

def setupDB(self):
        self.ftp = FTP('141.37.176.19')
        self.ftp.login('dmm', 'dmm$ios')
        self.ftp.cwd('printer')

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Inspector()
    # subplot = ex.getFigure().add_subplot(111)
    # subplot.plot(1,1)
    # ex.draw()
    sys.exit(app.exec_())
    self.ftp.quit()


if __name__ == '__main__':
    main()