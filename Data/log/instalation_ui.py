# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis\instalation_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    
    def unpack_files(path):
        import json
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(628, 150)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_path_instalation = QtWidgets.QLabel(self.centralwidget)
        self.label_path_instalation.setGeometry(QtCore.QRect(20, 10, 591, 16))
        self.label_path_instalation.setObjectName("label_path_instalation")
        
        self.plainTextEdit_path_instalation = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_path_instalation.setGeometry(QtCore.QRect(20, 50, 591, 31))
        self.plainTextEdit_path_instalation.setObjectName("plainTextEdit_path_instalation")
        
        self.toolButton_find_path_instalation = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_find_path_instalation.setGeometry(QtCore.QRect(580, 50, 31, 31))
        self.toolButton_find_path_instalation.setObjectName("toolButton_find_path_instalation")
        
        self.buttonBox_instalation = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox_instalation.setGeometry(QtCore.QRect(450, 100, 156, 24))
        self.buttonBox_instalation.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_instalation.setObjectName("buttonBox_instalation")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 628, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_path_instalation.setText(_translate("MainWindow", "Escolha uma pasta onde os programas serão instalados:"))
        self.toolButton_find_path_instalation.setText(_translate("MainWindow", "..."))

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())