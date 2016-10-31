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

from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar

dbimport = False    #True: imgs from ftp server, False: imgs from local folder

if dbimport:
    setupDB()
    ROOTDIR = FTP.pwd()
    DIRS = FTP.nlst()
else:
    pwd = os.getcwd()
    ROOTDIR = pwd + '/images/id'
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
        # every observed snippet (512,512) is reduced to a patch of 1024 (32,32)
        col = range(1024)
        col.append('name')
        self.printer_types = np.array(())

        # (1) imgs with their class
        self.data = pd.DataFrame(columns=col)
        self.train = pd.DataFrame()
        self.test = pd.DataFrame()
        ## (2) imgs in feature representation
        # self.train_feature = pd.DataFrame()
        # self.test_feature = pd.DataFrame()
        # (3) descriptor: mean and std of classes
        self.mean = pd.DataFrame(columns=range(2 * len(DIRS)))
        self.std = pd.DataFrame(columns=range(2 * len(DIRS)))

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
        if self.data.empty==False:
            self.data.to_pickle("spectra.pkl")
            print("saved spectra!")
        else:
            print("Data is still empty, press loadDB first.")

    def getSpectra(self):
        self.data = pd.read_pickle("spectra.pkl")
        self.printer_types = np.unique([printer for printer in self.data.ix[:,1024]])
        if self.data.empty:
            print("No Spectra on memory.")
        else:
            print("got spectra!")

    def loadDB(self):
        a=0
        self.printer_types = np.array(())
        for printer in DIRS:
            if printer == '.DS_Store':
                pass
            else:
                self.printer_types = np.append(self.printer_types, printer)

        for curr in self.printer_types:
            if os.path.isdir(ROOTDIR + '/' + curr):
                print(curr)
                imgs = os.listdir(ROOTDIR + '/' + curr)
                #if len(imgs) >= 70:
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
                        nperseg=[512,512]

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
                                segment = tmpGrey[start_i:(start_i+nperseg[0]+1),start_j:(start_j+nperseg[1]+1)]
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

                                # save spectrum in data (magnitude_spectrum or fshift ?)
                                #range(241,272,1)
                                magnitude_cut = magnitude_spectrum[:,range(192,320,4)]#64,192,4 for snippet-size: 256,256
                                magnitude_cut = magnitude_cut[range(192,320,4),:]#64,192,4 for snippet-size: 256,256
                                magnitude_cut = magnitude_cut.reshape(1024)
                                magnitude_cut = magnitude_cut.tolist() + [curr]
                                self.data.loc[a] = magnitude_cut
                                a=a+1
        print("load and prepare data finished!")
        self.statusBar().showMessage('images are loaded.')


    def PCA(self):

        self.train = pd.DataFrame()
        self.test = pd.DataFrame()

        #randomly reorder data
        data_rand = self.data.reindex(np.random.permutation(self.data.index))
        data_rand.index = range(0,len(data_rand))

        #splitpoint = int(round(data_rand.shape[0]*0.6))
        #self.train = data_rand.ix[0:splitpoint,:]
        #test = data_rand.ix[splitpoint+1:,:]
        #test.index = range(0,len(test))


        # chose same amount of data from each class
        for printer in self.printer_types:
            printer_data = data_rand[data_rand['name']==printer].copy()
            printer_data.index = range(0,len(printer_data))
            splitpoint = int(round(printer_data.shape[0]*0.6))

            self.train = self.train.append(printer_data.ix[0:splitpoint,:])
            self.train.index = range(0,len(self.train))
            self.test = self.test.append(printer_data.ix[splitpoint+1:,:])
            self.test.index = range(0,len(self.test))

        #split up into train and test set
        z = 0
        for printer in self.printer_types:
            print(printer)
            nrCanonTrain = len(self.train[self.train['name']==printer])
            nrOtherTrain = len(self.train) - nrCanonTrain

            nrCanonTest = len(self.test[self.test['name']==printer])
            nrOtherTest = len(self.test) - nrCanonTest
            
            #PCA
            axis, eigenData, s = hka.hka(self.train.transpose().ix[:1024,:])
            print("pca finished!")
            #Eigen-Spektren
            # for i in range(7):
            #     self.pic = eigenData[:,i].reshape(32,32)
                #plt.figure()
                #plt.imshow(pic, cmap=plt.cm.gray)
            #plt.show()
            
            #Feature Extraction
            train_feature = pd.DataFrame()
            for j in range(len(self.train)):
                feature = np.zeros(8)
                if self.train['name'].ix[j] == printer:
                    feature[7] = 1
                else:
                    feature[7] = -1

                for i in range(7):
                    feature[i] = eigenData[:,i].T*np.matrix(self.train.ix[j,:1024]).T
                train_feature[j] = feature

            test_feature = pd.DataFrame()
            for j in range(len(self.test)):
                feature = np.zeros(8)
                if self.test['name'].ix[j] == printer:
                    feature[7] = 1
                else:
                    feature[7] = -1

                for i in range(7):
                    feature[i] = eigenData[:,i].T*np.matrix(self.test.ix[j,:1024]).T
                test_feature[j] = feature

            train_feature = train_feature.transpose()
            test_feature = test_feature.transpose()

            train_feature.rename(columns={7: 'label'}, inplace=True)
            test_feature.rename(columns={7: 'label'}, inplace=True)

            # export features
            # name_train = printer+"_TrainFeature.pkl"
            # train_feature.to_pickle(name_train)
            # name_test = printer+"_TestFeature.pkl"
            # test_feature.to_pickle(name_test)
            # print "Feature extraction finished."
            # read features
            # name_train = printer+"_TrainFeature.pkl"
            # train_feature = pd.read_pickle(name_train)
            # name_test = printer+"_TestFeature.pkl"
            # test_feature = pd.read_pickle(name_test)
            #Gaussian Naive Bayes - Training
            mean = pd.DataFrame()
            mean[0] = np.matrix(train_feature[train_feature['label']==1].mean()[0:7]).tolist()[0]
            mean[1] = np.matrix(train_feature[train_feature['label']==-1].mean()[0:7]).tolist()[0]

            std = pd.DataFrame()
            std[0] = np.matrix(train_feature[train_feature['label']==1].std()[0:7]).tolist()[0]
            std[1] = np.matrix(train_feature[train_feature['label']==-1].std()[0:7]).tolist()[0]

            apriori = [len(train_feature[train_feature['label']==1])/float(len(train_feature)),len(train_feature[train_feature['label']==-1])/float(len(train_feature))]
            
            # #Plot gaussian probability distribution
            # for i in range(7):
            #     figure()
            #     stdMax = max(std.ix[i,0], std.ix[i,1])
            #     xMin = min(mean.ix[i,0], mean.ix[i,1]) - 3*stdMax
            #     xMax = max(mean.ix[i,0], mean.ix[i,1]) + 3*stdMax
            #     x = np.linspace(xMin,xMax,100)
            #     plt.plot(x,mlab.normpdf(x,mean.ix[i,0],std.ix[i,0]),color='b')
            #     plt.plot(x,mlab.normpdf(x,mean.ix[i,1],std.ix[i,1]),color='r')
                
            # Train Set
            [correctPositiveTrain[z], correctNegativeTrain[z], falsePositiveTrain[z], falseNegativeTrain[z], tmp, tmp] = GNBMatch(train_feature, mean, std, apriori, 1)
            train_feature_length[z] = len(train_feature)
            # Test Set
            [correctPositiveTest[z], correctNegativeTest[z], falsePositiveTest[z], falseNegativeTest[z], tmp, tmp] = GNBMatch(test_feature, mean, std, apriori, 1)
            test_feature_length[z] = len(test_feature) 
            print("GNB training finished.")
            z = z+1

        print("Training for all printers finished.")

    # def showPC(self):
    #     # for i in range(7):
    #     #     img = pg.image(pic[:,:,i])

    #     win = pg.GraphicsWindow(title="PC - Eigen-Spektren")
    #     win.resize(1000,600)
        
    #     for i in range(7):
    #         p1 = win.addPlot()
    #         p1.plot(pg.image(self.pic[:,:,i]))
    #         if i == 3:
    #             win.nextRow()
    # def classGNB(self):
    #     print ""

    # def showBayes(self):
    #     print "Show Bayes"

    def showStat(self):
        newstr = []
        for i in range(0, len(self.printer_types)):
            line0 = "TRAIN SET"
            line1 = self.printer_types[i]
            line2 = "%d documents - %d %s" % (correctPositiveTrain[i], 100*correctPositiveTrain[i]/train_feature_length[i], '% correctPositive classifications')
            line3 = "%d documents - %d %s" % (correctNegativeTrain[i], 100*correctNegativeTrain[i]/train_feature_length[i], '% correctNegative classifications')
            line4 = "%d documents - %d %s" % (falsePositiveTrain[i], 100*falsePositiveTrain[i]/train_feature_length[i], '% falsePositive classifications')
            line5 = "%d documents - %d %s" % (falseNegativeTrain[i], 100*falseNegativeTrain[i]/train_feature_length[i], '% falseNegative classifications')  
            # print self.printer_types[i]
            # print correctPositiveTrain[i], 100*correctPositiveTrain[i]/train_feature_length[i], '% correctPositive classifications'
            # print correctNegativeTrain[i], 100*correctNegativeTrain[i]/train_feature_length[i], '% correctNegative classifications'
            # print falsePositiveTrain[i], 100*falsePositiveTrain[i]/train_feature_length[i], '% falsePositive classifications'
            # print falseNegativeTrain[i], 100*falseNegativeTrain[i]/train_feature_length[i], '% falseNegative classifications'
            line6 = "TEST SET"
            line7 = self.printer_types[i]
            line8 = "%d documents - %d %s" % (correctPositiveTest[i], 100*correctPositiveTest[i]/test_feature_length[i], '% correctPositive classifications')
            line9 = "%d documents - %d %s" % (correctNegativeTest[i], 100*correctNegativeTest[i]/test_feature_length[i], '% correctNegative classifications')
            line10 = "%d documents - %d %s" % (falsePositiveTest[i], 100*falsePositiveTest[i]/test_feature_length[i], '% falsePositive classifications')
            line11 = "%d documents - %d %s" % (falseNegativeTest[i], 100*falseNegativeTest[i]/test_feature_length[i], '% falseNegative classifications')
            
            # print self.printer_types[i]
            # print correctPositiveTest[i], 100*correctPositiveTest[i]/test_feature_length[i], '% correctPositive classifications'
            # print correctNegativeTest[i], 100*correctNegativeTest[i]/test_feature_length[i], '% correctNegative classifications'
            # print falsePositiveTest[i], 100*falsePositiveTest[i]/test_feature_length[i], '% falsePositive classifications'
            # print falseNegativeTest[i], 100*falseNegativeTest[i]/test_feature_length[i], '% falseNegative classifications'
            newstr.append("\n".join(("                                                            ".join((line0,line6)),"                                                            ".join((line1,line7)),"          ".join((line2,line8)),"         ".join((line3,line9)),"                    ".join((line4,line10)),"                    ".join((line5,line11)))))
        
        self.lbl1.setText("\n".join((newstr)))
        #self.scra1.setText("\n".join((newstr)))

    # def showROC(self):
    #     print "Show ROC"

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

        z = 0
        for printer in self.printer_types:
            axis, eigenData, s = hka.hka(self.train.transpose().ix[:1024,:])
            
            #Feature Extraction
            questioned_feature = pd.DataFrame()
            for j in range(len(questioned)):
                feature = np.zeros(8)
                if questioned['name'].ix[j] == printer:
                    feature[7] = 1
                else:
                    feature[7] = -1

                for i in range(7):
                    feature[i] = eigenData[:,i].T*np.matrix(questioned.ix[j,:1024]).T
                questioned_feature[j] = feature

            questioned_feature = questioned_feature.transpose()
            questioned_feature.rename(columns={7: 'label'}, inplace=True)
            # export features
            name_test = printer+"_QuestionedFeature.pkl"
            questioned_feature.to_pickle(name_test)
            z = z+1

        print("Feature extraction of questioned document finished.")
        #self.lbl2.show() # show loaded image in screen (too large)


    def inspect(self):
        z=0
        newstr = []
        for printer in self.printer_types:
            print(printer)
            # read features
            col = range(1024)
            col.append('name') 
            questioned_feature = pd.DataFrame(columns=col)
            
            name_test = printer+"_QuestionedFeature.pkl"
            questioned_feature = pd.read_pickle(name_test)

            axis, eigenData, s = hka.hka(self.train.transpose().ix[:1024,:])
            #Feature Extraction of Train
            train_feature = pd.DataFrame()
            for j in range(len(self.train)):
                feature = np.zeros(8)
                if self.train['name'].ix[j] == printer:
                    feature[7] = 1
                else:
                    feature[7] = -1

                for i in range(7):
                    feature[i] = eigenData[:,i].T*np.matrix(self.train.ix[j,:1024]).T
                train_feature[j] = feature

            train_feature = train_feature.transpose()
            train_feature.rename(columns={7: 'label'}, inplace=True)


            #Gaussian Naive Bayes - Training
            mean = pd.DataFrame()
            mean[0] = np.matrix(train_feature[train_feature['label']==1].mean()[0:7]).tolist()[0]
            mean[1] = np.matrix(train_feature[train_feature['label']==-1].mean()[0:7]).tolist()[0]

            std = pd.DataFrame()
            std[0] = np.matrix(train_feature[train_feature['label']==1].std()[0:7]).tolist()[0]
            std[1] = np.matrix(train_feature[train_feature['label']==-1].std()[0:7]).tolist()[0]

            apriori = [len(train_feature[train_feature['label']==1])/float(len(train_feature)),len(train_feature[train_feature['label']==-1])/float(len(train_feature))]
               
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
            z = z+1
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
        for j in range(7):
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