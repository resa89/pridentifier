# -*- coding: utf-8 -*-
import os
import time

from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox


import config
from src.objects import pridentifier
from design import dialog_developer
from src.feature_extractor import save_as_pickled_object, try_to_load_as_pickled_object_or_None


#TODO: remove dropdown menu/training method
#TODO: make window responsive
#TODO: make loading bars show iterative process

class Ui_Pridentifier(object):
    def __init__(self):
        super(Ui_Pridentifier, self).__init__()
        # runtime parameters
        self.SNIPPET_WIDTH = config.SNIPPET_WIDTH
        self.NUMBER_PIXELS = config.NUMBER_PIXELS
        self.SNIPPET_WIDTH_last_upload = config.SNIPPET_WIDTH
        self.NUMBER_PIXELS_last_analysis = config.NUMBER_PIXELS

        self.state = 0 # 0: initial, 1: loaded images, 2: analysed images, 3: evaluated images, 4: load image, 5: inspected

        print("Number of Pixels: ", self.NUMBER_PIXELS)
        self.pridentifier = pridentifier.Pridentifier(self.SNIPPET_WIDTH_last_upload, self.NUMBER_PIXELS_last_analysis)


    def developer_dialog(self):
        # If you pass a parent (self) will block the Main Window,
        # and if you do not pass both will be independent,
        # I recommend you try both cases.
        widget = QtWidgets.QDialog()
        ui=dialog_developer.Ui_Dialog()
        ui.setupUi(widget)
        widget.exec_()

    #slot
    def onImageLoadUpdate(self, value, args=None):
        config.state_loading = value
        if args:
            config.state_loading = 100
            self.state = 1
            time.sleep(1)
            #self.progressBar_loadingData.setValue(value)
            self.pridentifier.write_image_infos(args)
            self.showLoadedData()
            #####
            self.button_loadData.setEnabled(True)
            self.button_train.setEnabled(True)
            self.button_evaluate.setEnabled(True)
            self.button_saveStatistics.setEnabled(True)
            self.button_loadImage.setEnabled(True)
            self.button_inspect.setEnabled(True)
            self.button_saveResults.setEnabled(True)
            self.tableWidget_learning.setColumnCount(0)
            self.tableWidget_learning.clear()
            ######
        return()

    #slot
    def onImageLoadUpdateUI(self, value):
        self.progressBar_loadingData.setValue(value)

    #slot
    def onAnalyzeDataUpdate(self, value, args=None):
        config.state_analysis = value
        if args:
            config.state_analysis = 100
            self.state = 2
            time.sleep(1)
            #self.progressBar_loadingTraining.setValue(value)
            self.pridentifier.write_training_results(args)
            self.showTrainingResult()

            #####
            self.button_loadData.setEnabled(True)
            self.button_train.setEnabled(True)
            self.button_evaluate.setEnabled(True)
            self.button_saveStatistics.setEnabled(True)
            self.button_loadImage.setEnabled(True)
            self.button_inspect.setEnabled(True)
            self.button_saveResults.setEnabled(True)
            ######
            self.tableWidget_evaluation.setColumnCount(0)
            self.tableWidget_evaluation.clear()

        return()

    #slot
    def onAnalyzeDataUpdateUI(self, value):
        self.progressBar_loadingTraining.setValue(value)

    #slot
    def onEvaluateDataUpdate(self, value, args=None):
        config.state_evaluation = value
        if args:
            config.state_evaluation = 100
            self.state = 3
            time.sleep(1)
            #self.progressBar_evaluation.setValue(value)
            self.pridentifier.write_evaluation_results(args)
            self.showEvaluationResult()
            #####
            self.button_loadData.setEnabled(True)
            self.button_train.setEnabled(True)
            self.button_evaluate.setEnabled(True)
            self.button_saveStatistics.setEnabled(True)
            self.button_loadImage.setEnabled(True)
            self.button_inspect.setEnabled(True)
            self.button_saveResults.setEnabled(True)
            ######
        return()

    #slot
    def onEvaluateDataUpdateUI(self, value):
        self.progressBar_evaluation.setValue(value)


    #slot
    def onInspectDataUpdate(self, value, args=None):
        config.state_inspection = value
        if type(args) == pd.DataFrame:
            config.state_inspection = 100
            self.state = 4
            time.sleep(1)
            #self.progressBar_inspection.setValue(value)
            self.pridentifier.write_inspection_results(args)
            self.showInspectionResults()
            #####
            self.button_loadData.setEnabled(True)
            self.button_train.setEnabled(True)
            self.button_evaluate.setEnabled(True)
            self.button_saveStatistics.setEnabled(True)
            self.button_loadImage.setEnabled(True)
            self.button_inspect.setEnabled(True)
            self.button_saveResults.setEnabled(True)
            ######
        return()

    #slot
    def onInspectDataUpdateUI(self, value):
        self.progressBar_inspection.setValue(value)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(942, 676)
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
        self.tab_data = QtWidgets.QWidget()
        self.tab_data.setStyleSheet("")
        self.tab_data.setObjectName("tab_data")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_data)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 911, 656))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(15, 30, 15, 15)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setStyleSheet("color: #fff;\n"
"font: 12pt \"Helvetica\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.spinBox_2 = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox_2.setStyleSheet("    background-color: #777777;\n"
"    min-width: 160px;\n"
"    color: #fff;\n"
"")
        self.spinBox_2.setMinimum(64)
        self.spinBox_2.setMaximum(1024)
        self.spinBox_2.setSingleStep(64)
        self.spinBox_2.setProperty("value", 512)
        self.spinBox_2.setObjectName("spinBox_2")
        self.verticalLayout_7.addWidget(self.spinBox_2)
        self.button_loadData = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_loadData.setStyleSheet("QPushButton {\n"
"background-color: #009999;\n"
"min-width: 160px;\n"
"padding: 12px 16px;\n"
"border: 2px solid #fff;\n"
"color: #fff;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #75bdc3;\n"
"}")
        self.button_loadData.setObjectName("button_loadData")
        self.verticalLayout_7.addWidget(self.button_loadData)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setStyleSheet("color: #fff;\n"
"font: 12pt \"Helvetica\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.progressBar_loadingData = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.progressBar_loadingData.setStyleSheet("QProgressBar {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    text-align: center;\n"
"    padding: 10px 20px 10px 20px;\n"
"\n"
"    background-color: #646464;\n"
"    \n"
"    font-size: 14pt;\n"
"    max-width: 250px;\n"
"    gridline-color: #fffff8;\n"
"    font-size: 10pt;\n"
"    border: 0px solid #fffff8;\n"
"    background-color: #646464;\n"
"    }")
        self.progressBar_loadingData.setProperty("value", 0)
        self.progressBar_loadingData.setObjectName("progressBar_loadingData")
        self.horizontalLayout_5.addWidget(self.progressBar_loadingData)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.tableWidget_data = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.tableWidget_data.setMinimumSize(QtCore.QSize(300, 200))
        self.tableWidget_data.setMaximumSize(QtCore.QSize(3000, 2000))
        self.tableWidget_data.setStyleSheet("QWidget {\n"
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
"    text-align: center;\n"
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
        self.tableWidget_data.setObjectName("tableWidget_data")
        self.tableWidget_data.setColumnCount(0)
        self.tableWidget_data.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget_data)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab_data, "")
        self.tab_learning = QtWidgets.QWidget()
        self.tab_learning.setObjectName("tab_learning")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_learning)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 911, 645))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(15, 30, 15, 15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setStyleSheet("color: #fff;\n"
"font: 12pt \"Helvetica\";\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.spinBox.setStyleSheet("    background-color: #777777;\n"
"    min-width: 160px;\n"
"    color: #fff;\n"
"")
        self.spinBox.setMinimum(10)
        self.spinBox.setMaximum(10000)
        self.spinBox.setSingleStep(100)
        self.spinBox.setProperty("value", 1000)
        self.spinBox.setDisplayIntegerBase(10)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_3.addWidget(self.spinBox)
        self.button_train = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.button_train.setStyleSheet("QPushButton{\n"
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
        self.button_train.setObjectName("button_train")
        self.verticalLayout_3.addWidget(self.button_train)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setStyleSheet("color: #fff;\n"
"font: 12pt \"Helvetica\";")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        self.progressBar_loadingTraining = QtWidgets.QProgressBar(self.horizontalLayoutWidget_2)
        self.progressBar_loadingTraining.setStyleSheet("QProgressBar {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    text-align: center;\n"
"    padding: 10px 20px 10px 20px;\n"
"\n"
"    background-color: #646464;\n"
"    \n"
"    font-size: 14pt;\n"
"    max-width: 250px;\n"
"    gridline-color: #fffff8;\n"
"    font-size: 10pt;\n"
"    border: 0px solid #fffff8;\n"
"    background-color: #646464;\n"
"    }\n"
"\n"
"")
        self.progressBar_loadingTraining.setProperty("value", 0)
        self.progressBar_loadingTraining.setObjectName("progressBar_loadingTraining")
        self.horizontalLayout_11.addWidget(self.progressBar_loadingTraining)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem6)
        self.label_evaluation4c = QtWidgets.QHBoxLayout()
        self.label_evaluation4c.setObjectName("label_evaluation4c")
        self.label_analysis1 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_analysis1.setStyleSheet("QLabel {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 0px solid #fffff8;\n"
"    font-size: 14pt;\n"
"\n"
"    width: 130px;\n"
"    min-height: 150px;\n"
"    gridline-color: #fffff8;\n"
"    font-size: 12pt;\n"
"\n"
"    background-color: #646464;\n"
"    border: 0px solid #fffff8;\n"
"}")
        self.label_analysis1.setText("")
        self.label_analysis1.setObjectName("label_analysis1")
        self.label_evaluation4c.addWidget(self.label_analysis1)
        self.label_analysis2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_analysis2.setStyleSheet("QLabel {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 0px solid #fffff8;\n"
"    font-size: 14pt;\n"
"\n"
"    width: 130px;\n"
"    min-height: 150px;\n"
"    gridline-color: #fffff8;\n"
"    font-size: 12pt;\n"
"\n"
"    background-color: #646464;\n"
"    border: 0px solid #fffff8;\n"
"}")
        self.label_analysis2.setText("")
        self.label_analysis2.setObjectName("label_analysis2")
        self.label_evaluation4c.addWidget(self.label_analysis2)
        self.label_analysis3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_analysis3.setStyleSheet("QLabel {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 0px solid #fffff8;\n"
"    font-size: 14pt;\n"
"\n"
"    width: 130px;\n"
"    min-height: 150px;\n"
"    gridline-color: #fffff8;\n"
"    font-size: 12pt;\n"
"\n"
"    background-color: #646464;\n"
"    border: 0px solid #fffff8;\n"
"}")
        self.label_analysis3.setText("")
        self.label_analysis3.setObjectName("label_analysis3")
        self.label_evaluation4c.addWidget(self.label_analysis3)
        self.label_analysis4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_analysis4.setStyleSheet("QLabel {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 0px solid #fffff8;\n"
"    font-size: 14pt;\n"
"\n"
"    width: 130px;\n"
"    min-height: 150px;\n"
"    gridline-color: #fffff8;\n"
"    font-size: 12pt;\n"
"\n"
"    background-color: #646464;\n"
"    border: 0px solid #fffff8;\n"
"}")
        self.label_analysis4.setText("")
        self.label_analysis4.setObjectName("label_analysis4")
        self.label_evaluation4c.addWidget(self.label_analysis4)
        self.verticalLayout_8.addLayout(self.label_evaluation4c)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_analysis1_class = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_analysis1_class.setStyleSheet("QLabel {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 0px solid #fffff8;\n"
"\n"
"    width: 130px;\n"
"    min-height: 20px;\n"
"    gridline-color: #fffff8;\n"
"    font: 13pt \"Helvetica\";\n"
"\n"
"    background-color: #646464;\n"
"    border: 0px solid #fffff8;\n"
"}")
        self.label_analysis1_class.setText("")
        self.label_analysis1_class.setObjectName("label_analysis1_class")
        self.horizontalLayout_12.addWidget(self.label_analysis1_class)
        self.label_analysis2_class = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_analysis2_class.setStyleSheet("QLabel {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 0px solid #fffff8;\n"
"\n"
"    width: 130px;\n"
"    min-height: 20px;\n"
"    gridline-color: #fffff8;\n"
"    font: 13pt \"Helvetica\";\n"
"\n"
"    background-color: #646464;\n"
"    border: 0px solid #fffff8;\n"
"}")
        self.label_analysis2_class.setText("")
        self.label_analysis2_class.setObjectName("label_analysis2_class")
        self.horizontalLayout_12.addWidget(self.label_analysis2_class)
        self.label_analysis3_class = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_analysis3_class.setStyleSheet("QLabel {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 0px solid #fffff8;\n"
"\n"
"    width: 130px;\n"
"    min-height: 20px;\n"
"    gridline-color: #fffff8;\n"
"    font: 13pt \"Helvetica\";\n"
"\n"
"    background-color: #646464;\n"
"    border: 0px solid #fffff8;\n"
"}")
        self.label_analysis3_class.setText("")
        self.label_analysis3_class.setObjectName("label_analysis3_class")
        self.horizontalLayout_12.addWidget(self.label_analysis3_class)
        self.label_analysis4_class = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_analysis4_class.setStyleSheet("QLabel {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 0px solid #fffff8;\n"
"\n"
"    width: 130px;\n"
"    min-height: 20px;\n"
"    gridline-color: #fffff8;\n"
"    font: 13pt \"Helvetica\";\n"
"\n"
"    background-color: #646464;\n"
"    border: 0px solid #fffff8;\n"
"}")
        self.label_analysis4_class.setText("")
        self.label_analysis4_class.setObjectName("label_analysis4_class")
        self.horizontalLayout_12.addWidget(self.label_analysis4_class)
        self.verticalLayout_8.addLayout(self.horizontalLayout_12)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem8)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_analysis5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_analysis5.setStyleSheet("QLabel {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 0px solid #fffff8;\n"
"    font-size: 14pt;\n"
"\n"
"    width: 130px;\n"
"    min-height: 150px;\n"
"    gridline-color: #fffff8;\n"
"    font-size: 12pt;\n"
"\n"
"    background-color: #646464;\n"
"    border: 0px solid #fffff8;\n"
"}")
        self.label_analysis5.setText("")
        self.label_analysis5.setObjectName("label_analysis5")
        self.horizontalLayout.addWidget(self.label_analysis5)
        self.label_analysis6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_analysis6.setStyleSheet("QLabel {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 0px solid #fffff8;\n"
"    font-size: 14pt;\n"
"\n"
"    width: 130px;\n"
"    min-height: 150px;\n"
"    gridline-color: #fffff8;\n"
"    font-size: 12pt;\n"
"\n"
"    background-color: #646464;\n"
"    border: 0px solid #fffff8;\n"
"}")
        self.label_analysis6.setText("")
        self.label_analysis6.setObjectName("label_analysis6")
        self.horizontalLayout.addWidget(self.label_analysis6)
        self.label_analysis7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_analysis7.setStyleSheet("QLabel {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 0px solid #fffff8;\n"
"    font-size: 14pt;\n"
"\n"
"    width: 130px;\n"
"    min-height: 150px;\n"
"    gridline-color: #fffff8;\n"
"    font-size: 12pt;\n"
"\n"
"    background-color: #646464;\n"
"    border: 0px solid #fffff8;\n"
"}")
        self.label_analysis7.setText("")
        self.label_analysis7.setObjectName("label_analysis7")
        self.horizontalLayout.addWidget(self.label_analysis7)
        self.label_analysis8 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_analysis8.setStyleSheet("QLabel {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 0px solid #fffff8;\n"
"    font-size: 14pt;\n"
"\n"
"    width: 130px;\n"
"    min-height: 150px;\n"
"    gridline-color: #fffff8;\n"
"    font-size: 12pt;\n"
"\n"
"    background-color: #646464;\n"
"    border: 0px solid #fffff8;\n"
"}")
        self.label_analysis8.setText("")
        self.label_analysis8.setObjectName("label_analysis8")
        self.horizontalLayout.addWidget(self.label_analysis8)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_analysis5_class = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_analysis5_class.setStyleSheet("QLabel {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 0px solid #fffff8;\n"
"\n"
"    width: 130px;\n"
"    min-height: 20px;\n"
"    gridline-color: #fffff8;\n"
"    font: 13pt \"Helvetica\";\n"
"\n"
"    background-color: #646464;\n"
"    border: 0px solid #fffff8;\n"
"}")
        self.label_analysis5_class.setText("")
        self.label_analysis5_class.setObjectName("label_analysis5_class")
        self.horizontalLayout_7.addWidget(self.label_analysis5_class)
        self.label_analysis6_class = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_analysis6_class.setStyleSheet("QLabel {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 0px solid #fffff8;\n"
"\n"
"    width: 130px;\n"
"    min-height: 20px;\n"
"    gridline-color: #fffff8;\n"
"    font: 13pt \"Helvetica\";\n"
"\n"
"    background-color: #646464;\n"
"    border: 0px solid #fffff8;\n"
"}")
        self.label_analysis6_class.setText("")
        self.label_analysis6_class.setObjectName("label_analysis6_class")
        self.horizontalLayout_7.addWidget(self.label_analysis6_class)
        self.label_analysis7_class = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_analysis7_class.setStyleSheet("QLabel {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 0px solid #fffff8;\n"
"\n"
"    width: 130px;\n"
"    min-height: 20px;\n"
"    gridline-color: #fffff8;\n"
"    font: 13pt \"Helvetica\";\n"
"\n"
"    background-color: #646464;\n"
"    border: 0px solid #fffff8;\n"
"}")
        self.label_analysis7_class.setText("")
        self.label_analysis7_class.setObjectName("label_analysis7_class")
        self.horizontalLayout_7.addWidget(self.label_analysis7_class)
        self.label_analysis8_class = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_analysis8_class.setStyleSheet("QLabel {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 0px solid #fffff8;\n"
"\n"
"    width: 130px;\n"
"    min-height: 20px;\n"
"    gridline-color: #fffff8;\n"
"    font: 13pt \"Helvetica\";\n"
"\n"
"    background-color: #646464;\n"
"    border: 0px solid #fffff8;\n"
"}")
        self.label_analysis8_class.setText("")
        self.label_analysis8_class.setObjectName("label_analysis8_class")
        self.horizontalLayout_7.addWidget(self.label_analysis8_class)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.tableWidget_learning = QtWidgets.QTableWidget(self.horizontalLayoutWidget_2)
        self.tableWidget_learning.setStyleSheet("QWidget {\n"
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
        self.tableWidget_learning.setObjectName("tableWidget_learning")
        self.tableWidget_learning.setColumnCount(0)
        self.tableWidget_learning.setRowCount(0)
        self.verticalLayout_8.addWidget(self.tableWidget_learning)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.tabWidget.addTab(self.tab_learning, "")
        self.tab_evaluation = QtWidgets.QWidget()
        self.tab_evaluation.setObjectName("tab_evaluation")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_evaluation)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 911, 738))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(15, 30, 15, 15)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.button_evaluate = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.button_evaluate.setStyleSheet("QPushButton{\n"
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
        self.button_evaluate.setObjectName("button_evaluate")
        self.verticalLayout_4.addWidget(self.button_evaluate)
        self.button_saveStatistics = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.button_saveStatistics.setStyleSheet("QPushButton {\n"
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
        self.button_saveStatistics.setObjectName("button_saveStatistics")
        self.verticalLayout_4.addWidget(self.button_saveStatistics)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem10)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setStyleSheet("color: #fff;\n"
"font: 12pt \"Helvetica\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.progressBar_evaluation = QtWidgets.QProgressBar(self.horizontalLayoutWidget_3)
        self.progressBar_evaluation.setStyleSheet("QProgressBar {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    text-align: center;\n"
"    padding: 10px 20px 10px 20px;\n"
"\n"
"    background-color: #646464;\n"
"    \n"
"    font-size: 14pt;\n"
"    max-width: 250px;\n"
"    gridline-color: #fffff8;\n"
"    font-size: 10pt;\n"
"    border: 0px solid #fffff8;\n"
"    background-color: #646464;\n"
"    }\n"
"\n"
"")
        self.progressBar_evaluation.setProperty("value", 0)
        self.progressBar_evaluation.setObjectName("progressBar_evaluation")
        self.horizontalLayout_8.addWidget(self.progressBar_evaluation)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem11)
        self.verticalLayout_10.addLayout(self.horizontalLayout_8)
        self.tableWidget_evaluation = QtWidgets.QTableWidget(self.horizontalLayoutWidget_3)
        self.tableWidget_evaluation.setMinimumSize(QtCore.QSize(300, 200))
        self.tableWidget_evaluation.setMaximumSize(QtCore.QSize(3000, 2000))
        self.tableWidget_evaluation.setStyleSheet("QWidget {\n"
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
        self.tableWidget_evaluation.setObjectName("tableWidget_evaluation")
        self.tableWidget_evaluation.setColumnCount(0)
        self.tableWidget_evaluation.setRowCount(0)
        self.verticalLayout_10.addWidget(self.tableWidget_evaluation)
        self.horizontalLayout_3.addLayout(self.verticalLayout_10)
        self.tabWidget.addTab(self.tab_evaluation, "")
        self.tab_inspection = QtWidgets.QWidget()
        self.tab_inspection.setObjectName("tab_inspection")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab_inspection)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 911, 1532))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(15, 30, 15, 15)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.button_loadImage = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.button_loadImage.setStyleSheet("QPushButton{\n"
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
        self.button_loadImage.setObjectName("button_loadImage")
        self.verticalLayout_5.addWidget(self.button_loadImage)
        self.button_inspect = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.button_inspect.setStyleSheet("QPushButton{\n"
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
        self.button_inspect.setObjectName("button_inspect")
        self.verticalLayout_5.addWidget(self.button_inspect)
        self.button_saveResults = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.button_saveResults.setStyleSheet("QPushButton {\n"
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
        self.button_saveResults.setObjectName("button_saveResults")
        self.verticalLayout_5.addWidget(self.button_saveResults)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem12)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem13)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_5.setStyleSheet("color: #fff;\n"
"font: 12pt \"Helvetica\";")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.progressBar_inspection = QtWidgets.QProgressBar(self.horizontalLayoutWidget_4)
        self.progressBar_inspection.setStyleSheet("QProgressBar {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    text-align: center;\n"
"    padding: 10px 20px 10px 20px;\n"
"\n"
"    background-color: #646464;\n"
"    \n"
"    font-size: 14pt;\n"
"    max-width: 250px;\n"
"    gridline-color: #fffff8;\n"
"    font-size: 10pt;\n"
"    border: 0px solid #fffff8;\n"
"    background-color: #646464;\n"
"    }\n"
"\n"
"\n"
"")
        self.progressBar_inspection.setProperty("value", 0)
        self.progressBar_inspection.setObjectName("progressBar_inspection")
        self.horizontalLayout_9.addWidget(self.progressBar_inspection)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem14)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_inspection = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_inspection.setMinimumSize(QtCore.QSize(200, 258))
        self.label_inspection.setMaximumSize(QtCore.QSize(600, 208))
        self.label_inspection.setStyleSheet("QLabel {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 0px solid #fffff8;\n"
"    font-size: 14pt;\n"
"\n"
"    width: 130px;\n"
"    min-height: 250px;\n"
"    gridline-color: #fffff8;\n"
"    font-size: 12pt;\n"
"    text-align: center;\n"
"\n"
"    background-color: #646464;\n"
"    border: 0px solid #fffff8;\n"
"}")
        self.label_inspection.setText("")
        self.label_inspection.setObjectName("label_inspection")
        self.horizontalLayout_10.addWidget(self.label_inspection)
        self.label_inspection_fingerprint = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_inspection_fingerprint.setMinimumSize(QtCore.QSize(200, 258))
        self.label_inspection_fingerprint.setMaximumSize(QtCore.QSize(600, 208))
        self.label_inspection_fingerprint.setStyleSheet("QLabel {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 0px solid #fffff8;\n"
"    font-size: 14pt;\n"
"\n"
"    width: 130px;\n"
"    min-height: 250px;\n"
"    gridline-color: #fffff8;\n"
"    font-size: 12pt;\n"
"    text-align: center;\n"
"\n"
"    background-color: #646464;\n"
"    border: 0px solid #fffff8;\n"
"}")
        self.label_inspection_fingerprint.setText("")
        self.label_inspection_fingerprint.setObjectName("label_inspection_fingerprint")
        self.horizontalLayout_10.addWidget(self.label_inspection_fingerprint)
        self.verticalLayout_9.addLayout(self.horizontalLayout_10)
        self.tableWidget_inspection = QtWidgets.QTableWidget(self.horizontalLayoutWidget_4)
        self.tableWidget_inspection.setMinimumSize(QtCore.QSize(200, 200))
        self.tableWidget_inspection.setMaximumSize(QtCore.QSize(2000, 3000))
        self.tableWidget_inspection.setStyleSheet("QWidget {\n"
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
        self.tableWidget_inspection.setObjectName("tableWidget_inspection")
        self.tableWidget_inspection.setColumnCount(0)
        self.tableWidget_inspection.setRowCount(0)
        self.verticalLayout_9.addWidget(self.tableWidget_inspection)
        self.horizontalLayout_4.addLayout(self.verticalLayout_9)
        self.tabWidget.addTab(self.tab_inspection, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 942, 22))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")
        self.menuPridentifier = QtWidgets.QMenu(self.menubar)
        self.menuPridentifier.setStyleSheet("background-color: #fff;\n"
"color: #393939;\n"
"")
        self.menuPridentifier.setObjectName("menuPridentifier")
        self.menuInstruction = QtWidgets.QMenu(self.menubar)
        self.menuInstruction.setStyleSheet("background-color: #fff;\n"
"color: #393939;")
        self.menuInstruction.setObjectName("menuInstruction")
        self.menuDevelopment = QtWidgets.QMenu(self.menubar)
        self.menuDevelopment.setStyleSheet("background-color: #fff;\n"
"color: #393939;")
        self.menuDevelopment.setObjectName("menuDevelopment")
        self.menuResearch = QtWidgets.QMenu(self.menubar)
        self.menuResearch.setStyleSheet("background-color: #fff;\n"
"color: #393939;")
        self.menuResearch.setObjectName("menuResearch")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setStyleSheet("background-color: #fff;\n"
"color: #393939;")
        self.menuHelp.setObjectName("menuHelp")
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
        self.actionDevelopment = QtWidgets.QAction(MainWindow)
        self.actionDevelopment.setObjectName("actionDevelopment")
        self.actionCredits = QtWidgets.QAction(MainWindow)
        self.actionCredits.setObjectName("actionCredits")
        self.actionLicence = QtWidgets.QAction(MainWindow)
        self.actionLicence.setObjectName("actionLicence")
        self.actionTroubleshooting = QtWidgets.QAction(MainWindow)
        self.actionTroubleshooting.setObjectName("actionTroubleshooting")
        self.actionFeedback = QtWidgets.QAction(MainWindow)
        self.actionFeedback.setObjectName("actionFeedback")
        self.actionContact = QtWidgets.QAction(MainWindow)
        self.actionContact.setObjectName("actionContact")
        self.actionPurpose = QtWidgets.QAction(MainWindow)
        self.actionPurpose.setObjectName("actionPurpose")
        self.actionUse_Cases = QtWidgets.QAction(MainWindow)
        self.actionUse_Cases.setObjectName("actionUse_Cases")
        self.actionExample = QtWidgets.QAction(MainWindow)
        self.actionExample.setObjectName("actionExample")
        self.actionExperiment = QtWidgets.QAction(MainWindow)
        self.actionExperiment.setObjectName("actionExperiment")
        self.actionExample_2 = QtWidgets.QAction(MainWindow)
        self.actionExample_2.setObjectName("actionExample_2")
        self.actionMethod = QtWidgets.QAction(MainWindow)
        self.actionMethod.setObjectName("actionMethod")
        self.actionExample_3 = QtWidgets.QAction(MainWindow)
        self.actionExample_3.setObjectName("actionExample_3")
        self.actionResult = QtWidgets.QAction(MainWindow)
        self.actionResult.setObjectName("actionResult")
        self.actionExample_4 = QtWidgets.QAction(MainWindow)
        self.actionExample_4.setObjectName("actionExample_4")
        self.actionResult_2 = QtWidgets.QAction(MainWindow)
        self.actionResult_2.setObjectName("actionResult_2")
        self.actionData = QtWidgets.QAction(MainWindow)
        self.actionData.setObjectName("actionData")
        self.actionAnalysis = QtWidgets.QAction(MainWindow)
        self.actionAnalysis.setObjectName("actionAnalysis")
        self.actionEvaluation = QtWidgets.QAction(MainWindow)
        self.actionEvaluation.setObjectName("actionEvaluation")
        self.actionInspection = QtWidgets.QAction(MainWindow)
        self.actionInspection.setObjectName("actionInspection")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAnalysis_Method = QtWidgets.QAction(MainWindow)
        self.actionAnalysis_Method.setObjectName("actionAnalysis_Method")
        self.actionExperiment_Results = QtWidgets.QAction(MainWindow)
        self.actionExperiment_Results.setObjectName("actionExperiment_Results")
        self.actionApplication_Field = QtWidgets.QAction(MainWindow)
        self.actionApplication_Field.setObjectName("actionApplication_Field")
        self.actionTroubleshooting_2 = QtWidgets.QAction(MainWindow)
        self.actionTroubleshooting_2.setObjectName("actionTroubleshooting_2")
        self.actionFeedback_2 = QtWidgets.QAction(MainWindow)
        self.actionFeedback_2.setObjectName("actionFeedback_2")
        self.actionContact_2 = QtWidgets.QAction(MainWindow)
        self.actionContact_2.setObjectName("actionContact_2")
        self.actionDeveloper = QtWidgets.QAction(MainWindow)
        self.actionDeveloper.setObjectName("actionDeveloper")
        self.actionParticipating_People = QtWidgets.QAction(MainWindow)
        self.actionParticipating_People.setObjectName("actionParticipating_People")
        self.actionCredits_2 = QtWidgets.QAction(MainWindow)
        self.actionCredits_2.setObjectName("actionCredits_2")
        self.actionOpen_Questions = QtWidgets.QAction(MainWindow)
        self.actionOpen_Questions.setObjectName("actionOpen_Questions")
        self.actionAbout_Pridentifier = QtWidgets.QAction(MainWindow)
        self.actionAbout_Pridentifier.setObjectName("actionAbout_Pridentifier")
        self.actionAbout_2 = QtWidgets.QAction(MainWindow)
        self.actionAbout_2.setObjectName("actionAbout_2")
        self.menuPridentifier.addAction(self.actionAbout_2)
        self.menuPridentifier.addAction(self.actionAbout_Pridentifier)
        self.menuPridentifier.addAction(self.actionApplication_Field)
        self.menuInstruction.addAction(self.actionData)
        self.menuInstruction.addAction(self.actionAnalysis)
        self.menuInstruction.addAction(self.actionEvaluation)
        self.menuInstruction.addAction(self.actionInspection)
        self.menuDevelopment.addAction(self.actionDeveloper)
        self.menuDevelopment.addAction(self.actionParticipating_People)
        self.menuDevelopment.addAction(self.actionCredits_2)
        self.menuResearch.addAction(self.actionAnalysis_Method)
        self.menuResearch.addAction(self.actionExperiment_Results)
        self.menuResearch.addAction(self.actionOpen_Questions)
        self.menuHelp.addAction(self.actionTroubleshooting_2)
        self.menuHelp.addAction(self.actionFeedback_2)
        self.menuHelp.addAction(self.actionContact_2)
        self.menubar.addAction(self.menuPridentifier.menuAction())
        self.menubar.addAction(self.menuInstruction.menuAction())
        self.menubar.addAction(self.menuDevelopment.menuAction())
        self.menubar.addAction(self.menuResearch.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.button_loadData.clicked.connect(self.loadData)
        self.button_loadImage.clicked.connect(self.loadImg)
        self.button_saveStatistics.clicked.connect(self.saveStat)
        self.button_saveResults.clicked.connect(self.saveResult)
        self.button_train.clicked.connect(self.training)
        self.button_inspect.clicked.connect(self.inspection)
        self.spinBox_2.valueChanged['int'].connect(self.changeSegmentSize)
        self.spinBox.valueChanged['int'].connect(self.changeFeatureCount)
        self.button_evaluate.clicked.connect(self.evaluate)
        # add dialogs
        self.actionDeveloper.triggered.connect(self.developer_dialog)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pridentifier"))
        self.label_3.setText(_translate("MainWindow", "Segment width/height:"))
        self.button_loadData.setText(_translate("MainWindow", "LOAD"))
        self.label_2.setText(_translate("MainWindow", "Loading:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_data), _translate("MainWindow", "Data"))
        self.label.setText(_translate("MainWindow", "Features:"))
        self.button_train.setText(_translate("MainWindow", "ANALYZE"))
        self.label_7.setText(_translate("MainWindow", "Analysis:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_learning), _translate("MainWindow", "Analysis"))
        self.button_evaluate.setText(_translate("MainWindow", "EVALUATE"))
        self.button_saveStatistics.setText(_translate("MainWindow", "save results"))
        self.label_4.setText(_translate("MainWindow", "Evaluation:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_evaluation), _translate("MainWindow", "Evaluation"))
        self.button_loadImage.setText(_translate("MainWindow", "LOAD IMAGE"))
        self.button_inspect.setText(_translate("MainWindow", "INSPECT"))
        self.button_saveResults.setText(_translate("MainWindow", "save results"))
        self.label_5.setText(_translate("MainWindow", "Inspection:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_inspection), _translate("MainWindow", "Inspection"))
        self.menuPridentifier.setTitle(_translate("MainWindow", "Pridentifier"))
        self.menuInstruction.setTitle(_translate("MainWindow", "Instruction"))
        self.menuDevelopment.setTitle(_translate("MainWindow", "Development"))
        self.menuResearch.setTitle(_translate("MainWindow", "Research"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionload.setText(_translate("MainWindow", "load"))
        self.actionimport.setText(_translate("MainWindow", "import data"))
        self.actiontrain.setText(_translate("MainWindow", "train"))
        self.actionimport_2.setText(_translate("MainWindow", "import knowledge"))
        self.actionevaluate.setText(_translate("MainWindow", "evaluate"))
        self.actionload_document.setText(_translate("MainWindow", "load image"))
        self.actioninspect.setText(_translate("MainWindow", "inspect"))
        self.actionDevelopment.setText(_translate("MainWindow", "Development"))
        self.actionCredits.setText(_translate("MainWindow", "Credits"))
        self.actionLicence.setText(_translate("MainWindow", "Licence"))
        self.actionTroubleshooting.setText(_translate("MainWindow", "Troubleshooting"))
        self.actionFeedback.setText(_translate("MainWindow", "Feedback"))
        self.actionContact.setText(_translate("MainWindow", "Contact"))
        self.actionPurpose.setText(_translate("MainWindow", "Purpose"))
        self.actionUse_Cases.setText(_translate("MainWindow", "Use Cases"))
        self.actionExample.setText(_translate("MainWindow", "Example"))
        self.actionExperiment.setText(_translate("MainWindow", "Method"))
        self.actionExample_2.setText(_translate("MainWindow", "Example"))
        self.actionMethod.setText(_translate("MainWindow", "Method"))
        self.actionExample_3.setText(_translate("MainWindow", "Example"))
        self.actionResult.setText(_translate("MainWindow", "Result"))
        self.actionExample_4.setText(_translate("MainWindow", "Example"))
        self.actionResult_2.setText(_translate("MainWindow", "Result"))
        self.actionData.setText(_translate("MainWindow", "Data"))
        self.actionAnalysis.setText(_translate("MainWindow", "Analysis"))
        self.actionEvaluation.setText(_translate("MainWindow", "Evaluation"))
        self.actionInspection.setText(_translate("MainWindow", "Inspection"))
        self.actionAbout.setText(_translate("MainWindow", "About Pridentifier"))
        self.actionAnalysis_Method.setText(_translate("MainWindow", "Analysis Method"))
        self.actionExperiment_Results.setText(_translate("MainWindow", "Experimental Results"))
        self.actionApplication_Field.setText(_translate("MainWindow", "Application Fields"))
        self.actionTroubleshooting_2.setText(_translate("MainWindow", "Troubleshooting"))
        self.actionFeedback_2.setText(_translate("MainWindow", "Feedback"))
        self.actionContact_2.setText(_translate("MainWindow", "Contact"))
        self.actionDeveloper.setText(_translate("MainWindow", "Developer"))
        self.actionParticipating_People.setText(_translate("MainWindow", "Participating People"))
        self.actionCredits_2.setText(_translate("MainWindow", "Credits"))
        self.actionOpen_Questions.setText(_translate("MainWindow", "Open Questions"))
        self.actionAbout_Pridentifier.setText(_translate("MainWindow", "About Pridentifier"))
        self.actionAbout_2.setText(_translate("MainWindow", "About"))




    def showFingerprints(self, train=True):

        #TODO: also add fingerprint images to inspection tab with train=False

        # prepare widgets for ever image
        list_of_labels = [self.label_analysis1, self.label_analysis2, self.label_analysis3, self.label_analysis4,
                          self.label_analysis5, self.label_analysis6, self.label_analysis7, self.label_analysis8]
        list_of_texts = [self.label_analysis1_class, self.label_analysis2_class, self.label_analysis3_class,
                         self.label_analysis4_class, self.label_analysis5_class, self.label_analysis6_class,
                         self.label_analysis7_class, self.label_analysis8_class]
        test_label = self.label_inspection_fingerprint

        #TODO: make size of widgets dynamic

        # prepare path to fingerprint images
        path = config.SUBPATH + '/fingerprint/'

        if not os.path.exists(path):
            os.makedirs(path)

        classes = self.pridentifier.get_classes()

        for i in range(len(classes)):
            class_name = classes[i]
            qimg = QtGui.QImage()
            if train:
                img_path = path + class_name + "_fingerprint.png"
                #data_path = path + class_name + "_fingerprint.pkl"
            else:
                img_path = path + "test_Q_fingerprint.png"
                #data_path = path + "test_" + class_name + "_fingerprint.pkl"

            qimg.load(img_path)
            #create widget
            fingerprint = QPixmap.fromImage(qimg)

            if train:
                label = list_of_labels[i]
                text = list_of_texts[i]
            else:
                label = test_label
                text = ''

            label.setPixmap(fingerprint.scaled(
                    label.size(), QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation))

            label.setAlignment(QtCore.Qt.AlignCenter)
            #self.tableWidget_inspection.clear()


            if train:
                text.setText(class_name)



    def loadData(self):
        # print(DIRS)
        #filter = "Folder with folders representing each class (*.*)"
        config.state_loading = 0
        dialog = QtWidgets.QFileDialog()
        path = dialog.getExistingDirectory(directory='..', options=QtWidgets.QFileDialog.ShowDirsOnly)

        if path:

            self.progressBar_loadingData.setValue(0)

            # use the last set snippet size in ui
            self.SNIPPET_WIDTH_last_upload = self.SNIPPET_WIDTH
            self.pridentifier.update_snippetSize(self.SNIPPET_WIDTH_last_upload)

            #####
            self.button_loadData.setEnabled(False)
            self.button_train.setEnabled(False)
            self.button_evaluate.setEnabled(False)
            self.button_saveStatistics.setEnabled(False)
            self.button_loadImage.setEnabled(False)
            self.button_inspect.setEnabled(False)
            self.button_saveResults.setEnabled(False)
            ######

            #####
            self.calc = self.pridentifier.load_images(path)
            self.calc.imageUploadStatusChanged.connect(self.onImageLoadUpdate)
            self.calc.start()
            #####
            #####
            self.calc4 =ProgressLoadingVisualizer()
            self.calc4.loadingStatusChanged.connect(self.onImageLoadUpdateUI)
            self.calc4.start()
            #####
            #self.progressBar_loadingData.setValue(100)

    def showLoadedData(self):
            # numbers of loaded data
            self.loadTable(self.tableWidget_data)
            # TODO: rewrite table when data is loaded a second time

    def loadTable(self, tableWidget):
        tableWidget.setRowCount(3)
        # set column count
        tableWidget.setColumnCount(int(len(self.pridentifier.get_classes())))

        #name columns
        classes = self.pridentifier.get_classes()
        for i in range(len(classes)):
            tableWidget.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(classes[i]))
        tableWidget.resizeColumnsToContents()

        #col = []
        #col.append('number of documents')
        #col.append('segments:')

        # name rows
        #for i in range(len(col)):
        tableWidget.setRowCount(2)
        tableWidget.setVerticalHeaderItem(0, QtWidgets.QTableWidgetItem('images:'))
        tableWidget.setVerticalHeaderItem(1, QtWidgets.QTableWidgetItem('segments:'))

        img_no, seg_no = self.pridentifier.get_numbers_per_printer()

        # compute and write stats for every printer
        for i in range(len(classes)):
            #tableWidgeta.setItem(0,i, QtWidgets.QTableWidgetItem(str(self.inspector.data_detailed.shape[0]) + "segments"))
            tableWidget.setItem(0,i, QtWidgets.QTableWidgetItem(str(int(img_no[i]))))#self.inspector.data_detailed.shape[0]/4)))) #ToDo: check segment amount per printer
            tableWidget.setItem(1,i, QtWidgets.QTableWidgetItem(str(int(seg_no[i]))))#self.inspector.data_detailed.shape[0]/4)))) #ToDo: check segment amount per printer

    '''
    def saveSpectra(self):

        self.pridentifier.save_fingerprints()

    def getSpectra(self):
        filter = "Folder which contains the data_detailed.pkl and data_merged.pkl files. (*.*)"
        path = QtWidgets.QFileDialog.getExistingDirectory(directory='..', options=QtWidgets.QFileDialog.ShowDirsOnly)
        print('selected path to get data: ', path)

        if path:
            self.pridentifier.get_fingerprints(path)
            self.progressBar_loadingData.setValue(100)
            self.loadTable(self.tableWidget_data)
    '''

    def training(self):
        if self.state >= 1:
            self.progressBar_loadingTraining.setValue(0)
            config.state_analysis = 0

            # use the last set snippet size in ui
            self.NUMBER_PIXELS_last_analysis = self.NUMBER_PIXELS
            self.pridentifier.update_pixelSize(self.NUMBER_PIXELS_last_analysis)

            #####
            self.button_loadData.setEnabled(False)
            self.button_train.setEnabled(False)
            self.button_evaluate.setEnabled(False)
            self.button_saveStatistics.setEnabled(False)
            self.button_loadImage.setEnabled(False)
            self.button_inspect.setEnabled(False)
            self.button_saveResults.setEnabled(False)
            ######
            self.calc2b =ProgressAnalyzeVisualizer()
            self.calc2b.analysisStatusChanged.connect(self.onAnalyzeDataUpdateUI)
            self.calc2b.start()
            #####

            #####
            self.calc2 = self.pridentifier.extract_features()
            self.calc2.analyzeDataStatusChanged.connect(self.onAnalyzeDataUpdate)
            self.calc2.start()
            #####
            #self.progressBar_loadingTraining.setValue(100)
            #self.tableWidget_learning
        else:
            self.tableWidget_learning.setColumnCount(1)
            self.tableWidget_learning.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem('You have to load data first, before you can do an analysis.'))
            self.tableWidget_learning.resizeColumnsToContents()

    def showTrainingResult(self):
        # show computed fingerprint images
        self.showFingerprints()


    '''
    # import analysis
    def getCorrelation(self):
        filter = "Folder which contains the data_detailed.pkl and data_merged.pkl files. (*.*)"
        path = QtWidgets.QFileDialog.getOpenFileName(filter='Images (*.pkl)')
        #path = "/Users/resa/Projekte/Korensics/02-Pridentifier/generated_data"
        print('selected path to get data: ', path)

        if path != None:
            self.pridentifier.fingerprints = try_to_load_as_pickled_object_or_None(path)
            #self.progressBar_loadingTraining.setValue(100)
            self.loadTable(self.tableWidget_learning)


    # export analysis
    def saveCorrelation(self):
        filter = "Folder which contains the data_detailed.pkl and data_merged.pkl files. (*.*)"
        path = QtWidgets.QFileDialog.getExistingDirectory(directory='..', options=QtWidgets.QFileDialog.ShowDirsOnly)
        #path = "/Users/resa/Projekte/Korensics/02-Pridentifier/generated_data"
        print('selected path to get data: ', path)

        path = path + '/pridentifier_exported_analysis.pkl'

        if path:
            save_as_pickled_object(self.pridentifier.fingerprints, path)
            #self.progressBar_loadingTraining.setValue(100)
            self.loadTable(self.tableWidget_learning)

    '''

    def evaluate(self):
        if self.state >= 2:
            self.progressBar_evaluation.setValue(0)
            config.state_evaluation = 0

            #####
            self.button_loadData.setEnabled(False)
            self.button_train.setEnabled(False)
            self.button_evaluate.setEnabled(False)
            self.button_saveStatistics.setEnabled(False)
            self.button_loadImage.setEnabled(False)
            self.button_inspect.setEnabled(False)
            self.button_saveResults.setEnabled(False)
            #####
            self.calc5 =ProgressEvaluateVisualizer()
            self.calc5.evaluationStatusChanged.connect(self.onEvaluateDataUpdateUI)
            self.calc5.start()
            #####
            self.calc3 = self.pridentifier.evaluate()
            self.calc3.evaluateDataStatusChanged.connect(self.onEvaluateDataUpdate)
            self.calc3.start()
            #####
        else:
            self.tableWidget_evaluation.setColumnCount(1)
            self.tableWidget_evaluation.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem('You have to load and analyze data first, before you can do an evaluation.'))
            self.tableWidget_evaluation.resizeColumnsToContents()

    def showEvaluationResult(self):
        # generate data for table
        col = []
        col.append('true positive')
        col.append('true negative')
        col.append('false positive')
        col.append('false negative')
        col.append('accuracy')
        #col.append('printer')

        #self.tableWidget = QTableWidget()
        # set row count
        self.tableWidget_evaluation.setRowCount(int(len(col)))

        # set column count
        self.tableWidget_evaluation.setColumnCount(int(len(self.pridentifier.get_classes())))

        # name columns
        for i in range(len(self.pridentifier.get_classes())):
            self.tableWidget_evaluation.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(self.pridentifier.get_classes()[i]))
        self.tableWidget_evaluation.resizeColumnsToContents()

        # name rows
        for i in range(len(col)):
            self.tableWidget_evaluation.setVerticalHeaderItem(i, QtWidgets.QTableWidgetItem(col[i]))

        # get computed statistcs
        statistics = self.pridentifier.get_stats()
        true_positives = statistics[0]
        true_negatives = statistics[1]
        false_positives= statistics[2]
        false_negatives = statistics[3]
        accuracy = statistics[4]

        # compute and write stats for every printer
        for i in range(len(self.pridentifier.get_classes())):

            self.tableWidget_evaluation.setItem(0,i, QtWidgets.QTableWidgetItem(str(true_positives[i]) + "%"))
            self.tableWidget_evaluation.setItem(1,i, QtWidgets.QTableWidgetItem(str(true_negatives[i]) + "%"))
            self.tableWidget_evaluation.setItem(2,i, QtWidgets.QTableWidgetItem(str(false_positives[i]) + "%"))
            self.tableWidget_evaluation.setItem(3,i, QtWidgets.QTableWidgetItem(str(false_negatives[i]) + "%"))
            self.tableWidget_evaluation.setItem(4,i, QtWidgets.QTableWidgetItem(str(accuracy[i]) + "%"))



    def saveStat(self):
        path = QtWidgets.QFileDialog.getSaveFileName(filter="CSV File (*.csv)")
        result = self.pridentifier.get_evaluation_result(train=True)
        if not result.empty:
            result.to_csv(path[0])




    def loadImg(self):
        if self.state >= 2:
            filename = QtWidgets.QFileDialog.getOpenFileName(filter='Images (*.png *.xpm *.jpg)')

            if filename:
                qimg = QtGui.QImage()
                qimg.load(filename[0])

                # Create widget
                if qimg:
                    self.pridentifier.set_inspection_image_path(filename[0])
                    pixmap = QPixmap.fromImage(qimg)
                    #self.label_inspection.setPixmap(pixmap)
                    #self.label_inspection.setScaledContents(True)
                    self.label_inspection.setPixmap(pixmap.scaled(
                        self.label_inspection.size(), QtCore.Qt.KeepAspectRatio,
                        QtCore.Qt.SmoothTransformation))

                    self.label_inspection.setAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget_inspection.clear()
                    self.tableWidget_inspection.setRowCount(0)
                    self.tableWidget_inspection.setColumnCount(0)
                    self.label_inspection_fingerprint.clear()
                    self.label_inspection_fingerprint.setAlignment(QtCore.Qt.AlignCenter)
                    self.progressBar_inspection.setValue(0)
                    config.state_inspection = 0
                    self.state = 4
                    self.tableWidget_inspection.setColumnCount(0)
                    self.tableWidget_inspection.clear()




    def inspection(self):
        if self.state >= 4:
            self.progressBar_inspection.setValue(0)
            #####
            self.button_loadData.setEnabled(False)
            self.button_train.setEnabled(False)
            self.button_evaluate.setEnabled(False)
            self.button_saveStatistics.setEnabled(False)
            self.button_loadImage.setEnabled(False)
            self.button_inspect.setEnabled(False)
            self.button_saveResults.setEnabled(False)
            ######
            #####
            self.calc6 =ProgressInspectionVisualizer()
            self.calc6.inspectionStatusChanged.connect(self.onInspectDataUpdateUI)
            self.calc6.start()
            #####
            #####
            self.calc3a = self.pridentifier.inspect()
            self.calc3a.inspectDataStatusChanged.connect(self.onInspectDataUpdate)
            self.calc3a.start()
            #####
        else:
            self.tableWidget_inspection.setColumnCount(1)
            self.tableWidget_inspection.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem('You have to load and alayze data and load an inspection image first, before you can do an inspection.'))
            self.tableWidget_inspection.resizeColumnsToContents()




    def showInspectionResults(self):
        # show computed fingerprint images
        self.showFingerprints(train=False)
        # get computed statistcs for test image
        statistics = self.pridentifier.get_stats(train=False)
        classified_as_class = statistics[0]
        probabilities = statistics[1]

        col = []
        col.append('Classified Segments')
        #col.append('false negative')
        #col.append('fall out')
        #col.append('accuracy')
        #col.append('failure')
        col.append('Probability')

        #self.tableWidget = QTableWidget()
        # set row count
        self.tableWidget_inspection.setRowCount(2)
        # set column count
        self.tableWidget_inspection.setColumnCount(int(len(self.pridentifier.get_classes())))


        # name columns
        for i in range(len(self.pridentifier.get_classes())):
            self.tableWidget_inspection.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(self.pridentifier.get_classes()[i]))
        self.tableWidget_inspection.resizeColumnsToContents()

        # name rows
        for i in range(len(col)):
            self.tableWidget_inspection.setVerticalHeaderItem(i, QtWidgets.QTableWidgetItem(col[i]))


        # compute and write stats for every printer
        for i in range(len(self.pridentifier.get_classes())):

            self.tableWidget_inspection.setItem(0,i, QtWidgets.QTableWidgetItem(str(classified_as_class[i])))
            self.tableWidget_inspection.setItem(1,i, QtWidgets.QTableWidgetItem(str(probabilities[i]) + "%"))



    def saveResult(self):

        path = QtWidgets.QFileDialog.getSaveFileName(filter="CSV File (*.csv)")
        result = self.pridentifier.get_evaluation_result(train=False)
        if not result.empty:
            result.to_csv(path[0])
        #print('Inspection TO SAVE: \n', result)


    def changeSegmentSize(self, size):
        self.SNIPPET_WIDTH = size #TODO: change constants



    def changeFeatureCount(self, count):
        self.NUMBER_PIXELS = count #TODO: change constants



class ProgressLoadingVisualizer(QtCore.QThread, QtCore.QObject):
    """
    Runs a counter object.
    """
    loadingStatusChanged = pyqtSignal(int)

    def __init__(self):
        super(ProgressLoadingVisualizer, self).__init__()

    def run(self):
        count = 0
        while count < 100:
            count = config.state_loading
            self.loadingStatusChanged.emit(count)
            time.sleep(1)

class ProgressAnalyzeVisualizer(QtCore.QThread, QtCore.QObject):
    """
    Runs a counter object.
    """
    analysisStatusChanged = pyqtSignal(int)

    def __init__(self):
        super(ProgressAnalyzeVisualizer, self).__init__()

    def run(self):
        count = 0
        while count < 100:
            count = config.state_analysis
            self.analysisStatusChanged.emit(count)
            time.sleep(1)

class ProgressEvaluateVisualizer(QtCore.QThread, QtCore.QObject):
    """
    Runs a counter object.
    """
    evaluationStatusChanged = pyqtSignal(int)

    def __init__(self):
        super(ProgressEvaluateVisualizer, self).__init__()

    def run(self):
        count = 0
        while count < 100:
            count = config.state_evaluation
            self.evaluationStatusChanged.emit(count)
            time.sleep(1)


class ProgressInspectionVisualizer(QtCore.QThread, QtCore.QObject):
    """
    Runs a counter object.
    """
    inspectionStatusChanged = pyqtSignal(int)

    def __init__(self):
        super(ProgressInspectionVisualizer, self).__init__()

    def run(self):
        count = 0
        while count < 100:
            count = config.state_inspection
            self.inspectionStatusChanged.emit(count)
            time.sleep(1)





def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = Ui_Pridentifier()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())
    app.exit()


if __name__ == '__main__':
    main()
