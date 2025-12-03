# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainui.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.clearBtn = QPushButton(MainWindow)
        self.clearBtn.setObjectName(u"clearBtn")
        self.clearBtn.setGeometry(QRect(910, 1000, 100, 50))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearBtn.sizePolicy().hasHeightForWidth())
        self.clearBtn.setSizePolicy(sizePolicy)
        self.clearBtn.setMaximumSize(QSize(100, 50))
        self.clearBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(60, 60, 60, 0.9);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    font-size: 16px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(80, 80, 80, 0.9);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(100, 100, 100, 0.9);\n"
"}")
        MainWindow.setCentralWidget(self.clearBtn)
        self.FloatToolWidget = QWidget(MainWindow)
        self.FloatToolWidget.setObjectName(u"FloatToolWidget")
        self.FloatToolWidget.setGeometry(QRect(660, 1000, 600, 60))
        self.FloatToolWidget.setStyleSheet(u"background-color: rgba(40, 40, 40, 0.85);\n"
"border-radius: 12px;")
        self.horizontalLayout_2 = QHBoxLayout(self.FloatToolWidget)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.btnPen = QPushButton(self.FloatToolWidget)
        self.btnPen.setObjectName(u"btnPen")
        self.btnPen.setMinimumSize(QSize(40, 40))
        self.btnPen.setMaximumSize(QSize(40, 40))
        self.btnPen.setStyleSheet(u"QPushButton { background-color: rgba(60, 60, 60, 0.7); color: white; border-radius: 8px; text-align: center; } QPushButton:hover { background-color: rgba(80, 80, 80, 0.7); } QPushButton:pressed, QPushButton:checked { background-color: rgba(100, 100, 100, 0.7); }")
        icon = QIcon()
        icon.addFile(u":/icons/pen.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPen.setIcon(icon)
        self.btnPen.setCheckable(True)
        self.btnPen.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.btnPen)

        self.btnLine = QPushButton(self.FloatToolWidget)
        self.btnLine.setObjectName(u"btnLine")
        self.btnLine.setMinimumSize(QSize(40, 40))
        self.btnLine.setMaximumSize(QSize(40, 40))
        self.btnLine.setStyleSheet(u"QPushButton { background-color: rgba(60, 60, 60, 0.7); color: white; border-radius: 8px; text-align: center; } QPushButton:hover { background-color: rgba(80, 80, 80, 0.7); } QPushButton:pressed, QPushButton:checked { background-color: rgba(100, 100, 100, 0.7); }")
        icon1 = QIcon()
        icon1.addFile(u":/icons/arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLine.setIcon(icon1)
        self.btnLine.setCheckable(True)
        self.btnLine.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.btnLine)

        self.btnRect = QPushButton(self.FloatToolWidget)
        self.btnRect.setObjectName(u"btnRect")
        self.btnRect.setMinimumSize(QSize(40, 40))
        self.btnRect.setMaximumSize(QSize(40, 40))
        self.btnRect.setStyleSheet(u"QPushButton { background-color: rgba(60, 60, 60, 0.7); color: white; border-radius: 8px; text-align: center; } QPushButton:hover { background-color: rgba(80, 80, 80, 0.7); } QPushButton:pressed, QPushButton:checked { background-color: rgba(100, 100, 100, 0.7); }")
        icon2 = QIcon()
        icon2.addFile(u":/icons/correction.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnRect.setIcon(icon2)
        self.btnRect.setCheckable(True)
        self.btnRect.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.btnRect)

        self.btnCircle = QPushButton(self.FloatToolWidget)
        self.btnCircle.setObjectName(u"btnCircle")
        self.btnCircle.setMinimumSize(QSize(40, 40))
        icon3 = QIcon()
        icon3.addFile(u":/icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCircle.setIcon(icon3)
        self.btnCircle.setMaximumSize(QSize(40, 40))
        self.btnCircle.setStyleSheet(u"QPushButton { background-color: rgba(60, 60, 60, 0.7); color: white; border-radius: 8px; text-align: center; } QPushButton:hover { background-color: rgba(80, 80, 80, 0.7); } QPushButton:pressed, QPushButton:checked { background-color: rgba(100, 100, 100, 0.7); }")
        self.btnCircle.setCheckable(True)
        self.btnCircle.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.btnCircle)

        self.btnEllipse = QPushButton(self.FloatToolWidget)
        self.btnEllipse.setObjectName(u"btnEllipse")
        self.btnEllipse.setMinimumSize(QSize(40, 40))
        icon4 = QIcon()
        icon4.addFile(u":/icons/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEllipse.setIcon(icon4)
        self.btnEllipse.setMaximumSize(QSize(40, 40))
        self.btnEllipse.setStyleSheet(u"QPushButton { background-color: rgba(60, 60, 60, 0.7); color: white; border-radius: 8px; text-align: center; } QPushButton:hover { background-color: rgba(80, 80, 80, 0.7); } QPushButton:pressed, QPushButton:checked { background-color: rgba(100, 100, 100, 0.7); }")
        self.btnEllipse.setCheckable(True)
        self.btnEllipse.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.btnEllipse)

        self.line = QFrame(self.FloatToolWidget)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgba(80, 80, 80, 0.5);")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.line_2 = QFrame(self.FloatToolWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgba(80, 80, 80, 0.5);")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.btnEraser = QPushButton(self.FloatToolWidget)
        self.btnEraser.setObjectName(u"btnEraser")
        self.btnEraser.setMinimumSize(QSize(40, 40))
        icon5 = QIcon()
        icon5.addFile(u":/icons/eraser.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEraser.setIcon(icon5)
        self.btnEraser.setMaximumSize(QSize(40, 40))
        self.btnEraser.setStyleSheet(u"QPushButton { background-color: rgba(60, 60, 60, 0.7); color: white; border-radius: 8px; text-align: center; } QPushButton:hover { background-color: rgba(80, 80, 80, 0.7); } QPushButton:pressed, QPushButton:checked { background-color: rgba(100, 100, 100, 0.7); }")
        self.btnEraser.setCheckable(True)
        self.btnEraser.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.btnEraser)

        self.line_3 = QFrame(self.FloatToolWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background-color: rgba(80, 80, 80, 0.5);")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_3)

        self.btnPPTPrev = QPushButton(self.FloatToolWidget)
        self.btnPPTPrev.setObjectName(u"btnPPTPrev")
        self.btnPPTPrev.setMinimumSize(QSize(40, 40))
        icon6 = QIcon()
        icon6.addFile(u":/icons/minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPPTPrev.setIcon(icon6)
        self.btnPPTPrev.setMaximumSize(QSize(40, 40))
        self.btnPPTPrev.setStyleSheet(u"QPushButton { background-color: rgba(60, 60, 60, 0.7); color: white; border-radius: 8px; } QPushButton:hover { background-color: rgba(80, 80, 80, 0.7); } QPushButton:pressed { background-color: rgba(100, 100, 100, 0.7); }")

        self.horizontalLayout_2.addWidget(self.btnPPTPrev)

        self.btnPPTNext = QPushButton(self.FloatToolWidget)
        self.btnPPTNext.setObjectName(u"btnPPTNext")
        self.btnPPTNext.setMinimumSize(QSize(40, 40))
        self.btnPPTNext.setIcon(icon6)
        self.btnPPTNext.setMaximumSize(QSize(40, 40))
        self.btnPPTNext.setStyleSheet(u"QPushButton { background-color: rgba(60, 60, 60, 0.7); color: white; border-radius: 8px; } QPushButton:hover { background-color: rgba(80, 80, 80, 0.7); } QPushButton:pressed { background-color: rgba(100, 100, 100, 0.7); }")

        self.horizontalLayout_2.addWidget(self.btnPPTNext)

        self.btnExit = QPushButton(self.FloatToolWidget)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setMinimumSize(QSize(40, 40))
        icon7 = QIcon()
        icon7.addFile(u":/icons/exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnExit.setIcon(icon7)
        self.btnExit.setMaximumSize(QSize(40, 40))
        self.btnExit.setStyleSheet(u"QPushButton { background-color: rgba(60, 60, 60, 0.7); color: white; border-radius: 8px; } QPushButton:hover { background-color: rgba(80, 80, 80, 0.7); } QPushButton:pressed { background-color: rgba(100, 100, 100, 0.7); }")

        self.horizontalLayout_2.addWidget(self.btnExit)

        MainWindow.setCentralWidget(self.FloatToolWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.clearBtn.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u5c4f", None))
        self.btnPen.setText(QCoreApplication.translate("MainWindow", u"P\n"
"\u753b\u7b14", None))
        self.btnLine.setText(QCoreApplication.translate("MainWindow", u"L\n"
"\u76f4\u7ebf", None))
        self.btnRect.setText(QCoreApplication.translate("MainWindow", u"R\n"
"\u77e9\u5f62", None))
        self.btnCircle.setText(QCoreApplication.translate("MainWindow", u"C\n"
"\u5706\u5f62", None))
        self.btnEllipse.setText(QCoreApplication.translate("MainWindow", u"O\n"
"\u692d\u5706", None))
        self.btnEraser.setText(QCoreApplication.translate("MainWindow", u"\u6a61\u76ae", None))
        self.btnPPTPrev.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u9875", None))
        self.btnPPTNext.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u9875", None))
        self.btnExit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
    # retranslateUi

