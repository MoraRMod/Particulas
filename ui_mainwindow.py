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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Particulas_GroupBox = QGroupBox(self.tab)
        self.Particulas_GroupBox.setObjectName(u"Particulas_GroupBox")
        self.gridLayout_2 = QGridLayout(self.Particulas_GroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Datos_GroupBox = QGroupBox(self.Particulas_GroupBox)
        self.Datos_GroupBox.setObjectName(u"Datos_GroupBox")
        self.Blue_SpinBox = QSpinBox(self.Datos_GroupBox)
        self.Blue_SpinBox.setObjectName(u"Blue_SpinBox")
        self.Blue_SpinBox.setGeometry(QRect(20, 290, 51, 22))
        self.Blue_SpinBox.setMaximum(255)
        self.Green_Label = QLabel(self.Datos_GroupBox)
        self.Green_Label.setObjectName(u"Green_Label")
        self.Green_Label.setGeometry(QRect(10, 220, 51, 21))
        self.Red_SpinBox = QSpinBox(self.Datos_GroupBox)
        self.Red_SpinBox.setObjectName(u"Red_SpinBox")
        self.Red_SpinBox.setGeometry(QRect(20, 190, 51, 22))
        self.Red_SpinBox.setMaximum(255)
        self.DestinoY_SpinBox = QSpinBox(self.Datos_GroupBox)
        self.DestinoY_SpinBox.setObjectName(u"DestinoY_SpinBox")
        self.DestinoY_SpinBox.setGeometry(QRect(20, 90, 51, 22))
        self.DestinoY_SpinBox.setMaximum(500)
        self.Red_Label = QLabel(self.Datos_GroupBox)
        self.Red_Label.setObjectName(u"Red_Label")
        self.Red_Label.setGeometry(QRect(10, 170, 51, 21))
        self.DestinoX_SpinBox = QSpinBox(self.Datos_GroupBox)
        self.DestinoX_SpinBox.setObjectName(u"DestinoX_SpinBox")
        self.DestinoX_SpinBox.setGeometry(QRect(21, 40, 51, 21))
        self.DestinoX_SpinBox.setMaximum(500)
        self.Blue_Label = QLabel(self.Datos_GroupBox)
        self.Blue_Label.setObjectName(u"Blue_Label")
        self.Blue_Label.setGeometry(QRect(10, 270, 51, 21))
        self.DestinoY_Label = QLabel(self.Datos_GroupBox)
        self.DestinoY_Label.setObjectName(u"DestinoY_Label")
        self.DestinoY_Label.setGeometry(QRect(10, 70, 51, 21))
        self.Green_SpinBox = QSpinBox(self.Datos_GroupBox)
        self.Green_SpinBox.setObjectName(u"Green_SpinBox")
        self.Green_SpinBox.setGeometry(QRect(20, 240, 51, 22))
        self.Green_SpinBox.setMaximum(255)
        self.Velocidad_Label = QLabel(self.Datos_GroupBox)
        self.Velocidad_Label.setObjectName(u"Velocidad_Label")
        self.Velocidad_Label.setGeometry(QRect(10, 120, 51, 21))
        self.DestinoX_Label = QLabel(self.Datos_GroupBox)
        self.DestinoX_Label.setObjectName(u"DestinoX_Label")
        self.DestinoX_Label.setGeometry(QRect(10, 20, 51, 21))
        self.Velocidad_SpinBox = QSpinBox(self.Datos_GroupBox)
        self.Velocidad_SpinBox.setObjectName(u"Velocidad_SpinBox")
        self.Velocidad_SpinBox.setGeometry(QRect(20, 140, 51, 22))

        self.gridLayout_2.addWidget(self.Datos_GroupBox, 0, 0, 2, 1)

        self.Contenido_PlainTextEdit = QPlainTextEdit(self.Particulas_GroupBox)
        self.Contenido_PlainTextEdit.setObjectName(u"Contenido_PlainTextEdit")

        self.gridLayout_2.addWidget(self.Contenido_PlainTextEdit, 0, 1, 1, 3)

        self.AgregarInicio_PushButton = QPushButton(self.Particulas_GroupBox)
        self.AgregarInicio_PushButton.setObjectName(u"AgregarInicio_PushButton")

        self.gridLayout_2.addWidget(self.AgregarInicio_PushButton, 1, 1, 1, 1)

        self.AgregarFinal_PushButton = QPushButton(self.Particulas_GroupBox)
        self.AgregarFinal_PushButton.setObjectName(u"AgregarFinal_PushButton")

        self.gridLayout_2.addWidget(self.AgregarFinal_PushButton, 1, 2, 1, 1)

        self.Mostrar_PushButon = QPushButton(self.Particulas_GroupBox)
        self.Mostrar_PushButon.setObjectName(u"Mostrar_PushButon")

        self.gridLayout_2.addWidget(self.Mostrar_PushButon, 1, 3, 1, 1)


        self.gridLayout.addWidget(self.Particulas_GroupBox, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Buscar_LineEdit = QLineEdit(self.tab_2)
        self.Buscar_LineEdit.setObjectName(u"Buscar_LineEdit")

        self.gridLayout_4.addWidget(self.Buscar_LineEdit, 1, 0, 2, 1)

        self.tableWidget = QTableWidget(self.tab_2)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_4.addWidget(self.tableWidget, 0, 0, 1, 3)

        self.MostrarTabla_PushButton = QPushButton(self.tab_2)
        self.MostrarTabla_PushButton.setObjectName(u"MostrarTabla_PushButton")

        self.gridLayout_4.addWidget(self.MostrarTabla_PushButton, 1, 2, 2, 1)

        self.Buscar_PushButton = QPushButton(self.tab_2)
        self.Buscar_PushButton.setObjectName(u"Buscar_PushButton")

        self.gridLayout_4.addWidget(self.Buscar_PushButton, 1, 1, 2, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.Particulas_GroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.Datos_GroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Datos", None))
        self.Green_Label.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.Red_Label.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.Blue_Label.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.DestinoY_Label.setText(QCoreApplication.translate("MainWindow", u"Destino Y", None))
        self.Velocidad_Label.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.DestinoX_Label.setText(QCoreApplication.translate("MainWindow", u"Destino X", None))
        self.AgregarInicio_PushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.AgregarFinal_PushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.Mostrar_PushButon.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.Buscar_LineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identificador de Particua", None))
        self.MostrarTabla_PushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.Buscar_PushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

