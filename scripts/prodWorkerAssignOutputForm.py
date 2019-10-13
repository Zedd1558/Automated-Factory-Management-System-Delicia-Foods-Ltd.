# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prodWorkerAssignOutputForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class Ui_prodWorkerAssignOutputForm(object):
    def setupUi(self, prodWorkerAssignOutputForm):
        self.form = prodWorkerAssignOutputForm
        prodWorkerAssignOutputForm.setObjectName("prodWorkerAssignOutputForm")
        prodWorkerAssignOutputForm.resize(900, 616)
        prodWorkerAssignOutputForm.setMinimumSize(QtCore.QSize(860, 616))
        prodWorkerAssignOutputForm.setMaximumSize(QtCore.QSize(900, 660))
        prodWorkerAssignOutputForm.setStyleSheet("background-color : rgb(231, 249, 255)")
        self.logo = QtWidgets.QLabel(prodWorkerAssignOutputForm)
        self.logo.setGeometry(QtCore.QRect(360, 0, 101, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../resource/deliciaLogo100.png"))
        self.logo.setObjectName("logo")
        self.title = QtWidgets.QLabel(prodWorkerAssignOutputForm)
        self.title.setGeometry(QtCore.QRect(50, 100, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color : rgb(113, 0, 113)")
        self.title.setObjectName("title")
        self.helpBtn = QtWidgets.QPushButton(prodWorkerAssignOutputForm)
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
        self.backBtn = QtWidgets.QPushButton(prodWorkerAssignOutputForm)
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
        self.textEdit = QtWidgets.QTextEdit(prodWorkerAssignOutputForm)
        self.textEdit.setGeometry(QtCore.QRect(50, 150, 791, 337))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textEdit.setObjectName("textEdit")
        self.okBtn = QtWidgets.QPushButton(prodWorkerAssignOutputForm)
        self.okBtn.setGeometry(QtCore.QRect(280, 540, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.okBtn.setFont(font)
        self.okBtn.setStyleSheet("color:rgb(51, 0, 77);\n"
"background-color: rgb(234, 218, 240);\n"
"border-radius: 5;")
        self.okBtn.setObjectName("okBtn")

        self.retranslateUi(prodWorkerAssignOutputForm)
        QtCore.QMetaObject.connectSlotsByName(prodWorkerAssignOutputForm)

    def retranslateUi(self, prodWorkerAssignOutputForm):
        _translate = QtCore.QCoreApplication.translate
        prodWorkerAssignOutputForm.setWindowTitle(_translate("prodWorkerAssignOutputForm", "ouptut of prodWorkerAssign.mzn"))
        self.title.setText(_translate("prodWorkerAssignOutputForm", "Output of prodWorkerAssign.mzn"))
        self.helpBtn.setText(_translate("prodWorkerAssignOutputForm", "?"))
        self.backBtn.setText(_translate("prodWorkerAssignOutputForm", "<"))
        self.textEdit.setHtml(_translate("prodWorkerAssignOutputForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto Slab\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.okBtn.setText(_translate("prodWorkerAssignOutputForm", "OK"))
        self.okBtn.clicked.connect(self.close)
    def close(self):
        self.form.hide()