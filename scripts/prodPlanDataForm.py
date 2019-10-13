# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prodPlanDataForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from prodPlanOutputForm import *

import sys
class Ui_prodPlanDataForm(object):
    def setupUi(self, prodPlanDataForm):
        self.form = prodPlanDataForm
        prodPlanDataForm.setObjectName("prodPlanDataForm")
        prodPlanDataForm.resize(860, 599)
        prodPlanDataForm.setMinimumSize(QtCore.QSize(860, 599))
        prodPlanDataForm.setMaximumSize(QtCore.QSize(860, 599))
        prodPlanDataForm.setStyleSheet("background-color : rgb(231, 249, 255)")
        self.logo = QtWidgets.QLabel(prodPlanDataForm)
        self.logo.setGeometry(QtCore.QRect(360, 0, 101, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../resource/deliciaLogo100.png"))
        self.logo.setObjectName("logo")
        self.title = QtWidgets.QLabel(prodPlanDataForm)
        self.title.setGeometry(QtCore.QRect(40, 90, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color : rgb(113, 0, 113)")
        self.title.setObjectName("title")
        self.helpBtn = QtWidgets.QPushButton(prodPlanDataForm)
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
        self.backBtn = QtWidgets.QPushButton(prodPlanDataForm)
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
        self.textEdit = QtWidgets.QTextEdit(prodPlanDataForm)
        self.textEdit.setGeometry(QtCore.QRect(40, 140, 791, 331))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.okBtn = QtWidgets.QPushButton(prodPlanDataForm)
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
        self.attachBtn = QtWidgets.QPushButton(prodPlanDataForm)
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
        self.fileNameLabel = QtWidgets.QLabel(prodPlanDataForm)
        self.fileNameLabel.setGeometry(QtCore.QRect(260, 490, 561, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.fileNameLabel.setFont(font)
        self.fileNameLabel.setStyleSheet("color : rgb(113, 0, 113)")
        self.fileNameLabel.setObjectName("fileNameLabel")

        self.retranslateUi(prodPlanDataForm)
        QtCore.QMetaObject.connectSlotsByName(prodPlanDataForm)

    def retranslateUi(self, prodPlanDataForm):
        _translate = QtCore.QCoreApplication.translate
        prodPlanDataForm.setWindowTitle(_translate("prodPlanDataForm", "set product data"))
        self.title.setText(_translate("prodPlanDataForm", "set data for prodPlan.mzn"))
        self.helpBtn.setText(_translate("prodPlanDataForm", "?"))
        self.backBtn.setText(_translate("prodPlanDataForm", "<"))
        self.textEdit.setHtml(_translate("prodPlanDataForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto Slab\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">nproducts =  ;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">profit = [ ];</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">demand = [ ];</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">penalty = [ ];</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">productName = [ ];</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">itemsPerBatch = [ ];</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">minimumProduce = [ ];</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">nresources = ;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">budgetForResources = ;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">resourceName = [ ];</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">resourceCost = [ ]; </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">consumption = [ ];</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">               </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">maxNumOfBatches =  ;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
        self.okBtn.setText(_translate("prodPlanDataForm", "done!"))
        self.attachBtn.setText(_translate("prodPlanDataForm", "Or, attach a dzn file"))
        self.fileNameLabel.setText(_translate("prodPlanDataForm", "~"))
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
                solns = pymzn.minizinc('prodPlan.mzn', self.fileName , output_mode='dict')
                
                strOutput = ""
                for key, value in solns[0].items():
                        s = '{} = {};\n'.format(key, value)
                        strOutput += s    
                produceList = solns[0]['produce']           
                self.prodPlanOutputf = QtWidgets.QWidget()
                self.prodPlanOutputfUi = Ui_prodPlanOutputForm()
                self.prodPlanOutputfUi.setupUi(self.prodPlanOutputf , produceList)
                self.prodPlanOutputfUi.textEdit.setText(strOutput)
                self.prodPlanOutputf.show()
                self.form.hide()
                pass
        else:
                strData = self.textEdit.toPlainText()
                fp = open("prodPlanDataAuto.dzn",'w')
                fp.write(strData)
                fp.close()
                solns = pymzn.minizinc('prodPlan.mzn',"prodPlanDataAuto.dzn" , output_mode='dict')
                strOutput = ""
                for key, value in solns[0].items():
                        s = '{} = {};\n'.format(key, value)
                        strOutput += s               
                produceList = solns[0]['produce']
                
                self.prodPlanOutputf = QtWidgets.QWidget()
                self.prodPlanOutputfUi = Ui_prodPlanOutputForm()
                self.prodPlanOutputfUi.setupUi(self.prodPlanOutputf , produceList)
                self.prodPlanOutputfUi.textEdit.setText(strOutput)
                self.prodPlanOutputf.show()
                self.form.hide()
                pass


    def close(self):
        sys.exit()
    