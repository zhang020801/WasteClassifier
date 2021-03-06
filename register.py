# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PySide2.QtCore import QMetaObject
from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import  QPushButton, QWidget, QLabel, QWidget,QMenuBar,QStatusBar,QCheckBox,QLineEdit
from PySide2 import QtGui

import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setGeometry(150, 30, 100, 20)
        self.label_title.setObjectName("label_title")
        self.label_title.setStyleSheet('font: 20px')
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(78, 100, 72, 18)
        self.label.setObjectName("label")
        self.label.setStyleSheet('font: 18px')
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(96, 150, 54, 18)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet('font: 18px')
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setGeometry(60, 210, 90, 18)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet('font: 18px')
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setGeometry(60, 280, 90, 18)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet('font: 18px')
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setGeometry(164, 400, 72, 18)
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet('font: 18px')
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(170, 280, 72, 15)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setStyleSheet('font: 15px')
        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(260, 280, 64, 15)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.setStyleSheet('font: 15px')
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(154, 340, 93, 28)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(160, 100, 121, 20)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(160, 150, 121, 20)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(160, 200, 121, 21)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEchoMode(QLineEdit.Password)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(0, 0, 400, 26)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "??????????????????????????????"))
        self.label_title.setText(_translate("MainWindow", "???????????????"))
        self.label.setText(_translate("MainWindow", "????????????"))
        self.label_2.setText(_translate("MainWindow", "?????????"))
        self.label_3.setText(_translate("MainWindow", "???????????????"))
        self.label_4.setText(_translate("MainWindow", "???????????????"))
        self.checkBox.setText(_translate("MainWindow", "?????????"))
        self.checkBox_2.setText(_translate("MainWindow", "??????"))
        self.pushButton.setText(_translate("MainWindow", "??????"))
    
    def slot_init(self):
        self.pushButton.clicked.connect(self.finish_register)
        self.lineEdit.textChanged.connect(self.handleNameChange)
        self.lineEdit_2.textChanged.connect(self.handlePasswordChange)
        self.lineEdit_3.textChanged.connect(self.handleSurewordChange)
        self.checkBox.stateChanged.connect(self.choose)
        self.checkBox_2.stateChanged.connect(self.choose)


    def finish_register(self):
        _translate = QtCore.QCoreApplication.translate

        conn = sqlite3.connect('resident.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS user
            (name text primary key,
            password text,
            flag int )''')
        
        c.execute("INSERT INTO user VALUES(?,?,?) ",(self.name,self.password,self.flag))
        conn.commit()
        conn.close()
        self.label_5.setText(_translate("MainWindow", "????????????"))   ## ??????????????????
    def choose(self):
        if (self.checkBox.isChecked()): self.flag = 0
        if (self.checkBox_2.isChecked()): self.flag = 1
      
    
    ## ??????????????????
    def handleNameChange(self):
        self.name = self.lineEdit.text()
    def handlePasswordChange(self):
        self.password = self.lineEdit_2.text()   
    def handleSurewordChange(self):
        self.sureword = self.lineEdit_3.text()         