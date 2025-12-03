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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLayout,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.drawing_board = QWidget(self.centralwidget)
        self.drawing_board.setObjectName(u"drawing_board")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drawing_board.sizePolicy().hasHeightForWidth())
        self.drawing_board.setSizePolicy(sizePolicy)
        self.drawing_board.setFocusPolicy(Qt.NoFocus)
        self.drawing_board.setAutoFillBackground(False)

        self.verticalLayout.addWidget(self.drawing_board)

        self.clearBtn = QPushButton(self.centralwidget)
        self.clearBtn.setObjectName(u"clearBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.clearBtn.sizePolicy().hasHeightForWidth())
        self.clearBtn.setSizePolicy(sizePolicy1)
        self.clearBtn.setGeometry(QRect(910, 1000, 100, 50))
        self.clearBtn.setMaximumSize(QSize(100, 50))
        self.clearBtn.setVisible(False)
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

        self.verticalLayout.addWidget(self.clearBtn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.FloatToolWidget = QWidget(MainWindow)
        self.FloatToolWidget.setObjectName(u"FloatToolWidget")
        self.FloatToolWidget.setGeometry(QRect(1800, 340, 400, 60))
        self.FloatToolWidget.setStyleSheet(u"background-color: rgba(40, 40, 40, 0.85);\n"
"border-radius: 12px;")
        self.horizontalLayout_2 = QHBoxLayout(self.FloatToolWidget)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.btnPen = QPushButton(self.FloatToolWidget)
        self.btnPen.setObjectName(u"btnPen")
        sizePolicy1.setHeightForWidth(self.btnPen.sizePolicy().hasHeightForWidth())
        self.btnPen.setSizePolicy(sizePolicy1)
        self.btnPen.setMinimumSize(QSize(40, 40))
        self.btnPen.setMaximumSize(QSize(40, 40))
        font = QFont()
        font.setPointSize(10)
        self.btnPen.setFont(font)
        self.btnPen.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(60, 60, 60, 0.7);\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(80, 80, 80, 0.7);\n"
"}\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"    background-color: rgba(100, 100, 100, 0.7);\n"
"}")
        self.btnPen.setCheckable(True)
        self.btnPen.setChecked(True)
        self.btnPen.setAutoExclusive(True)
        self.btnPen.setAutoRepeat(False)

        self.horizontalLayout_2.addWidget(self.btnPen)

        self.btnLine = QPushButton(self.FloatToolWidget)
        self.btnLine.setObjectName(u"btnLine")
        sizePolicy1.setHeightForWidth(self.btnLine.sizePolicy().hasHeightForWidth())
        self.btnLine.setSizePolicy(sizePolicy1)
        self.btnLine.setMinimumSize(QSize(40, 40))
        self.btnLine.setMaximumSize(QSize(40, 40))
        self.btnLine.setFont(font)
        self.btnLine.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(60, 60, 60, 0.7);\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(80, 80, 80, 0.7);\n"
"}\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"    background-color: rgba(100, 100, 100, 0.7);\n"
"}")
        self.btnLine.setCheckable(True)
        self.btnLine.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.btnLine)

        self.btnRect = QPushButton(self.FloatToolWidget)
        self.btnRect.setObjectName(u"btnRect")
        sizePolicy1.setHeightForWidth(self.btnRect.sizePolicy().hasHeightForWidth())
        self.btnRect.setSizePolicy(sizePolicy1)
        self.btnRect.setMinimumSize(QSize(40, 40))
        self.btnRect.setMaximumSize(QSize(40, 40))
        self.btnRect.setFont(font)
        self.btnRect.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(60, 60, 60, 0.7);\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(80, 80, 80, 0.7);\n"
"}\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"    background-color: rgba(100, 100, 100, 0.7);\n"
"}")
        self.btnRect.setCheckable(True)
        self.btnRect.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.btnRect)

        self.btnCircle = QPushButton(self.FloatToolWidget)
        self.btnCircle.setObjectName(u"btnCircle")
        sizePolicy1.setHeightForWidth(self.btnCircle.sizePolicy().hasHeightForWidth())
        self.btnCircle.setSizePolicy(sizePolicy1)
        self.btnCircle.setMinimumSize(QSize(40, 40))
        self.btnCircle.setMaximumSize(QSize(40, 40))
        self.btnCircle.setFont(font)
        self.btnCircle.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(60, 60, 60, 0.7);\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(80, 80, 80, 0.7);\n"
