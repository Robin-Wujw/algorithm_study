# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '首页.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
from algorithm_python import al_001,al_002,al_004,al_005
from UI import pyqt5_1,pyqt5_2,pyqt5_4,pyqt5_5
class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Ui_for_algorithm")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 80, 136, 44))
        self.pushButton.setObjectName("fibonacci")
        self.pushButton.clicked.connect(self.on_click)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 180, 136, 44))
        self.pushButton_2.setObjectName("QuickSort")
        self.pushButton_2.clicked.connect(self.on_click2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 280, 136, 44))
        self.pushButton_3.setObjectName("Convex Hull")
        self.pushButton_3.clicked.connect(self.on_click3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 380, 136, 44))
        self.pushButton_4.setObjectName("Prim_tree")
        self.pushButton_4.clicked.connect(self.on_click4)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(310, 480, 136, 44))
        self.pushButton_5.setObjectName("Dynamic_Programming")
        self.pushButton_5.clicked.connect(self.on_click5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 38))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UI_for_algorithm"))
        self.pushButton.setText(_translate("MainWindow", "fibonacci"))
        self.pushButton_2.setText(_translate("MainWindow", "QuickSort"))
        self.pushButton_3.setText(_translate("MainWindow", "Convex Hull"))
        self.pushButton_4.setText(_translate("MainWindow", "Prim_tree"))
        self.pushButton_5.setText(_translate("MainWindow", "Dynamic_Programming"))
    windowList = []
    def on_click(self):
        the_window = pyqt5_1.Dialog1()
        self.windowList.append(the_window)
        ua = pyqt5_1.Dialog1()
        ua.setupUi(the_window)
        the_window.show()
    def on_click2(self):
        the_window = pyqt5_2.Ui_MainWindow()
        self.windowList.append(the_window)
        ub = pyqt5_2.Ui_MainWindow()
        ub.setupUi(the_window)
        self.close()
        the_window.show()
    def on_click3(self):
        al_003.main()
    def on_click4(self):
        the_window = pyqt5_4.Ui_MainWindow()
        self.windowList.append(the_window)
        uc = pyqt5_4.Ui_MainWindow()
        uc.setupUi(the_window)
        self.close()
        the_window.show()
    def on_click5(self):
        the_window = pyqt5_5.Ui_MainWindow()
        self.windowList.append(the_window)
        ud = pyqt5_5.Ui_MainWindow()
        ud.setupUi(the_window)
        self.close()
        the_window.show()
