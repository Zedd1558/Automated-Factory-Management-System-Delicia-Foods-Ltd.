# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prodScheOutputForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QFileDialog
from prodWorkerAssignDataForm import *

class Ui_prodScheOutputForm(object):
    def setupUi(self, prodScheOutputForm):
        self.form = prodScheOutputForm
        prodScheOutputForm.setObjectName("prodScheOutputForm")
        prodScheOutputForm.resize(900, 616)
        prodScheOutputForm.setMinimumSize(QtCore.QSize(860, 616))
        prodScheOutputForm.setMaximumSize(QtCore.QSize(900, 660))
        prodScheOutputForm.setStyleSheet("background-color : rgb(231, 249, 255)")
        self.logo = QtWidgets.QLabel(prodScheOutputForm)
        self.logo.setGeometry(QtCore.QRect(360, 0, 101, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../resource/deliciaLogo100.png"))
        self.logo.setObjectName("logo")
        self.title = QtWidgets.QLabel(prodScheOutputForm)
        self.title.setGeometry(QtCore.QRect(50, 90, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color : rgb(113, 0, 113)")
        self.title.setObjectName("title")
        self.helpBtn = QtWidgets.QPushButton(prodScheOutputForm)
        self.helpBtn.setGeometry(QtCore.QRect(810, 20, 31, 31))
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
        self.backBtn = QtWidgets.QPushButton(prodScheOutputForm)
        self.backBtn.setGeometry(QtCore.QRect(40, 20, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.backBtn.setFont(font)
        self.backBtn.setStyleSheet("color:rgb(51, 0, 77);\n"
"background-color: rgb(234, 218, 240);\n"
"border-radius: 5;")
        self.backBtn.setObjectName("backBtn")
        self.textEdit = QtWidgets.QTextEdit(prodScheOutputForm)
        self.textEdit.setGeometry(QtCore.QRect(50, 150, 791, 337))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textEdit.setObjectName("textEdit")
        self.attachBtn = QtWidgets.QPushButton(prodScheOutputForm)
        self.attachBtn.setGeometry(QtCore.QRect(280, 530, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.attachBtn.setFont(font)
        self.attachBtn.setStyleSheet("color:rgb(51, 0, 77);\n"
"background-color: rgb(234, 218, 240);\n"
"border-radius: 5;")
        self.attachBtn.setObjectName("attachBtn")

        self.retranslateUi(prodScheOutputForm)
        QtCore.QMetaObject.connectSlotsByName(prodScheOutputForm)

    def retranslateUi(self, prodScheOutputForm):
        _translate = QtCore.QCoreApplication.translate
        prodScheOutputForm.setWindowTitle(_translate("prodScheOutputForm", "output of prodSchedule.mzn"))
        self.title.setText(_translate("prodScheOutputForm", "Output of prodSchedule.mzn"))
        self.helpBtn.setText(_translate("prodScheOutputForm", "?"))
        self.backBtn.setText(_translate("prodScheOutputForm", "<"))
        self.textEdit.setHtml(_translate("prodScheOutputForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto Slab\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.attachBtn.setText(_translate("prodScheOutputForm", "go to Worker Assignment  Panel"))
        self.attachBtn.clicked.connect(self.gotoWorkerAssign)
        
    def gotoWorkerAssign(self):
        self.prodWorkerAssignDataf = QtWidgets.QWidget()
        self.prodWorkerAssignDatafUi = Ui_prodWorkerAssignDataForm()
        self.prodWorkerAssignDatafUi.setupUi(self.prodWorkerAssignDataf)
        self.prodWorkerAssignDataf.show()
        self.form.hide()
        pass