#! /usr/bin/python3
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget
from UI import  pyqt5,pyqt5_1,pyqt5_2,pyqt5_4,pyqt5_5
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_mainwindow = pyqt5.QMainWindow()
    ui = pyqt5.Ui_MainWindow()
    ui.setupUi(the_mainwindow)
    the_mainwindow.show()
    sys.exit(app.exec_())
