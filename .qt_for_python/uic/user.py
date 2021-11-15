# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user.ui'
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
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(330, 30, 141, 51))
        self.label_title.setWordWrap(False)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(600, 140, 151, 51))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(30, 240, 151, 51))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 320, 141, 51))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 380, 121, 41))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 440, 151, 51))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 494, 111, 31))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(230, 220, 521, 271))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(510, 80, 151, 31))
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(660, 80, 93, 31))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(320, 140, 151, 51))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 140, 151, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u7cfb\u7edf", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8bc6\u522b\u6a21\u578b", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u8bc6\u522b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b\u7ed3\u679c\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"XXX\u5783\u573e", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u5ea6\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"98%", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"                                 \u56fe\u50cf\u663e\u793a\u533a", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u6444\u50cf\u5934", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6444\u50cf\u5934", None))
    # retranslateUi

