# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pridifiApp.ui'
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
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidget.setStyleSheet("QWidget {\n"
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
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_6.addWidget(self.listWidget)
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
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setStyleSheet("color: #fff;\n"
"font: 12pt \"Helvetica\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.spinBox.setStyleSheet("    background-color: #777777;\n"
"    min-width: 160px;\n"
"    color: #fff;\n"
"")
        self.spinBox.setMinimum(10)
        self.spinBox.setMaximum(10000)
        self.spinBox.setSingleStep(100)
        self.spinBox.setProperty("value", 1000)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_3.addWidget(self.spinBox)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setStyleSheet("color: #fff;\n"
"font: 12pt \"Helvetica\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.spinBox_2 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.spinBox_2.setStyleSheet("    background-color: #777777;\n"
"    min-width: 160px;\n"
"    color: #fff;\n"
"")
        self.spinBox_2.setMinimum(64)
        self.spinBox_2.setMaximum(1024)
        self.spinBox_2.setSingleStep(64)
        self.spinBox_2.setProperty("value", 512)
        self.spinBox_2.setObjectName("spinBox_2")
        self.verticalLayout_3.addWidget(self.spinBox_2)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
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
        self.button_exportKnowledge.setObjectName("button_exportKnowledge")
        self.verticalLayout_3.addWidget(self.button_exportKnowledge)
        self.button_importKnowledge = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.button_importKnowledge.setStyleSheet("QPushButton {\n"
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
        self.button_importKnowledge.setObjectName("button_importKnowledge")
        self.verticalLayout_3.addWidget(self.button_importKnowledge)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.listWidget_2 = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.listWidget_2.setStyleSheet("QWidget {\n"
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
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout_2.addWidget(self.listWidget_2)
        self.tabWidget.addTab(self.tab_learning, "")
        self.tab_evaluation = QtWidgets.QWidget()
        self.tab_evaluation.setObjectName("tab_evaluation")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_evaluation)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 911, 591))
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
        self.button_saveStatistics.setObjectName("button_saveStatistics")
        self.verticalLayout_4.addWidget(self.button_saveStatistics)
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
        self.tabWidget.addTab(self.tab_evaluation, "")
        self.tab_inspection = QtWidgets.QWidget()
        self.tab_inspection.setObjectName("tab_inspection")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab_inspection)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 911, 591))
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
        self.button_saveResults.setObjectName("button_saveResults")
        self.verticalLayout_5.addWidget(self.button_saveResults)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.listWidget_4 = QtWidgets.QListWidget(self.horizontalLayoutWidget_4)
        self.listWidget_4.setStyleSheet("QWidget {\n"
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
        self.listWidget_4.setObjectName("listWidget_4")
        self.horizontalLayout_4.addWidget(self.listWidget_4)
        self.tabWidget.addTab(self.tab_inspection, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 937, 22))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")
        self.menuData = QtWidgets.QMenu(self.menubar)
        self.menuData.setGeometry(QtCore.QRect(287, 139, 153, 56))
        self.menuData.setStyleSheet("background-color: #fff;\n"
"color: #000;")
        self.menuData.setObjectName("menuData")
        self.menuKnowledge = QtWidgets.QMenu(self.menubar)
        self.menuKnowledge.setStyleSheet("background-color: #fff;\n"
"color: #000;")
        self.menuKnowledge.setObjectName("menuKnowledge")
        self.menuTest = QtWidgets.QMenu(self.menubar)
        self.menuTest.setStyleSheet("background-color: #fff;\n"
"color: #000;")
        self.menuTest.setObjectName("menuTest")
        self.menuInspection = QtWidgets.QMenu(self.menubar)
        self.menuInspection.setStyleSheet("background-color: #fff;\n"
"color: #000;")
        self.menuInspection.setObjectName("menuInspection")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setStyleSheet("background-color: #fff;\n"
"color: #000;")
        self.menuAbout.setObjectName("menuAbout")
        self.menuIntroduction = QtWidgets.QMenu(self.menubar)
        self.menuIntroduction.setStyleSheet("background-color: #fff;\n"
"color: #000;")
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
        self.actionGeneral_Purpose = QtWidgets.QAction(MainWindow)
        self.actionGeneral_Purpose.setObjectName("actionGeneral_Purpose")
        self.actionData = QtWidgets.QAction(MainWindow)
        self.actionData.setObjectName("actionData")
        self.actionAnalysis = QtWidgets.QAction(MainWindow)
        self.actionAnalysis.setObjectName("actionAnalysis")
        self.actionEvaluation = QtWidgets.QAction(MainWindow)
        self.actionEvaluation.setObjectName("actionEvaluation")
        self.actionInspection = QtWidgets.QAction(MainWindow)
        self.actionInspection.setObjectName("actionInspection")
        self.actionUse_Case = QtWidgets.QAction(MainWindow)
        self.actionUse_Case.setObjectName("actionUse_Case")
        self.actionOther_Use_Cases = QtWidgets.QAction(MainWindow)
        self.actionOther_Use_Cases.setObjectName("actionOther_Use_Cases")
        self.actionInstruction = QtWidgets.QAction(MainWindow)
        self.actionInstruction.setObjectName("actionInstruction")
        self.actionResearch = QtWidgets.QAction(MainWindow)
        self.actionResearch.setObjectName("actionResearch")
        self.actionInterpretation = QtWidgets.QAction(MainWindow)
        self.actionInterpretation.setObjectName("actionInterpretation")
        self.actionResult = QtWidgets.QAction(MainWindow)
        self.actionResult.setObjectName("actionResult")
        self.actionResult_2 = QtWidgets.QAction(MainWindow)
        self.actionResult_2.setObjectName("actionResult_2")
        self.actionInteraction = QtWidgets.QAction(MainWindow)
        self.actionInteraction.setObjectName("actionInteraction")
        self.actionCredits = QtWidgets.QAction(MainWindow)
        self.actionCredits.setObjectName("actionCredits")
        self.actionDevelopment = QtWidgets.QAction(MainWindow)
        self.actionDevelopment.setObjectName("actionDevelopment")
        self.actionLicence = QtWidgets.QAction(MainWindow)
        self.actionLicence.setObjectName("actionLicence")
        self.actionIdea = QtWidgets.QAction(MainWindow)
        self.actionIdea.setObjectName("actionIdea")
        self.actionFeedback = QtWidgets.QAction(MainWindow)
        self.actionFeedback.setObjectName("actionFeedback")
        self.actionTroubleshooting = QtWidgets.QAction(MainWindow)
        self.actionTroubleshooting.setObjectName("actionTroubleshooting")
        self.actionContact = QtWidgets.QAction(MainWindow)
        self.actionContact.setObjectName("actionContact")
        self.menuData.addAction(self.actionload)
        self.menuKnowledge.addAction(self.actionInstruction)
        self.menuKnowledge.addAction(self.actionResearch)
        self.menuTest.addAction(self.actionevaluate)
        self.menuInspection.addAction(self.actionInteraction)
        self.menuAbout.addAction(self.actionDevelopment)
        self.menuAbout.addAction(self.actionCredits)
        self.menuAbout.addAction(self.actionLicence)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionFeedback)
        self.menuAbout.addAction(self.actionTroubleshooting)
        self.menuAbout.addAction(self.actionContact)
        self.menuIntroduction.addAction(self.actionUse_Case)
        self.menuIntroduction.addSeparator()
        self.menuIntroduction.addAction(self.actionGeneral_Purpose)
        self.menuIntroduction.addAction(self.actionOther_Use_Cases)
        self.menubar.addAction(self.menuIntroduction.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuKnowledge.menuAction())
        self.menubar.addAction(self.menuTest.menuAction())
        self.menubar.addAction(self.menuInspection.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        self.button_loadData.clicked.connect(MainWindow.loadData)
        self.button_evaluate.clicked.connect(MainWindow.showStat)
        self.button_loadImage.clicked.connect(MainWindow.loadImg)
        self.button_importKnowledge.clicked.connect(MainWindow.getCorrelation)
        self.button_exportKnowledge.clicked.connect(MainWindow.saveCorrelation)
        self.button_saveStatistics.clicked.connect(MainWindow.saveStat)
        self.button_saveResults.clicked.connect(MainWindow.saveResult)
        self.button_train.clicked.connect(MainWindow.training)
        self.button_inspect.clicked.connect(MainWindow.inspection)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pridentifier"))
        self.button_loadData.setText(_translate("MainWindow", "LOAD"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_data), _translate("MainWindow", "Data"))
        self.label_2.setText(_translate("MainWindow", "Feature count:"))
        self.label_3.setText(_translate("MainWindow", "Segment width:"))
        self.button_train.setText(_translate("MainWindow", "ANALYZE"))
        self.button_exportKnowledge.setText(_translate("MainWindow", "export analysis"))
        self.button_importKnowledge.setText(_translate("MainWindow", "import analysis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_learning), _translate("MainWindow", "Analysis"))
        self.button_evaluate.setText(_translate("MainWindow", "EVALUATE"))
        self.button_saveStatistics.setText(_translate("MainWindow", "save statistics"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_evaluation), _translate("MainWindow", "Evaluation"))
        self.button_loadImage.setText(_translate("MainWindow", "LOAD IMAGE"))
        self.button_inspect.setText(_translate("MainWindow", "INSPECT"))
        self.button_saveResults.setText(_translate("MainWindow", "save results"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_inspection), _translate("MainWindow", "Inspection"))
        self.menuData.setTitle(_translate("MainWindow", "Data"))
        self.menuKnowledge.setTitle(_translate("MainWindow", "Analysis"))
        self.menuTest.setTitle(_translate("MainWindow", "Evaluation"))
        self.menuInspection.setTitle(_translate("MainWindow", "Inspection"))
        self.menuAbout.setTitle(_translate("MainWindow", "Info"))
        self.menuIntroduction.setTitle(_translate("MainWindow", "Instruction"))
        self.actionload.setText(_translate("MainWindow", "Usage"))
        self.actionimport.setText(_translate("MainWindow", "import data"))
        self.actiontrain.setText(_translate("MainWindow", "train"))
        self.actionimport_2.setText(_translate("MainWindow", "import knowledge"))
        self.actionevaluate.setText(_translate("MainWindow", "Usage"))
        self.actionload_document.setText(_translate("MainWindow", "load image"))
        self.actioninspect.setText(_translate("MainWindow", "inspect"))
        self.actionGeneral_Purpose.setText(_translate("MainWindow", "Purpose"))
        self.actionData.setText(_translate("MainWindow", "Data"))
        self.actionAnalysis.setText(_translate("MainWindow", "Analysis"))
        self.actionEvaluation.setText(_translate("MainWindow", "Evaluation"))
        self.actionInspection.setText(_translate("MainWindow", "Inspection"))
        self.actionUse_Case.setText(_translate("MainWindow", "Example"))
        self.actionOther_Use_Cases.setText(_translate("MainWindow", "Other Use Cases"))
        self.actionInstruction.setText(_translate("MainWindow", "Uasge"))
        self.actionResearch.setText(_translate("MainWindow", "Method"))
        self.actionInterpretation.setText(_translate("MainWindow", "Interpretation"))
        self.actionResult.setText(_translate("MainWindow", "Result"))
        self.actionResult_2.setText(_translate("MainWindow", "Result"))
        self.actionInteraction.setText(_translate("MainWindow", "Usage"))
        self.actionCredits.setText(_translate("MainWindow", "Credits"))
        self.actionDevelopment.setText(_translate("MainWindow", "Development"))
        self.actionLicence.setText(_translate("MainWindow", "Licence"))
        self.actionIdea.setText(_translate("MainWindow", "Idea"))
        self.actionFeedback.setText(_translate("MainWindow", "Feedback"))
        self.actionTroubleshooting.setText(_translate("MainWindow", "Troubleshooting"))
        self.actionContact.setText(_translate("MainWindow", "Contact"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

