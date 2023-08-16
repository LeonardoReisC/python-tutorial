# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'workerUI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_MyWidget(object):
    def setupUi(self, MyWidget):
        if not MyWidget.objectName():
            MyWidget.setObjectName(u"MyWidget")
        MyWidget.resize(400, 300)
        font = QFont()
        font.setPointSize(30)
        MyWidget.setFont(font)
        self.horizontalLayout = QHBoxLayout(MyWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label2 = QLabel(MyWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label2, 0, 1, 1, 1)

        self.label1 = QLabel(MyWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1)

        self.button1 = QPushButton(MyWidget)
        self.button1.setObjectName(u"button1")

        self.gridLayout.addWidget(self.button1, 1, 0, 1, 1)

        self.button2 = QPushButton(MyWidget)
        self.button2.setObjectName(u"button2")

        self.gridLayout.addWidget(self.button2, 1, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.retranslateUi(MyWidget)

        QMetaObject.connectSlotsByName(MyWidget)
    # setupUi

    def retranslateUi(self, MyWidget):
        MyWidget.setWindowTitle(QCoreApplication.translate("MyWidget", u"Form", None))
        self.label2.setText(QCoreApplication.translate("MyWidget", u"L2", None))
        self.label1.setText(QCoreApplication.translate("MyWidget", u"L1", None))
        self.button1.setText(QCoreApplication.translate("MyWidget", u"B1", None))
        self.button2.setText(QCoreApplication.translate("MyWidget", u"B2", None))
    # retranslateUi

