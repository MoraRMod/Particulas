# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(709, 499)
        self.Particulas_GroupBox = QGroupBox(Dialog)
        self.Particulas_GroupBox.setObjectName(u"Particulas_GroupBox")
        self.Particulas_GroupBox.setGeometry(QRect(0, 0, 711, 501))
        self.gridLayout = QGridLayout(self.Particulas_GroupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Datos_GroupBox = QGroupBox(self.Particulas_GroupBox)
        self.Datos_GroupBox.setObjectName(u"Datos_GroupBox")
        self.spinBox_6 = QSpinBox(self.Datos_GroupBox)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setGeometry(QRect(20, 290, 51, 22))
        self.spinBox_6.setMaximum(255)
        self.Green_Label = QLabel(self.Datos_GroupBox)
        self.Green_Label.setObjectName(u"Green_Label")
        self.Green_Label.setGeometry(QRect(10, 220, 51, 21))
        self.spinBox_4 = QSpinBox(self.Datos_GroupBox)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setGeometry(QRect(20, 190, 51, 22))
        self.spinBox_4.setMaximum(255)
        self.spinBox_2 = QSpinBox(self.Datos_GroupBox)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(20, 90, 51, 22))
        self.spinBox_2.setMaximum(500)
        self.Red_Label = QLabel(self.Datos_GroupBox)
        self.Red_Label.setObjectName(u"Red_Label")
        self.Red_Label.setGeometry(QRect(10, 170, 51, 21))
        self.spinBox = QSpinBox(self.Datos_GroupBox)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(21, 40, 51, 21))
        self.spinBox.setMaximum(500)
        self.Blue_Label = QLabel(self.Datos_GroupBox)
        self.Blue_Label.setObjectName(u"Blue_Label")
        self.Blue_Label.setGeometry(QRect(10, 270, 51, 21))
        self.DestinoY_Label = QLabel(self.Datos_GroupBox)
        self.DestinoY_Label.setObjectName(u"DestinoY_Label")
        self.DestinoY_Label.setGeometry(QRect(10, 70, 51, 21))
        self.spinBox_5 = QSpinBox(self.Datos_GroupBox)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setGeometry(QRect(20, 240, 51, 22))
        self.spinBox_5.setMaximum(255)
        self.Velocidad_Label = QLabel(self.Datos_GroupBox)
        self.Velocidad_Label.setObjectName(u"Velocidad_Label")
        self.Velocidad_Label.setGeometry(QRect(10, 120, 51, 21))
        self.DestinoX_Label = QLabel(self.Datos_GroupBox)
        self.DestinoX_Label.setObjectName(u"DestinoX_Label")
        self.DestinoX_Label.setGeometry(QRect(10, 20, 51, 21))
        self.spinBox_3 = QSpinBox(self.Datos_GroupBox)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(20, 140, 51, 22))

        self.gridLayout.addWidget(self.Datos_GroupBox, 0, 0, 2, 1)

        self.Contenido_GraphicsView = QGraphicsView(self.Particulas_GroupBox)
        self.Contenido_GraphicsView.setObjectName(u"Contenido_GraphicsView")

        self.gridLayout.addWidget(self.Contenido_GraphicsView, 0, 1, 1, 3)

        self.AgregarInicio_PushButton = QPushButton(self.Particulas_GroupBox)
        self.AgregarInicio_PushButton.setObjectName(u"AgregarInicio_PushButton")

        self.gridLayout.addWidget(self.AgregarInicio_PushButton, 1, 1, 1, 1)

        self.AgregarFinal_PushButton = QPushButton(self.Particulas_GroupBox)
        self.AgregarFinal_PushButton.setObjectName(u"AgregarFinal_PushButton")

        self.gridLayout.addWidget(self.AgregarFinal_PushButton, 1, 2, 1, 1)

        self.Mostrar_PushButon = QPushButton(self.Particulas_GroupBox)
        self.Mostrar_PushButon.setObjectName(u"Mostrar_PushButon")

        self.gridLayout.addWidget(self.Mostrar_PushButon, 1, 3, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Particulas_GroupBox.setTitle(QCoreApplication.translate("Dialog", u"Particulas", None))
        self.Datos_GroupBox.setTitle(QCoreApplication.translate("Dialog", u"Datos", None))
        self.Green_Label.setText(QCoreApplication.translate("Dialog", u"Green", None))
        self.Red_Label.setText(QCoreApplication.translate("Dialog", u"Red", None))
        self.Blue_Label.setText(QCoreApplication.translate("Dialog", u"Blue", None))
        self.DestinoY_Label.setText(QCoreApplication.translate("Dialog", u"Destino Y", None))
        self.Velocidad_Label.setText(QCoreApplication.translate("Dialog", u"Velocidad", None))
        self.DestinoX_Label.setText(QCoreApplication.translate("Dialog", u"Destino X", None))
        self.AgregarInicio_PushButton.setText(QCoreApplication.translate("Dialog", u"Agregar Inicio", None))
        self.AgregarFinal_PushButton.setText(QCoreApplication.translate("Dialog", u"Agregar Final", None))
        self.Mostrar_PushButon.setText(QCoreApplication.translate("Dialog", u"Mostrar", None))
    # retranslateUi

