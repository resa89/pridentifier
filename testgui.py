# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pridentifier2.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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


dbimport = False    #True: imgs from ftp server, False: imgs from local folder
pca_amount = 20
snippet_w = 512
scale_fft = False
add_all_fft = True
nr_pixels = 10000
TRAINING = True # if False: then generating test dataset statistics


if dbimport:
    setupDB()
    ROOTDIR = FTP.pwd()
    DIRS = FTP.nlst()
else:
    pwd = os.getcwd()
    ROOTDIR = pwd + '/../data/images/idcards-testset' #id #idcards_all
    SUBPATH = 'the_same_large'
    DIRS = os.listdir(ROOTDIR)

#correctPositiveTrain = [0 for i in xrange(len(dirs))]  statt 5
correctPositiveTrain = [0 for i in range(len(DIRS))]
correctNegativeTrain = [0 for i in range(len(DIRS))]
falsePositiveTrain = [0 for i in range(len(DIRS))]
falseNegativeTrain = [0 for i in range(len(DIRS))]
correctPositiveTest = [0 for i in range(len(DIRS))]
correctNegativeTest = [0 for i in range(len(DIRS))]
falsePositiveTest = [0 for i in range(len(DIRS))]
falseNegativeTest = [0 for i in range(len(DIRS))]
# length of features for each printer
train_feature_length = [0 for i in range(len(DIRS))]
test_feature_length = [0 for i in range(len(DIRS))]


class Ui_MainWindow(object):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        print("Number of Pixels: ", nr_pixels)
        # every observed snippet (512,512) is reduced to a patch of 1024 (32,32)
        col = [i for i in range(1024)]
        col_large = [i for i in range(snippet_w*snippet_w)]
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
        #self.mean = pd.DataFrame(columns=[i for i in range(2 * len(DIRS))])
        #self.std = pd.DataFrame(columns=[i for i in range(2 * len(DIRS))])
        self.mean = np.array(())
        self.std = np.array(())
        self.apriori = np.array(())


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(937, 630)
        MainWindow.setStyleSheet("background-color: #222222;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 911, 611))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"    border-top: 4px solid #fff;\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border: 0px solid #fff;\n"
"    background-color: #393939;\n"
"    color: #fff;\n"
"    \n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"    color: #000;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: silver;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background: #777777;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("")
        self.tab.setObjectName("tab")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 911, 591))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(15, 30, 15, 15)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.comboBox_6 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_6.setStyleSheet("QComboBox {\n"
"    background-color: #777777;\n"
"    min-width: 160px;\n"
"    padding: 12px 16px;\n"
"    border: 2px solid #fff;\n"
"    color: #fff;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left-width: 0px;\n"
"    border-left-color: none;\n"
"    border-left-style: solid; /* just a single line */\n"
"    margin-right: 10px;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/Users/resa/Projekte/Korensics/arrow.png);\n"
"    height: 100px;\n"
"}")
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.verticalLayout_7.addWidget(self.comboBox_6)
        self.pushButton_21 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_21.setStyleSheet("QPushButton {\n"
"background-color: #009999;\n"
"min-width: 160px;\n"
"padding: 12px 16px;\n"
"border: 2px solid #fff;\n"
"color: #fff;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #75bdc3;\n"
"}")
        self.pushButton_21.setObjectName("pushButton_21")
        self.verticalLayout_7.addWidget(self.pushButton_21)
        self.pushButton_22 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_22.setStyleSheet("QPushButton {\n"
"    display: none;\n"
"    background-color: #393939;\n"
"    min-width: 160px;\n"
"    padding: 12px 16px;\n"
"    border: 2px solid #fff;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #777777;\n"
"}")
        self.pushButton_22.setObjectName("pushButton_22")
        self.verticalLayout_7.addWidget(self.pushButton_22)
        self.pushButton_23 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_23.setStyleSheet("QPushButton{\n"
"    display: none;\n"
"    background-color: #393939;\n"
"    min-width: 160px;\n"
"    padding: 12px 16px;\n"
"    border: 2px solid #fff;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #777777;\n"
"}")
        self.pushButton_23.setObjectName("pushButton_23")
        self.verticalLayout_7.addWidget(self.pushButton_23)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.listWidget_6 = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidget_6.setStyleSheet("border: 0px;")
        self.listWidget_6.setObjectName("listWidget_6")
        self.horizontalLayout_6.addWidget(self.listWidget_6)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 911, 591))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(15, 30, 15, 15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_2.setStyleSheet("QComboBox {\n"
"    background-color: #777777;\n"
"    min-width: 160px;\n"
"    padding: 12px 16px;\n"
"    border: 2px solid #fff;\n"
"    color: #fff;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left-width: 0px;\n"
"    border-left-color: none;\n"
"    border-left-style: solid; /* just a single line */\n"
"    margin-right: 10px;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/Users/resa/Projekte/Korensics/arrow.png);\n"
"    height: 100px;\n"
"}")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    background-color: #009999;\n"
"    min-width: 160px;\n"
"    padding: 12px 16px;\n"
"    border: 2px solid #fff;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #75bdc3;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    display: none;\n"
"    background-color: #393939;\n"
"    min-width: 160px;\n"
"    padding: 12px 16px;\n"
"    border: 2px solid #fff;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #777777;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    display: none;\n"
"    background-color: #393939;\n"
"    min-width: 160px;\n"
"    padding: 12px 16px;\n"
"    border: 2px solid #fff;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #777777;\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_3.addWidget(self.pushButton_7)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.listWidget_2 = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.listWidget_2.setStyleSheet("border: 0px;")
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout_2.addWidget(self.listWidget_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 911, 591))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(15, 30, 15, 15)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.comboBox_3 = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.comboBox_3.setStyleSheet("QComboBox {\n"
"    background-color: #777777;\n"
"    min-width: 160px;\n"
"    padding: 12px 16px;\n"
"    border: 2px solid #fff;\n"
"    color: #fff;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left-width: 0px;\n"
"    border-left-color: none;\n"
"    border-left-style: solid; /* just a single line */\n"
"    margin-right: 10px;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/Users/resa/Projekte/Korensics/arrow.png);\n"
"    height: 100px;\n"
"}")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox_3)
        self.pushButton_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    background-color: #009999;\n"