"}\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"    background-color: rgba(100, 100, 100, 0.7);\n"
"}")
        self.btnCircle.setCheckable(True)
        self.btnCircle.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.btnCircle)

        self.btnEllipse = QPushButton(self.FloatToolWidget)
        self.btnEllipse.setObjectName(u"btnEllipse")
        sizePolicy1.setHeightForWidth(self.btnEllipse.sizePolicy().hasHeightForWidth())
        self.btnEllipse.setSizePolicy(sizePolicy1)
        self.btnEllipse.setMinimumSize(QSize(40, 40))
        self.btnEllipse.setMaximumSize(QSize(40, 40))
        self.btnEllipse.setFont(font)
        self.btnEllipse.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(60, 60, 60, 0.7);\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(80, 80, 80, 0.7);\n"
"}\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"    background-color: rgba(100, 100, 100, 0.7);\n"
"}")
        self.btnEllipse.setCheckable(True)
        self.btnEllipse.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.btnEllipse)

        self.line = QFrame(self.FloatToolWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setStyleSheet(u"background-color: rgba(80, 80, 80, 0.5);")

        self.horizontalLayout_2.addWidget(self.line)

        self.line_2 = QFrame(self.FloatToolWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setStyleSheet(u"background-color: rgba(80, 80, 80, 0.5);")

        self.horizontalLayout_2.addWidget(self.line_2)

        self.btnEraser = QPushButton(self.FloatToolWidget)
        self.btnEraser.setObjectName(u"btnEraser")
        sizePolicy1.setHeightForWidth(self.btnEraser.sizePolicy().hasHeightForWidth())
        self.btnEraser.setSizePolicy(sizePolicy1)
        self.btnEraser.setMinimumSize(QSize(40, 40))
        self.btnEraser.setMaximumSize(QSize(40, 40))
        self.btnEraser.setFont(font)
        self.btnEraser.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(60, 60, 60, 0.7);\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(80, 80, 80, 0.7);\n"
"}\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"    background-color: rgba(100, 100, 100, 0.7);\n"
"}")
        self.btnEraser.setCheckable(True)
        self.btnEraser.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.btnEraser)

        self.line_3 = QFrame(self.FloatToolWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.setStyleSheet(u"background-color: rgba(80, 80, 80, 0.5);")

        self.horizontalLayout_2.addWidget(self.line_3)

        self.btnPPTPrev = QPushButton(self.FloatToolWidget)
        self.btnPPTPrev.setObjectName(u"btnPPTPrev")
        sizePolicy1.setHeightForWidth(self.btnPPTPrev.sizePolicy().hasHeightForWidth())
        self.btnPPTPrev.setSizePolicy(sizePolicy1)
        self.btnPPTPrev.setMinimumSize(QSize(40, 40))
        self.btnPPTPrev.setMaximumSize(QSize(40, 40))
        self.btnPPTPrev.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(60, 60, 60, 0.7);\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(80, 80, 80, 0.7);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(100, 100, 100, 0.7);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btnPPTPrev)

        self.btnPPTNext = QPushButton(self.FloatToolWidget)
        self.btnPPTNext.setObjectName(u"btnPPTNext")
        sizePolicy1.setHeightForWidth(self.btnPPTNext.sizePolicy().hasHeightForWidth())
        self.btnPPTNext.setSizePolicy(sizePolicy1)
        self.btnPPTNext.setMinimumSize(QSize(40, 40))
        self.btnPPTNext.setMaximumSize(QSize(40, 40))
        self.btnPPTNext.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(60, 60, 60, 0.7);\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(80, 80, 80, 0.7);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(100, 100, 100, 0.7);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btnPPTNext)

        self.btnExit = QPushButton(self.FloatToolWidget)
        self.btnExit.setObjectName(u"btnExit")
        sizePolicy1.setHeightForWidth(self.btnExit.sizePolicy().hasHeightForWidth())
        self.btnExit.setSizePolicy(sizePolicy1)
        self.btnExit.setMinimumSize(QSize(40, 40))
        self.btnExit.setMaximumSize(QSize(40, 40))
        self.btnExit.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(60, 60, 60, 0.7);\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(80, 80, 80, 0.7);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(100, 100, 100, 0.7);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btnExit)

        MainWindow.setCentralWidget(self.FloatToolWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EasyWriteWhiteBoard", None))
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
        self.btnEraser.setText(QCoreApplication.translate("MainWindow", u"E\n"
"\u6a61\u76ae", None))
        self.btnPPTPrev.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u9875", None))
        self.btnPPTNext.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u9875", None))
        self.btnExit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
    # retranslateUi

