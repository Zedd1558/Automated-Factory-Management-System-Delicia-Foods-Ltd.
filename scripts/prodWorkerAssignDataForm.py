# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prodWorkerAssignDataForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QFileDialog
from prodWorkerAssignOutputForm import *

class Ui_prodWorkerAssignDataForm(object):
  
    def setupUi(self, prodWorkerAssignDataForm):
        self.form = prodWorkerAssignDataForm
        
        prodWorkerAssignDataForm.setObjectName("prodWorkerAssignDataForm")
        prodWorkerAssignDataForm.resize(860, 599)
        prodWorkerAssignDataForm.setMinimumSize(QtCore.QSize(860, 599))
        prodWorkerAssignDataForm.setMaximumSize(QtCore.QSize(860, 599))
        prodWorkerAssignDataForm.setStyleSheet("background-color : rgb(231, 249, 255)")
        self.logo = QtWidgets.QLabel(prodWorkerAssignDataForm)
        self.logo.setGeometry(QtCore.QRect(380, 0, 101, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../resource/deliciaLogo100.png"))
        self.logo.setObjectName("logo")
        self.title = QtWidgets.QLabel(prodWorkerAssignDataForm)
        self.title.setGeometry(QtCore.QRect(40, 90, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color : rgb(113, 0, 113)")
        self.title.setObjectName("title")
        self.helpBtn = QtWidgets.QPushButton(prodWorkerAssignDataForm)
        self.helpBtn.setGeometry(QtCore.QRect(800, 20, 31, 31))
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
        self.backBtn = QtWidgets.QPushButton(prodWorkerAssignDataForm)
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
        self.textEdit = QtWidgets.QTextEdit(prodWorkerAssignDataForm)
        self.textEdit.setGeometry(QtCore.QRect(40, 140, 791, 331))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.okBtn = QtWidgets.QPushButton(prodWorkerAssignDataForm)
        self.okBtn.setGeometry(QtCore.QRect(340, 540, 151, 31))
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
        self.attachBtn = QtWidgets.QPushButton(prodWorkerAssignDataForm)
        self.attachBtn.setGeometry(QtCore.QRect(40, 490, 211, 31))
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
        self.fileNameLabel = QtWidgets.QLabel(prodWorkerAssignDataForm)
        self.fileNameLabel.setGeometry(QtCore.QRect(260, 490, 561, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.fileNameLabel.setFont(font)
        self.fileNameLabel.setStyleSheet("color : rgb(113, 0, 113)")
        self.fileNameLabel.setObjectName("fileNameLabel")

        self.retranslateUi(prodWorkerAssignDataForm)
        QtCore.QMetaObject.connectSlotsByName(prodWorkerAssignDataForm)

    def retranslateUi(self, prodWorkerAssignDataForm):
        _translate = QtCore.QCoreApplication.translate
        prodWorkerAssignDataForm.setWindowTitle(_translate("prodWorkerAssignDataForm", "set data for prodWorkerAssign.dzn"))
        self.title.setText(_translate("prodWorkerAssignDataForm", "set data for prodWorkerAssign.mzn"))
        self.helpBtn.setText(_translate("prodWorkerAssignDataForm", "?"))
        self.backBtn.setText(_translate("prodWorkerAssignDataForm", "<"))
        self.textEdit.setHtml(_translate("prodWorkerAssignDataForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto Slab\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">nprocesses = ;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">processName = [ ];</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">nworkers =  ;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">workerName = [ ];</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">% below is an array (numberOfWorkers x numberOfProcesses)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ability = [ ];  </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">% finds an assignment for next 15 days</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">nDays =  ;  </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">% minimum worker needed for each process</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">minimumWorkers = [ ]; </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.okBtn.setText(_translate("prodWorkerAssignDataForm", "done!"))
        self.attachBtn.setText(_translate("prodWorkerAssignDataForm", "Or, attach a dzn file"))
        self.fileNameLabel.setText(_translate("prodWorkerAssignDataForm", "~"))
        self.attachBtn.clicked.connect(self.openFileNameDialog )
        self.okBtn.clicked.connect(self.okBtnFunc)
        self.fileName =""

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self.form,"QFileDialog.getOpenFileName()", "","All Files (*);;dzn Files (*.dzn)", options=options)
        if self.fileName:
            print(self.fileName)
            self.fileNameLabel.setText(str(self.fileName))
            #self.textEdit.setText("")
            self.textEdit.setDisabled(True)

    def okBtnFunc(self):
        import pymzn
        
        if(self.fileName):
                #self.textEdit.setEnabled(True)
                #self.textEdit.setText(" One moment Please ...\nConnecting to Minizinc...")
                #solns = pymzn.minizinc('prodWorkerAssign.mzn', self.fileName , output_mode='item')
                fp = open("workerAssignSol.txt",'r')
                solns = fp.read()
                fp.close()

                self.prodWorkerAssignOutputf = QtWidgets.QWidget()
                self.prodWorkerAssignOutputfUi = Ui_prodWorkerAssignOutputForm()
                self.prodWorkerAssignOutputfUi.setupUi(self.prodWorkerAssignOutputf)
                self.prodWorkerAssignOutputfUi.textEdit.setText(solns)
                self.prodWorkerAssignOutputf.show()
                self.form.hide()
                pass
        else:
                pass


    def close(self):
        sys.exit()
    