"    min-width: 160px;\n"
"    padding: 12px 16px;\n"
"    border: 2px solid #fff;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #75bdc3;\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_4.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"    display: none;\n"
"    background-color: #393939;\n"
"    min-width: 160px;\n"
"    padding: 12px 16px;\n"
"    border: 2px solid #fff;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #777777;\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_4.addWidget(self.pushButton_10)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.tableWidget = QtWidgets.QTableWidget(self.horizontalLayoutWidget_3)
        self.tableWidget.setStyleSheet("QWidget {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 1px solid #fffff8;\n"
"    font-size: 14pt;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    width: 130px;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: #fffff8;\n"
"    font-size: 12pt;\n"
"    padding-top: 30px;\n"
"    padding-left: 30px;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #646464;\n"
"    border: 1px solid #fffff8;\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab_4)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 911, 591))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(15, 30, 15, 15)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_13 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_13.setStyleSheet("QPushButton{\n"
"    background-color: #009999;\n"
"    min-width: 160px;\n"
"    padding: 12px 16px;\n"
"    border: 2px solid #fff;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #75bdc3;\n"
"}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_5.addWidget(self.pushButton_13)
        self.comboBox_4 = QtWidgets.QComboBox(self.horizontalLayoutWidget_4)
        self.comboBox_4.setStyleSheet("QComboBox {\n"
"    background-color: #777777;\n"
"    min-width: 160px;\n"
"    padding: 12px 16px;\n"
"    border: 2px solid #fff;\n"
"    color: #fff;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left-width: 0px;\n"
"    border-left-color: none;\n"
"    border-left-style: solid; /* just a single line */\n"
"    margin-right: 10px;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/Users/resa/Projekte/Korensics/arrow.png);\n"
"    height: 100px;\n"
"}")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.verticalLayout_5.addWidget(self.comboBox_4)
        self.pushButton_15 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_15.setStyleSheet("QPushButton{\n"
"    background-color: #009999;\n"
"    min-width: 160px;\n"
"    padding: 12px 16px;\n"
"    border: 2px solid #fff;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #75bdc3;\n"
"}")
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout_5.addWidget(self.pushButton_15)
        self.pushButton_11 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_11.setStyleSheet("QPushButton {\n"
"    display: none;\n"
"    background-color: #393939;\n"
"    min-width: 160px;\n"
"    padding: 12px 16px;\n"
"    border: 2px solid #fff;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #777777;\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_5.addWidget(self.pushButton_11)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.listWidget_4 = QtWidgets.QListWidget(self.horizontalLayoutWidget_4)
        self.listWidget_4.setObjectName("listWidget_4")
        self.horizontalLayout_4.addWidget(self.listWidget_4)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 937, 22))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")
        self.menuData = QtWidgets.QMenu(self.menubar)
        self.menuData.setObjectName("menuData")
        self.menuKnowledge = QtWidgets.QMenu(self.menubar)
        self.menuKnowledge.setObjectName("menuKnowledge")
        self.menuTest = QtWidgets.QMenu(self.menubar)
        self.menuTest.setObjectName("menuTest")
        self.menuInspection = QtWidgets.QMenu(self.menubar)
        self.menuInspection.setObjectName("menuInspection")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuIntroduction = QtWidgets.QMenu(self.menubar)
        self.menuIntroduction.setObjectName("menuIntroduction")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionload = QtWidgets.QAction(MainWindow)
        self.actionload.setObjectName("actionload")
        self.actionimport = QtWidgets.QAction(MainWindow)
        self.actionimport.setObjectName("actionimport")
        self.actiontrain = QtWidgets.QAction(MainWindow)
        self.actiontrain.setObjectName("actiontrain")
        self.actionimport_2 = QtWidgets.QAction(MainWindow)
        self.actionimport_2.setObjectName("actionimport_2")
        self.actionevaluate = QtWidgets.QAction(MainWindow)
        self.actionevaluate.setObjectName("actionevaluate")
        self.actionload_document = QtWidgets.QAction(MainWindow)
        self.actionload_document.setObjectName("actionload_document")
        self.actioninspect = QtWidgets.QAction(MainWindow)
        self.actioninspect.setObjectName("actioninspect")
        self.menuData.addAction(self.actionload)
        self.menuData.addAction(self.actionimport)
        self.menuKnowledge.addAction(self.actiontrain)
        self.menuKnowledge.addAction(self.actionimport_2)
        self.menuTest.addAction(self.actionevaluate)
        self.menuInspection.addAction(self.actionload_document)
        self.menuInspection.addAction(self.actioninspect)
        self.menubar.addAction(self.menuIntroduction.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuKnowledge.menuAction())
        self.menubar.addAction(self.menuTest.menuAction())
        self.menubar.addAction(self.menuInspection.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_21.clicked.connect(self.loadData)
        self.pushButton_22.clicked.connect(self.saveSpectra)
        self.pushButton_23.clicked.connect(self.getSpectra)
        self.pushButton_21.clicked['bool'].connect(self.listWidget_6.show)
        self.pushButton_5.clicked.connect(self.training)
        self.pushButton_6.clicked.connect(self.save_correlation)
        self.pushButton_9.clicked.connect(self.showStat)
        self.pushButton_13.clicked.connect(self.loadimg)
        self.pushButton_15.clicked.connect(self.toinspect)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pridentifier"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "FFT Fingerprint"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "images only"))
        self.pushButton_21.setText(_translate("MainWindow", "LOAD"))
        self.pushButton_22.setText(_translate("MainWindow", "export data"))
        self.pushButton_23.setText(_translate("MainWindow", "import data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Data"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "FFT Correlation"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Bayes Classifier"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Support Vector Machine"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Neural Network"))
        self.pushButton_5.setText(_translate("MainWindow", "TRAIN"))
        self.pushButton_6.setText(_translate("MainWindow", "export knowledge"))
        self.pushButton_7.setText(_translate("MainWindow", "import knowledge"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Learning"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "FFT Correlation"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Naive Bayes"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Support Vector Machine"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Neural Network"))
        self.pushButton_9.setText(_translate("MainWindow", "EVALUATE"))
        self.pushButton_10.setText(_translate("MainWindow", "save statistics"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Evaluation"))
        self.pushButton_13.setText(_translate("MainWindow", "LOAD IMAGE"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "FFT Correlation"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Bayes Classifier"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Support Vector Machine"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Neural Networks"))
        self.pushButton_15.setText(_translate("MainWindow", "INSPECT"))
        self.pushButton_11.setText(_translate("MainWindow", "save results"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Inspection"))
        self.menuData.setTitle(_translate("MainWindow", "Data"))
        self.menuKnowledge.setTitle(_translate("MainWindow", "Learning"))
        self.menuTest.setTitle(_translate("MainWindow", "Evaluation"))
        self.menuInspection.setTitle(_translate("MainWindow", "Inspection"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuIntroduction.setTitle(_translate("MainWindow", "Instruction"))
        self.actionload.setText(_translate("MainWindow", "load"))
        self.actionimport.setText(_translate("MainWindow", "import data"))
        self.actiontrain.setText(_translate("MainWindow", "train"))
        self.actionimport_2.setText(_translate("MainWindow", "import knowledge"))
        self.actionevaluate.setText(_translate("MainWindow", "evaluate"))
        self.actionload_document.setText(_translate("MainWindow", "load image"))
        self.actioninspect.setText(_translate("MainWindow", "inspect"))



    def loadData(self):

        #print(DIRS)
        filter = "Folder with folders representing each class (*.*)"
        ROOTDIR = QtWidgets.QFileDialog.getExistingDirectory(directory = '..', options = QtWidgets.QFileDialog.ShowDirsOnly)
        DIRS = os.listdir(ROOTDIR)
        print('DIRS: ', DIRS)
        print('ROOTDIR: ', ROOTDIR)

        a=0
        self.printer_types = np.array(())
        for printer in DIRS:
            if printer == '.DS_Store':
                pass
            else:
                self.printer_types = np.append(self.printer_types, printer)
                print('Printer', printer)

        print('printer_types: ', self.printer_types)
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
                        img_path = ROOTDIR + '/' + curr + '/' + img
                        print("img path: " + img_path)
                        #/Users/resa/Studium Master/2. Semester - WiSe2014/Projekt/ipython/printers/canon/005_Canon_L02.tif
                        #tmp = skimage.io.imread(rootdir + '/' + curr + '/' + img, plugin='tifffile')
                        tmp = skimage.io.imread(img_path)
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
                    #select only 1000 brightest pixel
                    magnitude_all[magnitude_all<threshold] = min
                    #magnitude_all_multi[magnitude_all_multi<threshold] = min

                    magnitude_all = magnitude_all - magnitude_all.min()
                    magnitude_all = magnitude_all/magnitude_all.sum()

                    self.data_merged.loc[printer_number] = magnitude_all.reshape(magnitude_all.size).tolist() + [curr]
                    #self.data_merged_multi.loc[printer_number] = magnitude_all_multi.reshape(magnitude_all_multi.size).tolist() + [curr]

                    #save image: merged frequency spectrum by addition
                    f_add = Image.fromarray(np.divide(magnitude_all,magnitude_all.max())*255).convert('RGB')

                    #save image: merged frequency spectrum by addition

                    #use a threshold (only for visualization)
                    self.snippet_amount_perPrinter[printer_number] = segment_count[0]*segment_count[1]*len(imgs)
                    mean = np.divide(magnitude_all_multi.mean(),self.snippet_amount_perPrinter[printer_number])

                    # do the same for multiplied
                    idx = np.argsort(magnitude_all_multi.flatten())
                    c = magnitude_all.flatten()[idx]

                    threshold = c[c.size - nr_pixels]
                    min = magnitude_all_multi.min()
                    magnitude_all_multi[magnitude_all_multi<threshold] = min

                    magnitude_all_multi = magnitude_all_multi - min
                    magnitude_all_multi = magnitude_all_multi/magnitude_all_multi.sum()

                    #self.data_merged_multi.loc[printer_number] = magnitude_all_multi.reshape(magnitude_all_multi.size).tolist() + [curr]

                    f_multi = Image.fromarray(magnitude_all_multi).convert('RGB')
                    f_add.save(curr+"_merged_add.png","PNG")
                    f_multi.save(curr+"_merged_multi.png","PNG")


                else:
                    if self.data.empty==False:
                        self.data.to_pickle(curr+"/spectra.pkl")
                        print("saved spectra!")
                    else:
                        print("Data is still empty, press load first.")


        print("load and prepare data finished!")
        #self.statusBar().showMessage('images are loaded.')
        print('images are loaded.')

    def saveSpectra(self):

        if add_all_fft:
            if self.data_merged.empty==False:
                self.data_merged.to_pickle(SUBPATH+"/data_merged.pkl")
                #self.data_merged_multi.to_pickle(SUBPATH,"/data_merged_multi.pkl")
                self.data_detailed.to_pickle(SUBPATH+"/data_detailed.pkl")
                print("saved merged spectra!")
            else:
                print("Data is still empty, press load first.")
        else:
            if self.data.empty==False:
                self.data.to_pickle(SUBPATH+"/spectra.pkl")
                print("saved spectra!")
            else:
                print("Data is still empty, press load first.")

    def getSpectra(self):

        if add_all_fft:
            self.data_merged = pd.read_pickle(SUBPATH+"/data_merged.pkl")
            #self.data_merged_multi = pd.read_pickle(SUBPATH+"/data_merged_multi.pkl")
            self.data_detailed = pd.read_pickle(SUBPATH+"/data_detailed.pkl")
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
            self.data = pd.read_pickle("B_additiveCorrelation_id_w512_1000px/spectra.pkl")
            self.printer_types = np.unique([printer for printer in self.data.ix[:,1024]])
            self.snippet_amount_perPrinter = np.zeros((len(self.printer_types)))
            if self.data.empty:
                print("No Spectra on memory.")
            else:
                print("got spectra!")

        self.mean = np.zeros((len(self.printer_types),pca_amount,2))
        self.std = np.zeros((len(self.printer_types),pca_amount,2))
        self.apriori = np.zeros((len(self.printer_types),2))

    def training(self):
        if add_all_fft:
            data_normed = np.zeros((self.printer_types.size, snippet_w,snippet_w))
            class_column = self.data_detailed.shape[1]-1
            sum = np.zeros((self.printer_types.size))

            if TRAINING == True:
                for p in range(self.printer_types.size):
                    #vector = np.array(np.divide(self.data_merged.ix[p,:-1],self.snippet_amount_perPrinter[p]))
                    vector = np.array(self.data_merged.ix[p,:-1])
                    data_normed[p,:,:] = np.reshape(vector, (snippet_w,snippet_w))
                    sum[p] = np.sum(np.sum(data_normed[p]))
                    #data_normed[p,:,:] = np.divide(data_normed[p,:,:],sum[p])
                    # Training
                    pd.DataFrame(data_normed[p]).to_pickle(SUBPATH+"/corr_"+self.printer_types[p]+".pkl")
            else:
                # Test data
                for p in range(self.printer_types.size):
                    data_normed[p] = pd.read_pickle("knowledge/corr_"+self.printer_types[p]+".pkl")

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
                # for each segment from one printer
                for row in range(printer_list.shape[0]):
                    #printer_list[row,:].max()
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

            #for p in range(len(self.printer_types)):
            pd.DataFrame(np.array(correctPositiveTrain)).to_pickle(SUBPATH+"/correctPositive.pkl")
            pd.DataFrame(np.array(correctNegativeTrain)).to_pickle(SUBPATH+"/correctNegative.pkl")
            pd.DataFrame(np.array(falsePositiveTrain)).to_pickle(SUBPATH+"/falsePositive.pkl")
            pd.DataFrame(np.array(falseNegativeTrain)).to_pickle(SUBPATH+"/falseNegative.pkl")

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
            name_eigen = SUBPATH+"/eigenData.pkl"
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
                name_mean = SUBPATH+"/" +printer +"_mean.pkl"
                mean.to_pickle(name_mean)
                name_std = SUBPATH+"/" +printer +"_std.pkl"
                std.to_pickle(name_std)
                name_apriori = SUBPATH+"/" +printer +"_apriori.pkl"
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

    def save_correlation(self):

        self.data_merged.to_pickle(SUBPATH+"/data_merged.pkl")

    def showStat(self):
        newstr = []
        if add_all_fft:
            col = []
            col.append('hit_rate')
            col.append('miss_rate')
            col.append('fall_out')
            col.append('accuracy')
            col.append('failure')
            col.append('printer')

            #self.tableWidget = QTableWidget()
            # set row count
            self.tableWidget.setRowCount(int(len(col)-1))
            # set column count
            self.tableWidget.setColumnCount(int(len(self.printer_types)))

            # name columns
            for i in range(len(self.printer_types)):
                self.tableWidget.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(self.printer_types[i]))

            # name rows
            for i in range(len(col)-1):
                self.tableWidget.setVerticalHeaderItem(i, QtWidgets.QTableWidgetItem(col[i]))

            # compute and write stats for every printer
            for i in range(len(self.printer_types)):
                hit_rate = 100*correctPositiveTrain[i] / (correctPositiveTrain[i] + falseNegativeTrain[i])
                miss_rate = 100*falseNegativeTrain[i] / (correctNegativeTrain[i] + falseNegativeTrain[i])
                fall_out = 100*falsePositiveTrain[i] / (falsePositiveTrain[i] + correctNegativeTrain[i])
                amount_all = correctPositiveTrain[i] + correctNegativeTrain[i] + falsePositiveTrain[i] + falseNegativeTrain[i]
                accuracy = 100*(correctPositiveTrain[i]+correctNegativeTrain[i]) / amount_all
                failure = 100*(falsePositiveTrain[i] + falseNegativeTrain[i]) / amount_all

                self.tableWidget.setItem(0,i, QtWidgets.QTableWidgetItem(str(hit_rate) + "%"))
                self.tableWidget.setItem(1,i, QtWidgets.QTableWidgetItem(str(miss_rate) + "%"))
                self.tableWidget.setItem(2,i, QtWidgets.QTableWidgetItem(str(fall_out) + "%"))
                self.tableWidget.setItem(3,i, QtWidgets.QTableWidgetItem(str(accuracy) + "%"))
                self.tableWidget.setItem(4,i, QtWidgets.QTableWidgetItem(str(failure) + "%"))

            statistics = pd.DataFrame(columns=col)

            for i in range(0, len(self.printer_types)):
                #print("TRAIN SET")
                hit_rate = 100*correctPositiveTrain[i] / (correctPositiveTrain[i] + falseNegativeTrain[i])
                miss_rate = 100*falseNegativeTrain[i] / (correctNegativeTrain[i] + falseNegativeTrain[i])
                fall_out = 100*falsePositiveTrain[i] / (falsePositiveTrain[i] + correctNegativeTrain[i])
                amount_all = correctPositiveTrain[i] + correctNegativeTrain[i] + falsePositiveTrain[i] + falseNegativeTrain[i]
                accuracy = 100*(correctPositiveTrain[i]+correctNegativeTrain[i]) / amount_all
                failure = 100*(falsePositiveTrain[i] + falseNegativeTrain[i]) / amount_all
                print(self.printer_types[i], "############################")
                print("Hit Rate: %d %s" % (hit_rate, "%"))
                print("Miss Rate: %d %s" % (miss_rate, "%"))
                print("Fallout: %d %s" % (fall_out, "%"))
                print("-------------------------------")
                print("Accuracy: %d %s" % (accuracy, "%"))
                print("Classification Failure: %d %s" % (failure, "%"))

                statistics.loc[i] = np.array([hit_rate,miss_rate,fall_out,accuracy,failure,self.printer_types[i]])

            statistics.to_pickle(SUBPATH+"/statistics.pkl")
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

        #tabledata = "\n".join((newstr))

        #header = ['date', 'time', '', 'size', 'filename']
        #tm = self.tableView(tabledata, header, self)


    def loadimg(self):
        qimg = QtGui.QImage()
        col = [i for i in range(1024)]
        col.append('name')
        questioned = pd.DataFrame(columns=col)
        filename = QtWidgets.QFileDialog.getOpenFileName(filter='Images (*.png *.xpm *.jpg)')
        #print(filename)
        print((filename[0]), "2. ", (filename[0]))
        qimg.load(filename[0])
        print("image is loaded.")

        #pixmap = QtGui.QPixmap.fromImage(qimg) # show loaded image in screen (too large)
        #self.lbl2.setPixmap(pixmap) # show loaded image in screen (too large)

        tmp = skimage.io.imread(str(filename[0]))

        if tmp.size == 0:
            print("Image could not be load: ")
            print(filename[0])
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
        name_test = SUBPATH+"/QuestionedFeature.pkl"
        questioned_feature.to_pickle(name_test)

        print("Feature extraction of questioned document finished.")
        #self.lbl2.show() # show loaded image in screen (too large)


    def toinspect(self):
        z = 0
        newstr = []
        for printer in self.printer_types:
            print(printer)
            printer_number = np.where(self.printer_types == printer)[0][0]
            # read features
            col = [i for i in range(1024)]
            col.append('name')
            questioned_feature = pd.DataFrame(columns=col)

            name_test = SUBPATH + "/QuestionedFeature.pkl"
            questioned_feature = pd.read_pickle(name_test)

            mean = pd.DataFrame(self.mean[printer_number, :, :], columns=[0, 1])
            std = pd.DataFrame(self.std[printer_number, :, :], columns=[0, 1])
            apriori = self.apriori[printer_number, :]

            name_test = SUBPATH + "/QuestionedFeature.pkl"
            questioned_feature = pd.read_pickle(name_test)

            # import gaussian naive bayes
            mean = pd.read_pickle(printer + "_mean.pkl")
            std = pd.read_pickle(printer + "_std.pkl")
            apriori = np.array(pd.read_pickle(printer + "_apriori.pkl")).T.flatten()

            ## Train Set
            # [correctPositiveTrain[z], correctNegativeTrain[z], falsePositiveTrain[z], falseNegativeTrain[z], tmp, tmp] = GNBMatch(train_feature, self.mean.ix[:,2*z:2*z+1], self.std.ix[:,2*z:2*z+1], apriori, 1)
            # train_feature_length[z] = len(train_feature)
            # Test Set
            [correctPositiveQ, correctNegativeQ, falsePositiveQ, falseNegativeQ, tmp, tmp] = GNBMatch(
                    questioned_feature, mean, std, apriori, 1)

            if (falsePositiveQ + correctPositiveQ >= correctNegativeQ + falseNegativeQ):
                newstr1 = "POSITIVE: "
                quote_pos = "%d %s" % (
                    100 * (falsePositiveQ + correctPositiveQ) / len(questioned_feature), '% agreement ------')
                newstr.append("  ".join((newstr1, printer, quote_pos)))
            else:
                newstr2 = "Negative: "
                quote_neg = "%d %s" % (
                    100 * (falsePositiveQ + correctPositiveQ) / len(questioned_feature), '% agreement')
                newstr.append("  ".join((newstr2, printer, quote_neg)))
            # Zugehörigkeit:       Espon (zu 99%)
            # Nicht-Zugehörigkeit: Canon (zu 94%), HP(zu 100%), Brother (zu 99%)
            # z = z+1
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
            # self.lbl1.setText("\n".join((newstr)))
            print("GNB training finished.")
            z = z + 1


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




def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()