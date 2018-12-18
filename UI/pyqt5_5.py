# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets,QtWidgets
from PyQt5.QtWidgets import QInputDialog,QMainWindow,QPushButton,QApplication
from algorithm_python import al_005
class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 190, 171, 32))
        self.label.setObjectName("label")
        self.LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEdit.setGeometry(QtCore.QRect(335, 170, 261, 61))
        self.LineEdit.setObjectName("textBrowser")
        self.PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton.setGeometry(QtCore.QRect(145, 360, 120, 45))
        self.PushButton.setObjectName("label_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(340, 350, 251, 61))
        self.textBrowser_2.setObjectName("textBrowser_2")
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
        self.PushButton.clicked.connect(self.onChanged)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dynamic_Programming_Experiment"))
        self.label.setText(_translate("MainWindow", "输入的数组："))
        self.PushButton.setText(_translate("MainWindow", "结果："))

    def onChanged(self):
        numberList = self.LineEdit.text()
        List = numberList.split(",")
        number =len(List)
        a = []
        for i in range(int(number)):
            a.append(int(List[i]))
        self.textBrowser_2.clear()
        self.textBrowser_2.append(str(al_005.MAXL(a)))