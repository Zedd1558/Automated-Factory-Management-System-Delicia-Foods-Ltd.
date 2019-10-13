# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from prodPlanDataForm import *
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(940, 620)
        MainWindow.setMinimumSize(QtCore.QSize(940, 620))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("background-color : rgb(237, 248, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(210, 240, 541, 31))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color : rgb(113, 0, 113)")
        self.title.setObjectName("title")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(370, 20, 200, 185))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../resource/deliciaLogoSS.png"))
        self.logo.setObjectName("logo")
        self.manBtn = QtWidgets.QPushButton(self.centralwidget)
        self.manBtn.setGeometry(QtCore.QRect(320, 340, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.manBtn.setFont(font)
        self.manBtn.setStyleSheet("color:rgb(51, 0, 77);\n"
"background-color: rgb(234, 218, 240);\n"
"border-radius: 5;")
        self.manBtn.setObjectName("manBtn")
        self.helpBtn = QtWidgets.QPushButton(self.centralwidget)
        self.helpBtn.setGeometry(QtCore.QRect(320, 420, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.helpBtn.setFont(font)
        self.helpBtn.setStyleSheet("color:rgb(51, 0, 77);\n"
"background-color: rgb(234, 218, 240);\n"
"border-radius: 5;")
        self.helpBtn.setObjectName("helpBtn")
        self.quitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.quitBtn.setGeometry(QtCore.QRect(320, 500, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.quitBtn.setFont(font)
        self.quitBtn.setStyleSheet("color:rgb(51, 0, 77);\n"
"background-color: rgb(234, 218, 240);\n"
"border-radius: 5;")
        self.quitBtn.setObjectName("quitBtn")
        
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.manBtn.clicked.connect(self.callProdPlanData)
        self.quitBtn.clicked.connect(self.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Delicia Foods Ltd."))
        self.title.setText(_translate("MainWindow", "Automatic Factory Management System"))
        self.manBtn.setText(_translate("MainWindow", "manufacturing panel"))
        self.helpBtn.setText(_translate("MainWindow", "help"))
        self.quitBtn.setText(_translate("MainWindow", "quit"))
        



    def close(self):
        sys.exit()
    
    def callProdPlanData(self):
        self.prodPlanDataf = QtWidgets.QWidget()
        self.prodPlanDatafUi = Ui_prodPlanDataForm()
        self.prodPlanDatafUi.setupUi(self.prodPlanDataf)
        self.prodPlanDataf.show()



def main():
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
        


if __name__ == "__main__":
        main()
