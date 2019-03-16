from PyQt5 import QtGui, QtCore, QtWidgets
import os
import time


class MainWindow(QtWidgets):
    i = 0
    style ='''
    QProgressBar
    {
        border: 2px solid grey;
        border-radius: 5px;
        text-align: center;
    }
    '''

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        grid = QtGui.QGridLayout()

        self.bar = QtGui.QProgressBar()
        self.bar.setMaximum(1)
        self.bar.setMinimum(0)

        self.bar.setStyleSheet(self.style)
        self.bar.setFormat("Custom %v units %p % %m ticks")

        self.setCentralWidget(self.bar)


        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(500) # update every 0.5 sec

    def update(self):
        print(self.i)
        self.i += 1
        self.i %= 2
        self.bar.setValue(self.i)


if __name__ == '__main__':
    app = QtGui.QApplication([])
    win = MainWindow()
    win.show();
    QtGui.QApplication.instance().exec_()