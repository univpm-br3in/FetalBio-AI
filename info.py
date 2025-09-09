# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(630, 491)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 591, 410))
        self.Main = QVBoxLayout(self.verticalLayoutWidget)
        self.Main.setObjectName(u"Main")
        self.Main.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Main.addWidget(self.label)

        self.motherLayout = QVBoxLayout()
        self.motherLayout.setObjectName(u"motherLayout")
        self.label_12 = QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.motherLayout.addWidget(self.label_12)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_4.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_4)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_6)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_3)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_5)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.IdInput = QLineEdit(self.verticalLayoutWidget)
        self.IdInput.setObjectName(u"IdInput")

        self.verticalLayout_6.addWidget(self.IdInput)

        self.AgeInput = QLineEdit(self.verticalLayoutWidget)
        self.AgeInput.setObjectName(u"AgeInput")

        self.verticalLayout_6.addWidget(self.AgeInput)

        self.WeightInput = QLineEdit(self.verticalLayoutWidget)
        self.WeightInput.setObjectName(u"WeightInput")

        self.verticalLayout_6.addWidget(self.WeightInput)

        self.HeightInput = QLineEdit(self.verticalLayoutWidget)
        self.HeightInput.setObjectName(u"HeightInput")

        self.verticalLayout_6.addWidget(self.HeightInput)

        self.BmiInput = QLineEdit(self.verticalLayoutWidget)
        self.BmiInput.setObjectName(u"BmiInput")

        self.verticalLayout_6.addWidget(self.BmiInput)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_7)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_8)

        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_9)

        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_10)

        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_11)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.GravidityBox = QComboBox(self.verticalLayoutWidget)
        self.GravidityBox.addItem("")
        self.GravidityBox.addItem("")
        self.GravidityBox.addItem("")
        self.GravidityBox.addItem("")
        self.GravidityBox.addItem("")
        self.GravidityBox.addItem("")
        self.GravidityBox.addItem("")
        self.GravidityBox.setObjectName(u"GravidityBox")

        self.verticalLayout_8.addWidget(self.GravidityBox)

        self.ParityBox = QComboBox(self.verticalLayoutWidget)
        self.ParityBox.addItem("")
        self.ParityBox.addItem("")
        self.ParityBox.addItem("")
        self.ParityBox.addItem("")
        self.ParityBox.addItem("")
        self.ParityBox.addItem("")
        self.ParityBox.addItem("")
        self.ParityBox.setObjectName(u"ParityBox")

        self.verticalLayout_8.addWidget(self.ParityBox)

        self.DiabetesBool = QCheckBox(self.verticalLayoutWidget)
        self.DiabetesBool.setObjectName(u"DiabetesBool")

        self.verticalLayout_8.addWidget(self.DiabetesBool)

        self.HypertensionBool = QCheckBox(self.verticalLayoutWidget)
        self.HypertensionBool.setObjectName(u"HypertensionBool")

        self.verticalLayout_8.addWidget(self.HypertensionBool)

        self.PreeclampsiaBool = QCheckBox(self.verticalLayoutWidget)
        self.PreeclampsiaBool.setObjectName(u"PreeclampsiaBool")

        self.verticalLayout_8.addWidget(self.PreeclampsiaBool)


        self.horizontalLayout_2.addLayout(self.verticalLayout_8)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 1)

        self.motherLayout.addLayout(self.horizontalLayout_2)

        self.motherLayout.setStretch(1, 1)

        self.Main.addLayout(self.motherLayout)

        self.FetusLayout = QVBoxLayout()
        self.FetusLayout.setObjectName(u"FetusLayout")
        self.label_13 = QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.FetusLayout.addWidget(self.label_13)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_14 = QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_14)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.GaInputDays = QLineEdit(self.verticalLayoutWidget)
        self.GaInputDays.setObjectName(u"GaInputDays")

        self.horizontalLayout_3.addWidget(self.GaInputDays)

        self.label_15 = QLabel(self.verticalLayoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_3.addWidget(self.label_15)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.GaInputWeeks = QLineEdit(self.verticalLayoutWidget)
        self.GaInputWeeks.setObjectName(u"GaInputWeeks")

        self.horizontalLayout_3.addWidget(self.GaInputWeeks)

        self.label_16 = QLabel(self.verticalLayoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_3.addWidget(self.label_16)


        self.FetusLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_18 = QLabel(self.verticalLayoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_18)

        self.EDDInput = QDateEdit(self.verticalLayoutWidget)
        self.EDDInput.setObjectName(u"EDDInput")
        self.EDDInput.setDateTime(QDateTime(QDate(2024, 12, 31), QTime(22, 0, 0)))

        self.horizontalLayout_6.addWidget(self.EDDInput)


        self.FetusLayout.addLayout(self.horizontalLayout_6)

        self.sexLayout = QHBoxLayout()
        self.sexLayout.setObjectName(u"sexLayout")
        self.label_17 = QLabel(self.verticalLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)

        self.sexLayout.addWidget(self.label_17)

        self.sexBox = QComboBox(self.verticalLayoutWidget)
        self.sexBox.addItem("")
        self.sexBox.addItem("")
        self.sexBox.addItem("")
        self.sexBox.setObjectName(u"sexBox")

        self.sexLayout.addWidget(self.sexBox)


        self.FetusLayout.addLayout(self.sexLayout)


        self.Main.addLayout(self.FetusLayout)

        self.Main.setStretch(1, 1)
        self.Main.setStretch(2, 1)
        self.done_Button = QPushButton(Form)
        self.done_Button.setObjectName(u"done_Button")
        self.done_Button.setGeometry(QRect(470, 450, 141, 31))
        self.label_19 = QLabel(Form)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 450, 191, 21))
        self.cancel_button = QPushButton(Form)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(320, 450, 141, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Please enter the following information", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Mother's Information", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"ID *", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Age (Y) * ", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Weight (Kg)", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Height (cm)", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"BMI (Kg/cm2)", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Gravidity", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Parity", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Diabetes", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Hypertension", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Preeclampsia", None))
        self.GravidityBox.setItemText(0, QCoreApplication.translate("Form", u"Unknown", None))
        self.GravidityBox.setItemText(1, QCoreApplication.translate("Form", u"1", None))
        self.GravidityBox.setItemText(2, QCoreApplication.translate("Form", u"2", None))
        self.GravidityBox.setItemText(3, QCoreApplication.translate("Form", u"3", None))
        self.GravidityBox.setItemText(4, QCoreApplication.translate("Form", u"4", None))
        self.GravidityBox.setItemText(5, QCoreApplication.translate("Form", u"5", None))
        self.GravidityBox.setItemText(6, QCoreApplication.translate("Form", u">5", None))

        self.ParityBox.setItemText(0, QCoreApplication.translate("Form", u"Unknown", None))
        self.ParityBox.setItemText(1, QCoreApplication.translate("Form", u"1", None))
        self.ParityBox.setItemText(2, QCoreApplication.translate("Form", u"2", None))
        self.ParityBox.setItemText(3, QCoreApplication.translate("Form", u"3", None))
        self.ParityBox.setItemText(4, QCoreApplication.translate("Form", u"4", None))
        self.ParityBox.setItemText(5, QCoreApplication.translate("Form", u"5", None))
        self.ParityBox.setItemText(6, QCoreApplication.translate("Form", u">5", None))

        self.DiabetesBool.setText("")
        self.HypertensionBool.setText("")
        self.PreeclampsiaBool.setText("")
        self.label_13.setText(QCoreApplication.translate("Form", u"Fetus's Information", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"GA*", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"D", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"W", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"EDD*: ", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Sex", None))
        self.sexBox.setItemText(0, QCoreApplication.translate("Form", u"Unknown", None))
        self.sexBox.setItemText(1, QCoreApplication.translate("Form", u"Male", None))
        self.sexBox.setItemText(2, QCoreApplication.translate("Form", u"Female", None))

        self.done_Button.setText(QCoreApplication.translate("Form", u"Done", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Feilds with * are mandatory.", None))
        self.cancel_button.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

