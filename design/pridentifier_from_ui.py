# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pridentifier.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
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
        self.menuData.setStyleSheet("background-color: #fff;\n"
"color: #393939;")
        self.menuData.setObjectName("menuData")
        self.menuAnalysis = QtWidgets.QMenu(self.menubar)
        self.menuAnalysis.setStyleSheet("background-color: #fff;\n"
"color: #393939;")
        self.menuAnalysis.setObjectName("menuAnalysis")
        self.menuTest = QtWidgets.QMenu(self.menubar)
        self.menuTest.setStyleSheet("background-color: #fff;\n"
"color: #393939;")
        self.menuTest.setObjectName("menuTest")
        self.menuInspection = QtWidgets.QMenu(self.menubar)
        self.menuInspection.setStyleSheet("background-color: #fff;\n"
"color: #393939;")
        self.menuInspection.setObjectName("menuInspection")
        self.menuInfo = QtWidgets.QMenu(self.menubar)
        self.menuInfo.setStyleSheet("background-color: #fff;\n"
"color: #393939;")
        self.menuInfo.setObjectName("menuInfo")
        self.menuIntroduction = QtWidgets.QMenu(self.menubar)
        self.menuIntroduction.setStyleSheet("background-color: #fff;\n"
"color: #393939;")
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
        self.menuData.addAction(self.actionExample)
        self.menuData.addAction(self.actionExperiment)
        self.menuAnalysis.addAction(self.actionExample_2)
        self.menuAnalysis.addAction(self.actionMethod)
        self.menuTest.addAction(self.actionExample_3)
        self.menuTest.addAction(self.actionResult)
        self.menuInspection.addAction(self.actionExample_4)
        self.menuInspection.addAction(self.actionResult_2)
        self.menuInfo.addAction(self.actionDevelopment)
        self.menuInfo.addAction(self.actionCredits)
        self.menuInfo.addAction(self.actionLicence)
        self.menuInfo.addSeparator()
        self.menuInfo.addAction(self.actionTroubleshooting)
        self.menuInfo.addAction(self.actionFeedback)
        self.menuInfo.addAction(self.actionContact)
        self.menuIntroduction.addAction(self.actionPurpose)
        self.menuIntroduction.addAction(self.actionUse_Cases)
        self.menubar.addAction(self.menuIntroduction.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuTest.menuAction())
        self.menubar.addAction(self.menuInspection.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.button_loadData.clicked.connect(MainWindow.loadData)
        self.button_evaluate.clicked.connect(MainWindow.showStat)
        self.button_loadImage.clicked.connect(MainWindow.loadImg)
        self.button_importKnowledge.clicked.connect(MainWindow.getCorrelation)
        self.button_exportKnowledge.clicked.connect(MainWindow.saveCorrelation)
        self.button_saveStatistics.clicked.connect(MainWindow.saveStat)
        self.button_saveResults.clicked.connect(MainWindow.saveResult)
        self.button_train.clicked.connect(MainWindow.training)
        self.button_inspect.clicked.connect(MainWindow.inspection)
        self.spinBox_2.valueChanged['int'].connect(MainWindow.changeSegmentSize)
        self.spinBox.valueChanged['int'].connect(MainWindow.changeFeatureCount)
        self.menubar.hovered['QAction*'].connect(self.progressBar_loadingData.reset)
        self.menubar.hovered['QAction*'].connect(self.progressBar_loadingTraining.reset)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pridentifier"))
        self.label_3.setText(_translate("MainWindow", "Segment width:"))
        self.button_loadData.setText(_translate("MainWindow", "LOAD"))
        self.label_2.setText(_translate("MainWindow", "Loading:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_data), _translate("MainWindow", "Data"))
        self.label.setText(_translate("MainWindow", "Feature count:"))
        self.button_train.setText(_translate("MainWindow", "ANALYZE"))
        self.button_importKnowledge.setText(_translate("MainWindow", "import analysis"))
        self.button_exportKnowledge.setText(_translate("MainWindow", "export analysis"))
        self.label_7.setText(_translate("MainWindow", "Training:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_learning), _translate("MainWindow", "Analysis"))
        self.button_evaluate.setText(_translate("MainWindow", "EVALUATE"))
        self.button_saveStatistics.setText(_translate("MainWindow", "save statistics"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_evaluation), _translate("MainWindow", "Evaluation"))
        self.button_loadImage.setText(_translate("MainWindow", "LOAD IMAGE"))
        self.button_inspect.setText(_translate("MainWindow", "INSPECT"))
        self.button_saveResults.setText(_translate("MainWindow", "save results"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_inspection), _translate("MainWindow", "Inspection"))
        self.menuData.setTitle(_translate("MainWindow", "Data"))
        self.menuAnalysis.setTitle(_translate("MainWindow", "Analysis"))
        self.menuTest.setTitle(_translate("MainWindow", "Evaluation"))
        self.menuInspection.setTitle(_translate("MainWindow", "Inspection"))
        self.menuInfo.setTitle(_translate("MainWindow", "Info"))
        self.menuIntroduction.setTitle(_translate("MainWindow", "Instruction"))
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

