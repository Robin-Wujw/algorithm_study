# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets,QtWidgets
from PyQt5.QtWidgets import QInputDialog,QMainWindow,QPushButton,QApplication
from algorithm_python import al_002
class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 220, 201, 32))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 100, 201, 32))
        self.label_2.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(370, 100, 256, 51))
        self.lineEdit_2.setObjectName("textBrowser")
        self.PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton.setGeometry(QtCore.QRect(125, 320, 150, 51))
        self.PushButton.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(370, 210, 256, 51))
        self.lineEdit.setObjectName("textBrowser")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(370, 320, 256, 51))
        self.textBrowser.setObjectName("textBrowser_2")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Quick_Sort_Experiment"))
        self.label_2.setText(_translate("MainWindow", "排序的数的个数："))
        self.label.setText(_translate("MainWindow", "快速排序的数组："))
        self.PushButton.setText(_translate("MainWindow", "结果："))

    def onChanged(self):
        number     = self.lineEdit_2.text()
        numberList = self.lineEdit.text()
        List = numberList.split(",")
        a = []
        for i in range(int(number)):
            a.append(int(List[i]))
        self.textBrowser.clear()
        self.textBrowser.append(str(al_002.Quick_Sort(a, 0, len(a) - 1)))