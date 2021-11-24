# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'randomizer.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy)

class Ui_randomizer(object):
    def setupUi(self, randomizer):
        if not randomizer.objectName():
            randomizer.setObjectName(u"randomizer")
        randomizer.resize(250, 300)
        randomizer.setMinimumSize(QSize(250, 300))
        randomizer.setMaximumSize(QSize(250, 300))
        randomizer.setStyleSheet(u"background-color:#2e2e2e;")
        self.pushButton = QPushButton(randomizer)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 190, 231, 41))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"color:#fc7777;\n"
"border:2px solid #fc7777;\n"
"border-radius:20px;\n"
"font: 75 14pt \"Courier New\";\n"
"}\n"
"QPushButton:pressed{\n"
"color:#f23333;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#363636;\n"
"\n"
"}\n"
"")
        self.lineEdit = QLineEdit(randomizer)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(170, 60, 71, 41))
        self.lineEdit.setStyleSheet(u"color:#fc7777;\n"
"border:2px solid #fc7777;\n"
"border-radius:20px;\n"
"	font: 14pt \"Courier New\";")
        self.lineEdit.setMaxLength(4)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.label = QLabel(randomizer)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 70, 151, 16))
        self.label.setStyleSheet(u"\n"
"color:#fc7777;\n"
"\n"
"	font: 12pt \"Courier New\";")
        self.lineEdit_2 = QLineEdit(randomizer)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(170, 120, 71, 41))
        self.lineEdit_2.setStyleSheet(u"color:#fc7777;\n"
"border:2px solid #fc7777;\n"
"border-radius:20px;\n"
"	font: 14pt \"Courier New\";")
        self.lineEdit_2.setMaxLength(4)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(randomizer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 130, 151, 16))
        self.label_2.setStyleSheet(u"\n"
"color:#fc7777;\n"
"\n"
"	font: 12pt \"Courier New\";")
        self.label_3 = QLabel(randomizer)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 260, 151, 16))
        self.label_3.setStyleSheet(u"\n"
"color:#fc7777;\n"
"\n"
"	font: 12pt \"Courier New\";")
        self.label_out = QLabel(randomizer)
        self.label_out.setObjectName(u"label_out")
        self.label_out.setGeometry(QRect(180, 250, 61, 41))
        self.label_out.setStyleSheet(u"color:#fc7777;\n"
"border:2px solid #fc7777;\n"
"border-radius:20px;\n"
"	font: 14pt \"Courier New\";")
        self.label_out.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(randomizer)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 2, 231, 41))
        self.label_5.setStyleSheet(u"color:#fc7777;\n"
"border:2px solid #fc7777;\n"
"border-radius:20px;\n"
"font: 75 14pt \"Courier New\";")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.retranslateUi(randomizer)

        QMetaObject.connectSlotsByName(randomizer)
    # setupUi

    def retranslateUi(self, randomizer):
        randomizer.setWindowTitle(QCoreApplication.translate("randomizer", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("randomizer", u"\u0440\u0430\u043d\u0434\u043e\u043c\u043d\u043e\u0435 \u0447\u0438\u0441\u043b\u043e", None))
        self.label.setText(QCoreApplication.translate("randomizer", u"\u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0435 \u0447\u0438\u0441\u043b\u043e", None))
        self.label_2.setText(QCoreApplication.translate("randomizer", u"\u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0435 \u0447\u0438\u0441\u043b\u043e", None))
        self.label_3.setText(QCoreApplication.translate("randomizer", u"\u0440\u0430\u043d\u0434\u043e\u043c\u043d\u043e\u0435 \u0447\u0438\u0441\u043b\u043e", None))
        self.label_out.setText("")
        self.label_5.setText(QCoreApplication.translate("randomizer", u"\u0440\u0430\u043d\u0434\u043e\u043c\u043d\u043e\u0435 \u0447\u0438\u0441\u043b\u043e ", None))
    # retranslateUi

