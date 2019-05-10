# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_experimentResults.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(636, 449)
        Dialog.setStyleSheet("background-color: #222222;\n"
"")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 601, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setStyleSheet("color: #fff;\n"
"font: 12pt \"Helvetica\";\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_4.addWidget(self.textBrowser)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
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
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("color: #fff;\n"
"font: 12pt \"Helvetica\";\n"
"")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setStyleSheet("QPushButton {\n"
"background-color: #009999;\n"
"padding: 12px 16px;\n"
"border: 2px solid #fff;\n"
"color: #fff;\n"
"font: Helvetica;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #75bdc3;\n"
"}")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        self.buttonBox.clicked['QAbstractButton*'].connect(Dialog.reject)
        self.buttonBox.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Helvetica\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Experimental Results</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt;\">In our examination of 4 printers (Brother, Canon MX870, Canon Pro and one HP printer) we achieved the following accuracy and classification failure statistics. Per printer 3 different prints were used. From each print not all segments but only 210 segments of size 512x512px were used.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:13pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt;\">This results is the prediction for one snippet (512×512px). If a larger image is used, we can cut the image into several 512×512px snippets and the probability increases.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:13pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt;\">To see more about the observed data in this research study visit:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:13pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt;\">https://www.korensic.com/pridentifier</span></p></body></html>"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Accuracy"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "Classification Failure"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Brother"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Canon MX870"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Canon Pro"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "HP"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Dialog", "100%"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Dialog", "93%"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Dialog", "95%"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("Dialog", "97%"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Dialog", "0%"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("Dialog", "7%"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("Dialog", "5%"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("Dialog", "3%"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Dialog", "© 2019 Theresa Kocher"))

