# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projectone.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore, QtGui, QtWidgets

from DetailsUI import DetailsUI
from Grammer_checkUI import Mistakes
from Plagarism_checkUI import Plagarism_c
from EssayScoreUI import Score

class Ui_MainWindow(object):
    def openwindow(self):
        self.window=DetailsUI()
        self.window.show()
       
    def openwindow2(self):
        self.window=Mistakes()
        self.window.show()

    def openwindow4(self):
        self.window=Score()
        self.window.show() 
        
    def openwindow3(self):
        self.window=Plagarism_c()
        self.window.show()
          
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(771, 611)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QWidget{\n"
"    background-color: rgb(131, 249, 255);\n"
"    \n"
"    \n"
"    background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0.0681818 rgba(38, 209, 255, 255), stop:1 rgba(91, 43, 255, 255));\n"
"}\n"
"\n"
"QPlainTextEdit{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 0, 551, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 60, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(620, 170, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Button1.setFont(font)
        self.Button1.setObjectName("Button1")

        self.Button1.clicked.connect(self.openwindow)
        
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_2.setGeometry(QtCore.QRect(620, 230, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Button_2.setFont(font)
        self.Button_2.setObjectName("Button_2")

        self.Button_2.clicked.connect(self.openwindow2)
        
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_3.setGeometry(QtCore.QRect(620, 290, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Button_3.setFont(font)
        self.Button_3.setObjectName("Button_3")

        self.Button_3.clicked.connect(self.openwindow3)
        
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_4.setGeometry(QtCore.QRect(620, 350, 111, 41))
        self.Button_4.setObjectName("Button_4")

        self.Button_4.clicked.connect(self.openwindow4)

        self.button_SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.button_SaveButton.setGeometry(QtCore.QRect(300, 550, 111, 41))
        self.button_SaveButton.setObjectName("SaveButton")

        self.button_SaveButton.clicked.connect(self.SaveEssay)
        
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 150, 591, 391))
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # self.button_SaveButton = self.centralwidget.findChild(QtWidgets.QPushButton,'SaveButton')
        # print(self.button_SaveButton)
        # self.button_SaveButton.clicked.connect(self.SaveEssay)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def SaveEssay(self):     
        Essay = self.plainTextEdit.toPlainText()
        with open('./Backend/essay.txt', 'w') as f:
            f.write(Essay)        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Automatic Essay Scorer and Recommendation"))
        self.label_2.setText(_translate("MainWindow", "Enter Your Essay"))
        self.Button1.setText(_translate("MainWindow", "get essay details"))
        self.Button_2.setText(_translate("MainWindow", "grammer check"))
        self.Button_3.setText(_translate("MainWindow", "plagarism check"))
        self.Button_4.setText(_translate("MainWindow", "Get essay score"))
        self.button_SaveButton.setText(_translate("MainWindow", "Save Essay"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "enter your essay...\n"""))
       
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
