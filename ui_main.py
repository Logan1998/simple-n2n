# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(250, 290)
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        Form.setFont(font)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(175, 264, 41, 20))
        self.label.setFont(font)
        self.labelStatus = QLabel(Form)
        self.labelStatus.setObjectName(u"labelStatus")
        self.labelStatus.setGeometry(QRect(220, 265, 18, 18))
        self.labelStatus.setStyleSheet(u"border-image: url(\"img/n.png\");")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(92, 190, 64, 64))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"border-image: url(./img/run.png);")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 155, 210, 28))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(10)
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setCursor(QCursor(Qt.ArrowCursor))
        self.lineEdit_2.setStyleSheet(u"")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 130, 51, 20))
        font2 = QFont()
        font2.setFamilies([u"\u9ed1\u4f53"])
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 35, 210, 28))
        self.lineEdit.setFont(font1)
        self.lineEdit.setCursor(QCursor(Qt.ArrowCursor))
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 51, 20))
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 250, 231, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 70, 71, 20))
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(20, 95, 210, 28))
        self.lineEdit_3.setFont(font1)
        self.lineEdit_3.setCursor(QCursor(Qt.ArrowCursor))
        self.lineEdit_3.setStyleSheet(u"")
        self.lineEdit_3.setAlignment(Qt.AlignCenter)
        self.lineEdit_3.setReadOnly(True)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(12, 263, 41, 20))
        self.label_2.setFont(font)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 265, 21, 16))
        self.label_6.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"SimpleN2N", None))
        self.label.setText(QCoreApplication.translate("Form", u"Status:", None))
        self.labelStatus.setText("")
        self.pushButton.setText("")
        self.lineEdit_2.setText(QCoreApplication.translate("Form", u"\u672a\u5206\u914d", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u865a\u62df\u7f51IP", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"localhost", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u670d\u52a1\u5668", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u5c0f\u7ec4\u540d\u79f0", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Form", u"network", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Online:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"??", None))
    # retranslateUi

