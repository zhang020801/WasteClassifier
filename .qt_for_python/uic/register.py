# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(170, 30, 60, 12))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 100, 48, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 150, 36, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 210, 60, 12))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 280, 60, 16))
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(170, 280, 63, 16))
        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(260, 280, 51, 16))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 340, 93, 28))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(160, 150, 121, 20))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(160, 100, 121, 20))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(160, 200, 121, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u8005\u6ce8\u518c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u5bc6\u7801\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u6027\u8d28\uff1a", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u7ba1\u7406\u5458", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c", None))
    # retranslateUi

