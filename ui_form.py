# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(987, 814)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMaximumSize(QSize(1084, 16777215))
        self.centralwidget.setBaseSize(QSize(0, 0))
        self.centralwidget.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.centralwidget.setAutoFillBackground(True)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 0, 951, 761))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.PatientLayout = QHBoxLayout()
        self.PatientLayout.setObjectName(u"PatientLayout")
        self.IDtext = QLabel(self.verticalLayoutWidget)
        self.IDtext.setObjectName(u"IDtext")
        font = QFont()
        font.setPointSize(12)
        self.IDtext.setFont(font)

        self.PatientLayout.addWidget(self.IDtext)

        self.MOTHERAGEtext = QLabel(self.verticalLayoutWidget)
        self.MOTHERAGEtext.setObjectName(u"MOTHERAGEtext")
        self.MOTHERAGEtext.setFont(font)

        self.PatientLayout.addWidget(self.MOTHERAGEtext)

        self.GAtext = QLabel(self.verticalLayoutWidget)
        self.GAtext.setObjectName(u"GAtext")
        self.GAtext.setFont(font)

        self.PatientLayout.addWidget(self.GAtext)

        self.EDDtext = QLabel(self.verticalLayoutWidget)
        self.EDDtext.setObjectName(u"EDDtext")
        self.EDDtext.setFont(font)

        self.PatientLayout.addWidget(self.EDDtext)


        self.verticalLayout_2.addLayout(self.PatientLayout)

        self.Workspace_Layout = QHBoxLayout()
        self.Workspace_Layout.setObjectName(u"Workspace_Layout")
        self.Workspace_Layout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.Workspace_Layout.setContentsMargins(0, 0, 0, 0)
        self.ControlPnael_Layout = QVBoxLayout()
        self.ControlPnael_Layout.setObjectName(u"ControlPnael_Layout")
        self.Buttons = QVBoxLayout()
        self.Buttons.setSpacing(20)
        self.Buttons.setObjectName(u"Buttons")
        self.newSub_Button = QPushButton(self.verticalLayoutWidget)
        self.newSub_Button.setObjectName(u"newSub_Button")
        font1 = QFont()
        font1.setPointSize(11)
        self.newSub_Button.setFont(font1)

        self.Buttons.addWidget(self.newSub_Button)

        self.loadImage_Button = QPushButton(self.verticalLayoutWidget)
        self.loadImage_Button.setObjectName(u"loadImage_Button")
        self.loadImage_Button.setEnabled(False)
        self.loadImage_Button.setFont(font1)

        self.Buttons.addWidget(self.loadImage_Button)

        self.predict_Button = QPushButton(self.verticalLayoutWidget)
        self.predict_Button.setObjectName(u"predict_Button")
        self.predict_Button.setEnabled(False)
        self.predict_Button.setFont(font1)

        self.Buttons.addWidget(self.predict_Button)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pixelSizeText = QLineEdit(self.verticalLayoutWidget)
        self.pixelSizeText.setObjectName(u"pixelSizeText")

        self.horizontalLayout_2.addWidget(self.pixelSizeText)

        self.unit = QLabel(self.verticalLayoutWidget)
        self.unit.setObjectName(u"unit")
        self.unit.setFont(font)

        self.horizontalLayout_2.addWidget(self.unit)


        self.Buttons.addLayout(self.horizontalLayout_2)


        self.ControlPnael_Layout.addLayout(self.Buttons)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.HCtextLabel = QLabel(self.verticalLayoutWidget)
        self.HCtextLabel.setObjectName(u"HCtextLabel")
        self.HCtextLabel.setFont(font)
        self.HCtextLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.HCtextLabel.setIndent(0)

        self.verticalLayout_5.addWidget(self.HCtextLabel)

        self.BPDtextLabel = QLabel(self.verticalLayoutWidget)
        self.BPDtextLabel.setObjectName(u"BPDtextLabel")
        self.BPDtextLabel.setFont(font)
        self.BPDtextLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.BPDtextLabel.setIndent(0)

        self.verticalLayout_5.addWidget(self.BPDtextLabel)

        self.OFDtextLabel = QLabel(self.verticalLayoutWidget)
        self.OFDtextLabel.setObjectName(u"OFDtextLabel")
        self.OFDtextLabel.setFont(font)
        self.OFDtextLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.OFDtextLabel.setIndent(0)

        self.verticalLayout_5.addWidget(self.OFDtextLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.HCtextLabel_5 = QLabel(self.verticalLayoutWidget)
        self.HCtextLabel_5.setObjectName(u"HCtextLabel_5")
        self.HCtextLabel_5.setFont(font)
        self.HCtextLabel_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.HCtextLabel_5.setIndent(0)

        self.verticalLayout_9.addWidget(self.HCtextLabel_5)

        self.BPDtextLabel_5 = QLabel(self.verticalLayoutWidget)
        self.BPDtextLabel_5.setObjectName(u"BPDtextLabel_5")
        self.BPDtextLabel_5.setFont(font)
        self.BPDtextLabel_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.BPDtextLabel_5.setIndent(0)

        self.verticalLayout_9.addWidget(self.BPDtextLabel_5)

        self.OFDtextLabel_5 = QLabel(self.verticalLayoutWidget)
        self.OFDtextLabel_5.setObjectName(u"OFDtextLabel_5")
        self.OFDtextLabel_5.setFont(font)
        self.OFDtextLabel_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.OFDtextLabel_5.setIndent(0)

        self.verticalLayout_9.addWidget(self.OFDtextLabel_5)


        self.horizontalLayout.addLayout(self.verticalLayout_9)


        self.ControlPnael_Layout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.ControlPnael_Layout.addItem(self.verticalSpacer)

        self.save_Button = QPushButton(self.verticalLayoutWidget)
        self.save_Button.setObjectName(u"save_Button")
        self.save_Button.setEnabled(False)
        self.save_Button.setFont(font1)

        self.ControlPnael_Layout.addWidget(self.save_Button)

        self.exit_Button = QPushButton(self.verticalLayoutWidget)
        self.exit_Button.setObjectName(u"exit_Button")
        self.exit_Button.setFont(font1)

        self.ControlPnael_Layout.addWidget(self.exit_Button)


        self.Workspace_Layout.addLayout(self.ControlPnael_Layout)

        self.graphicsView = QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView.setObjectName(u"graphicsView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy2)

        self.Workspace_Layout.addWidget(self.graphicsView)

        self.Workspace_Layout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.Workspace_Layout)

        self.contactUs_Layout = QHBoxLayout()
        self.contactUs_Layout.setObjectName(u"contactUs_Layout")
        self.Br3inLOGO = QGraphicsView(self.verticalLayoutWidget)
        self.Br3inLOGO.setObjectName(u"Br3inLOGO")
        sizePolicy.setHeightForWidth(self.Br3inLOGO.sizePolicy().hasHeightForWidth())
        self.Br3inLOGO.setSizePolicy(sizePolicy)

        self.contactUs_Layout.addWidget(self.Br3inLOGO)

        self.DIILOGO = QGraphicsView(self.verticalLayoutWidget)
        self.DIILOGO.setObjectName(u"DIILOGO")
        sizePolicy.setHeightForWidth(self.DIILOGO.sizePolicy().hasHeightForWidth())
        self.DIILOGO.setSizePolicy(sizePolicy)

        self.contactUs_Layout.addWidget(self.DIILOGO)

        self.logoUNIVPM = QGraphicsView(self.verticalLayoutWidget)
        self.logoUNIVPM.setObjectName(u"logoUNIVPM")
        sizePolicy.setHeightForWidth(self.logoUNIVPM.sizePolicy().hasHeightForWidth())
        self.logoUNIVPM.setSizePolicy(sizePolicy)

        self.contactUs_Layout.addWidget(self.logoUNIVPM)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(10)
        self.label.setFont(font2)
        self.label.setMargin(0)
        self.label.setIndent(0)

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setMargin(0)
        self.label_2.setIndent(0)

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setMargin(0)
        self.label_3.setIndent(0)

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)


        self.contactUs_Layout.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addLayout(self.contactUs_Layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 987, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.IDtext.setText(QCoreApplication.translate("MainWindow", u"Subject ID:", None))
        self.MOTHERAGEtext.setText(QCoreApplication.translate("MainWindow", u"Mother's Age:", None))
        self.GAtext.setText(QCoreApplication.translate("MainWindow", u"GA:", None))
        self.EDDtext.setText(QCoreApplication.translate("MainWindow", u"EDD:", None))
        self.newSub_Button.setText(QCoreApplication.translate("MainWindow", u"New Subject", None))
        self.loadImage_Button.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.predict_Button.setText(QCoreApplication.translate("MainWindow", u"Make Prediction", None))
        self.unit.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.HCtextLabel.setText(QCoreApplication.translate("MainWindow", u"HC:", None))
        self.BPDtextLabel.setText(QCoreApplication.translate("MainWindow", u"BPD:", None))
        self.OFDtextLabel.setText(QCoreApplication.translate("MainWindow", u"OFD:", None))
        self.HCtextLabel_5.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.BPDtextLabel_5.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.OFDtextLabel_5.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.save_Button.setText(QCoreApplication.translate("MainWindow", u"Save Prediction", None))
        self.exit_Button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label_5.setText("")
        self.label_6.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Contact Us:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Prof. Laura Burattini", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"l.burattini@univpm.it", None))
        self.label_7.setText("")
        self.label_4.setText("")
    # retranslateUi

