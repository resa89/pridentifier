# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pridentifier2.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets

import pandas as pd
from PyQt5.QtGui import QPixmap

from config import *
from src import inspector


class Ui_MainWindow(object):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        print("Number of Pixels: ", nr_pixels)
        self.inspector = inspector.Inspector()

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
        self.tab_data = QtWidgets.QWidget()
        self.tab_data.setStyleSheet("")
        self.tab_data.setObjectName("tab_data")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_data)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 911, 591))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(15, 30, 15, 15)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setStyleSheet("color: #fff;\n"
"font: 14pt \"Helvetica\";")
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.dropdown_dataMethod = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.dropdown_dataMethod.setStyleSheet("QComboBox {\n"
"    background-color: #777777;\n"
"    min-width: 160px;\n"
"    padding: 12px 4px;\n"
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
        self.dropdown_dataMethod.setObjectName("dropdown_dataMethod")
        self.dropdown_dataMethod.addItem("")
        self.dropdown_dataMethod.addItem("")
        self.verticalLayout_7.addWidget(self.dropdown_dataMethod)
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
        self.button_exportData = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_exportData.setStyleSheet("QPushButton {\n"
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
        self.button_exportData.setObjectName("button_exportData")
        self.verticalLayout_7.addWidget(self.button_exportData)
        self.button_importData = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_importData.setStyleSheet("QPushButton{\n"
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
        self.button_importData.setObjectName("button_importData")
        self.verticalLayout_7.addWidget(self.button_importData)
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
        self.label_2.setStyleSheet("color: #fff;")
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
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 911, 591))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(15, 30, 15, 15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
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
        self.button_exportKnowledge = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.button_exportKnowledge.setStyleSheet("QPushButton {\n"
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
        self.button_exportKnowledge.setObjectName("button_exportKnowledge")
        self.verticalLayout_3.addWidget(self.button_exportKnowledge)
        self.button_importKnowledge = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.button_importKnowledge.setStyleSheet("QPushButton {\n"
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
        self.button_importKnowledge.setObjectName("button_importKnowledge")
        self.verticalLayout_3.addWidget(self.button_importKnowledge)
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
        self.label_7.setStyleSheet("color: #fff;")
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
"    }")
        self.progressBar_loadingTraining.setProperty("value", 0)
        self.progressBar_loadingTraining.setObjectName("progressBar_loadingTraining")
        self.horizontalLayout_11.addWidget(self.progressBar_loadingTraining)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
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
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_evaluation1 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_evaluation1.setStyleSheet("QLabel {\n"
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
        self.label_evaluation1.setText("")
        self.label_evaluation1.setObjectName("label_evaluation1")
        self.horizontalLayout_7.addWidget(self.label_evaluation1)
        self.label_evaluation2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_evaluation2.setStyleSheet("QLabel {\n"
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
        self.label_evaluation2.setText("")
        self.label_evaluation2.setObjectName("label_evaluation2")
        self.horizontalLayout_7.addWidget(self.label_evaluation2)
        self.label_evaluation3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_evaluation3.setStyleSheet("QLabel {\n"
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
        self.label_evaluation3.setText("")
        self.label_evaluation3.setObjectName("label_evaluation3")
        self.horizontalLayout_7.addWidget(self.label_evaluation3)
        self.label_evaluation4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_evaluation4.setStyleSheet("QLabel {\n"
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
        self.label_evaluation4.setText("")
        self.label_evaluation4.setObjectName("label_evaluation4")
        self.horizontalLayout_7.addWidget(self.label_evaluation4)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_evaluation1_text = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_evaluation1_text.setStyleSheet("QLabel {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 0px solid #fffff8;\n"
"    font-size: 14pt;\n"
"\n"
"    width: 130px;\n"
"    min-height: 20px;\n"
"    gridline-color: #fffff8;\n"
"    font-size: 12pt;\n"
"\n"
"    background-color: #646464;\n"
"    border: 0px solid #fffff8;\n"
"}")
        self.label_evaluation1_text.setText("")
        self.label_evaluation1_text.setObjectName("label_evaluation1_text")
        self.horizontalLayout.addWidget(self.label_evaluation1_text)
        self.label_evaluation2_text = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_evaluation2_text.setStyleSheet("QLabel {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 0px solid #fffff8;\n"
"    font-size: 14pt;\n"
"\n"
"    width: 130px;\n"
"    min-height: 20px;\n"
"    gridline-color: #fffff8;\n"
"    font-size: 12pt;\n"
"\n"
"    background-color: #646464;\n"
"    border: 0px solid #fffff8;\n"
"}")
        self.label_evaluation2_text.setText("")
        self.label_evaluation2_text.setObjectName("label_evaluation2_text")
        self.horizontalLayout.addWidget(self.label_evaluation2_text)
        self.label_evaluation3_text = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_evaluation3_text.setStyleSheet("QLabel {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 0px solid #fffff8;\n"
"    font-size: 14pt;\n"
"\n"
"    width: 130px;\n"
"    min-height: 20px;\n"
"    gridline-color: #fffff8;\n"
"    font-size: 12pt;\n"
"\n"
"    background-color: #646464;\n"
"    border: 0px solid #fffff8;\n"
"}")
        self.label_evaluation3_text.setText("")
        self.label_evaluation3_text.setObjectName("label_evaluation3_text")
        self.horizontalLayout.addWidget(self.label_evaluation3_text)
        self.label_evaluation4_text = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_evaluation4_text.setStyleSheet("QLabel {\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 0px solid #fffff8;\n"
"    font-size: 14pt;\n"
"\n"
"    width: 130px;\n"
"    min-height: 20px;\n"
"    gridline-color: #fffff8;\n"
"    font-size: 12pt;\n"
"\n"
"    background-color: #646464;\n"
"    border: 0px solid #fffff8;\n"
"}")
        self.label_evaluation4_text.setText("")
        self.label_evaluation4_text.setObjectName("label_evaluation4_text")
        self.horizontalLayout.addWidget(self.label_evaluation4_text)
        self.verticalLayout_10.addLayout(self.horizontalLayout)
        self.tableWidget_evaluation = QtWidgets.QTableWidget(self.horizontalLayoutWidget_3)
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
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem7)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_inspection = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
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
        self.verticalLayout_9.addWidget(self.label_inspection)
        self.tableWidget_inspection = QtWidgets.QTableWidget(self.horizontalLayoutWidget_4)
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
        self.button_loadData.clicked.connect(self.loadData)
        self.button_exportData.clicked.connect(self.saveSpectra)
        self.button_importData.clicked.connect(self.getSpectra)
        self.button_evaluate.clicked.connect(self.showStat)
        self.button_loadImage.clicked.connect(self.loadImg)
        self.button_importKnowledge.clicked.connect(self.getCorrelation)
        self.button_exportKnowledge.clicked.connect(self.saveCorrelation)
        self.button_saveStatistics.clicked.connect(self.saveStat)
        self.button_saveResults.clicked.connect(self.saveResult)
        self.button_train.clicked.connect(self.training)
        self.button_inspect.clicked.connect(self.inspection)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pridentifier"))
        self.label.setText(_translate("MainWindow", "Training method: "))
        self.dropdown_dataMethod.setItemText(0, _translate("MainWindow", "FFT Fingerprint"))
        self.dropdown_dataMethod.setItemText(1, _translate("MainWindow", "images only"))
        self.button_loadData.setText(_translate("MainWindow", "LOAD"))
        self.button_exportData.setText(_translate("MainWindow", "export data"))
        self.button_importData.setText(_translate("MainWindow", "import data"))
        self.label_2.setText(_translate("MainWindow", "Loading:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_data), _translate("MainWindow", "Data"))
        self.button_train.setText(_translate("MainWindow", "TRAIN"))
        self.button_exportKnowledge.setText(_translate("MainWindow", "export knowledge"))
        self.button_importKnowledge.setText(_translate("MainWindow", "import knowledge"))
        self.label_7.setText(_translate("MainWindow", "Training:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_learning), _translate("MainWindow", "Learning"))
        self.button_evaluate.setText(_translate("MainWindow", "EVALUATE"))
        self.button_saveStatistics.setText(_translate("MainWindow", "save statistics"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_evaluation), _translate("MainWindow", "Evaluation"))
        self.button_loadImage.setText(_translate("MainWindow", "LOAD IMAGE"))
        self.button_inspect.setText(_translate("MainWindow", "INSPECT"))
        self.button_saveResults.setText(_translate("MainWindow", "save results"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_inspection), _translate("MainWindow", "Inspection"))
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





    def showFingerprints(self):

        qimg_1 = QtGui.QImage()
        qimg_2 = QtGui.QImage()
        qimg_3 = QtGui.QImage()
        qimg_4 = QtGui.QImage()

        filename_1 = ROOTDIR + "/../../fingerprints/Brother_merged_multi.png"
        filename_2 = ROOTDIR + "/../../fingerprints/Canon_MX870_merged_multi.png"
        filename_3 = ROOTDIR + "/../../fingerprints/Canon_Pro_merged_multi.png"
        filename_4 = ROOTDIR + "/../../fingerprints/HP_merged_multi.png"

        qimg_1.load(filename_1)
        qimg_2.load(filename_2)
        qimg_3.load(filename_3)
        qimg_4.load(filename_4)

        # Create widget
        fingerprint_1 = QPixmap.fromImage(qimg_1)
        fingerprint_2 = QPixmap.fromImage(qimg_2)
        fingerprint_3 = QPixmap.fromImage(qimg_3)
        fingerprint_4 = QPixmap.fromImage(qimg_4)


        self.label_evaluation1.setPixmap(fingerprint_1.scaled(
            self.label_evaluation1.size(), QtCore.Qt.KeepAspectRatio,
            QtCore.Qt.SmoothTransformation))
        self.label_evaluation2.setPixmap(fingerprint_2.scaled(
            self.label_evaluation2.size(), QtCore.Qt.KeepAspectRatio,
            QtCore.Qt.SmoothTransformation))
        self.label_evaluation3.setPixmap(fingerprint_3.scaled(
            self.label_evaluation3.size(), QtCore.Qt.KeepAspectRatio,
            QtCore.Qt.SmoothTransformation))
        self.label_evaluation4.setPixmap(fingerprint_4.scaled(
            self.label_evaluation4.size(), QtCore.Qt.KeepAspectRatio,
            QtCore.Qt.SmoothTransformation))

        self.label_evaluation1_text.setText("Brother")
        self.label_evaluation2_text.setText("Canon_MX870")
        self.label_evaluation3_text.setText("Canon_Pro")
        self.label_evaluation4_text.setText("HP")


    def loadData(self):
        # print(DIRS)
        #filter = "Folder with folders representing each class (*.*)"
        dialog = QtWidgets.QFileDialog()
        path = dialog.getExistingDirectory(directory='..', options=QtWidgets.QFileDialog.ShowDirsOnly)

        if path:
            self.inspector.loadData(path)
            self.progressBar_loadingData.setValue(100)

            # numbers of loaded data
            self.loadTable(self.tableWidget_data)

    def loadTable(self, tableWidget):
        tableWidget.setRowCount(3)
        # set column count
        tableWidget.setColumnCount(int(len(self.inspector.printer_types)))

        #name columns
        for i in range(len(self.inspector.printer_types)):
            tableWidget.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(self.inspector.printer_types[i]))
        tableWidget.resizeColumnsToContents()

        #col = []
        #col.append('number of documents')
        #col.append('segments:')

        # name rows
        #for i in range(len(col)):
        tableWidget.setRowCount(1)
        tableWidget.setVerticalHeaderItem(0, QtWidgets.QTableWidgetItem('segments:'))

        # compute and write stats for every printer
        for i in range(len(self.inspector.printer_types)):
            #tableWidgeta.setItem(0,i, QtWidgets.QTableWidgetItem(str(self.inspector.data_detailed.shape[0]) + "segments"))
            tableWidget.setItem(0,i, QtWidgets.QTableWidgetItem(str(int(self.inspector.data_detailed.shape[0]/4)))) #ToDo: check segment amount per printer

    def saveSpectra(self):

        self.inspector.saveSpectra()

    def getSpectra(self):
        filter = "Folder which contains the data_detailed.pkl and data_merged.pkl files. (*.*)"
        path = QtWidgets.QFileDialog.getExistingDirectory(directory='..', options=QtWidgets.QFileDialog.ShowDirsOnly)
        print('selected path to get data: ', path)

        if path:
            self.inspector.getSpectra(path)
            self.progressBar_loadingData.setValue(100)
            self.loadTable(self.tableWidget_data)


    def training(self):

        self.inspector.training()
        self.progressBar_loadingTraining.setValue(100)
        self.tableWidget_learning

    def getCorrelation(self):

        filter = "Folder which contains the data_detailed.pkl and data_merged.pkl files. (*.*)"
        path = QtWidgets.QFileDialog.getExistingDirectory(directory='..', options=QtWidgets.QFileDialog.ShowDirsOnly)
        #path = "/Users/resa/Projekte/Korensics/02-Pridentifier/generated_data"
        print('selected path to get data: ', path)

        if path:
            self.inspector.getCorrelation(path)
            self.progressBar_loadingTraining.setValue(100)
            self.loadTable(self.tableWidget_learning)



    def saveCorrelation(self):

        self.inspector.saveCorrelation()


    def showStat(self):

        self.showFingerprints()
        newstr = []

        if add_all_fft:
            col = []
            col.append('true positive')
            col.append('false negative')
            #col.append('fall out')
            col.append('accuracy')
            #col.append('failure')
            col.append('printer')

            #self.tableWidget = QTableWidget()
            # set row count
            self.tableWidget_evaluation.setRowCount(int(len(col)-1))
            # set column count
            self.tableWidget_evaluation.setColumnCount(int(len(self.inspector.printer_types)))


            # name columns
            for i in range(len(self.inspector.printer_types)):
                self.tableWidget_evaluation.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(self.inspector.printer_types[i]))
            self.tableWidget_evaluation.resizeColumnsToContents()

            # name rows
            for i in range(len(col)-1):
                self.tableWidget_evaluation.setVerticalHeaderItem(i, QtWidgets.QTableWidgetItem(col[i]))

            # compute and write stats for every printer
            for i in range(len(self.inspector.printer_types)):
                amount_pos = self.inspector.correctPositiveTrain[i] + self.inspector.falseNegativeTrain[i]
                amount_neg = self.inspector.correctNegativeTrain[i] + self.inspector.falsePositiveTrain[i]
                amount_all = amount_neg + amount_pos

                true_positive = 100*self.inspector.correctPositiveTrain[i] / amount_pos
                miss_rate = 100*self.inspector.falseNegativeTrain[i] / amount_pos
                #fall_out = 100*self.inspector.falsePositiveTrain[i] / (self.inspector.falsePositiveTrain[i] + self.inspector.correctNegativeTrain[i])
                accuracy = 100*(self.inspector.correctPositiveTrain[i]+self.inspector.correctNegativeTrain[i]) / amount_all
                #failure = 100*(self.inspector.falsePositiveTrain[i] + self.inspector.falseNegativeTrain[i]) / amount_all

                self.tableWidget_evaluation.setItem(0,i, QtWidgets.QTableWidgetItem(str(true_positive) + "%"))
                self.tableWidget_evaluation.setItem(1,i, QtWidgets.QTableWidgetItem(str(miss_rate) + "%"))
                #self.tableWidget_evaluation.setItem(2,i, QtWidgets.QTableWidgetItem(str(fall_out) + "%"))
                self.tableWidget_evaluation.setItem(2,i, QtWidgets.QTableWidgetItem(str(accuracy) + "%"))
                #self.tableWidget_evaluation.setItem(4,i, QtWidgets.QTableWidgetItem(str(failure) + "%"))



    def saveStat(self):

        if add_all_fft:

            statistics = pd.DataFrame(columns=col)

            for i in range(0, len(self.inspector.printer_types)):
                #print("TRAIN SET")
                amount_pos = self.inspector.correctPositiveTrain[i] + self.inspector.falseNegativeTrain[i]
                amount_neg = self.inspector.correctNegativeTrain[i] + self.inspector.falsePositiveTrain[i]
                amount_all = amount_neg + amount_pos

                true_positive = 100*self.inspector.correctPositiveTrain[i] / amount_pos
                miss_rate = 100*self.inspector.falseNegativeTrain[i] / amount_pos
                #fall_out = 100*self.inspector.falsePositiveTrain[i] / (self.inspector.falsePositiveTrain[i] + self.inspector.correctNegativeTrain[i])
                accuracy = 100*(self.inspector.correctPositiveTrain[i]+self.inspector.correctNegativeTrain[i]) / amount_all
                #failure = 100*(self.inspector.falsePositiveTrain[i] + self.inspector.falseNegativeTrain[i]) / amount_all

                # print(self.inspector.printer_types[i], "############################")
                print("Hit Rate: %d %s" % (true_positive, "%"))
                print("Miss Rate: %d %s" % (miss_rate, "%"))
                #print("Fallout: %d %s" % (fall_out, "%"))
                print("-------------------------------")
                print("Accuracy: %d %s" % (accuracy, "%"))
                #print("Classification Failure: %d %s" % (failure, "%"))

                statistics.loc[i] = np.array([true_positive,miss_rate,accuracy,self.inspector.printer_types[i]])

            statistics.to_pickle(SUBPATH+"/statistics.pkl")
                #line6 = "TEST SET"
                #line7 = self.inspector.printer_types[i]
                #line111 = "Hit Rate: %d %s" % (100*correctPositiveTest[i] / (correctPositiveTest[i] + falseNegativeTest[i]), "%")
                #line112 = "Accuracy: %d %s" % (100*correctPositiveTest[i] / (correctPositiveTest[i] + falsePositiveTest[i]), "%")
                #line113 = "Fallout: %d %s" % (100*falsePositiveTest[i] / (falsePositiveTest[i] + correctNegativeTest[i]), "%")
                #newstr.append("\n".join(("                                                            ".join((line0)),"                                                            ".join((line1)),"          ".join((line2)),"         ".join((line3)),"                    ".join((line4)),"                    ".join((line5)),"                                                        ".join((line6)),"                                                        ".join((line7)))))



    def loadImg(self):

        filename = QtWidgets.QFileDialog.getOpenFileName(filter='Images (*.png *.xpm *.jpg)')
        #filename = "/Users/resa/Projekte/Korensics/02-Pridentifier/data/images/id_mini/HP/idcard_11.jpg"
        #print("load from ", filename)

        if filename:
            questioned_image = self.inspector.loadImg(filename)

            # Create widget
            if questioned_image:
                pixmap = QPixmap.fromImage(questioned_image)
                #self.label_inspection.setPixmap(pixmap)
                #self.label_inspection.setScaledContents(True)
                self.label_inspection.setPixmap(pixmap.scaled(
                    self.label_inspection.size(), QtCore.Qt.KeepAspectRatio,
                    QtCore.Qt.SmoothTransformation))

                self.label_inspection.setAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget_inspection.clear()
                #self.inspection()



    def inspection(self):

        hitsPerClassOfInspectedSegments = self.inspector.inspection()

        if hitsPerClassOfInspectedSegments:
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
            self.tableWidget_inspection.setColumnCount(int(len(self.inspector.printer_types)))


            # name columns
            for i in range(len(self.inspector.printer_types)):
                self.tableWidget_inspection.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(self.inspector.printer_types[i]))
            self.tableWidget_inspection.resizeColumnsToContents()

            # name rows
            for i in range(len(col)):
                self.tableWidget_inspection.setVerticalHeaderItem(i, QtWidgets.QTableWidgetItem(col[i]))

            all_seg = np.sum(np.sum(hitsPerClassOfInspectedSegments))
            # compute and write stats for every printer
            for i in range(len(self.inspector.printer_types)):

                self.tableWidget_inspection.setItem(0,i, QtWidgets.QTableWidgetItem(str(hitsPerClassOfInspectedSegments[i])))
                self.tableWidget_inspection.setItem(1,i, QtWidgets.QTableWidgetItem(str(hitsPerClassOfInspectedSegments[i]/all_seg *100) + "%"))



    def saveResult(self):

        self.inspector.saveResult()



def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())
    app.exit()

def code_view():

    inspects = inspector.Inspector()
    inspects.getCorrelation()
    inspects.loadImg()
    inspects.inspection()

    print("This is for testing...")
    print("This is for testing...")


if __name__ == '__main__':
    main()
    #code_view()