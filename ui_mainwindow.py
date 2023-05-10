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
        self.Agregar_Tab = QWidget()
        self.Agregar_Tab.setObjectName(u"Agregar_Tab")
        self.gridLayout = QGridLayout(self.Agregar_Tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Particulas_GroupBox = QGroupBox(self.Agregar_Tab)
        self.Particulas_GroupBox.setObjectName(u"Particulas_GroupBox")
        self.gridLayout_11 = QGridLayout(self.Particulas_GroupBox)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.Contenido_PlainTextEdit = QPlainTextEdit(self.Particulas_GroupBox)
        self.Contenido_PlainTextEdit.setObjectName(u"Contenido_PlainTextEdit")
        self.Contenido_PlainTextEdit.setEnabled(True)

        self.gridLayout_11.addWidget(self.Contenido_PlainTextEdit, 0, 2, 3, 1)

        self.Datos_GroupBox = QGroupBox(self.Particulas_GroupBox)
        self.Datos_GroupBox.setObjectName(u"Datos_GroupBox")
        self.gridLayout_13 = QGridLayout(self.Datos_GroupBox)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.ID_GroupBox = QGroupBox(self.Datos_GroupBox)
        self.ID_GroupBox.setObjectName(u"ID_GroupBox")
        self.gridLayout_10 = QGridLayout(self.ID_GroupBox)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.ID_LineEdit = QLineEdit(self.ID_GroupBox)
        self.ID_LineEdit.setObjectName(u"ID_LineEdit")

        self.gridLayout_10.addWidget(self.ID_LineEdit, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.ID_GroupBox, 0, 0, 1, 3)

        self.Origen_GroupBox = QGroupBox(self.Datos_GroupBox)
        self.Origen_GroupBox.setObjectName(u"Origen_GroupBox")
        self.gridLayout_6 = QGridLayout(self.Origen_GroupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.OrigenX_SpinBox = QSpinBox(self.Origen_GroupBox)
        self.OrigenX_SpinBox.setObjectName(u"OrigenX_SpinBox")
        self.OrigenX_SpinBox.setMaximum(500)

        self.gridLayout_6.addWidget(self.OrigenX_SpinBox, 0, 1, 1, 1)

        self.OrigenY_SpinBox = QSpinBox(self.Origen_GroupBox)
        self.OrigenY_SpinBox.setObjectName(u"OrigenY_SpinBox")
        self.OrigenY_SpinBox.setMaximum(500)

        self.gridLayout_6.addWidget(self.OrigenY_SpinBox, 0, 3, 1, 1)

        self.OrigenX_Label = QLabel(self.Origen_GroupBox)
        self.OrigenX_Label.setObjectName(u"OrigenX_Label")

        self.gridLayout_6.addWidget(self.OrigenX_Label, 0, 0, 1, 1)

        self.OrigenY_Label = QLabel(self.Origen_GroupBox)
        self.OrigenY_Label.setObjectName(u"OrigenY_Label")

        self.gridLayout_6.addWidget(self.OrigenY_Label, 0, 2, 1, 1)


        self.gridLayout_13.addWidget(self.Origen_GroupBox, 1, 0, 1, 2)

        self.Velocidad_GroupBox = QGroupBox(self.Datos_GroupBox)
        self.Velocidad_GroupBox.setObjectName(u"Velocidad_GroupBox")
        self.gridLayout_12 = QGridLayout(self.Velocidad_GroupBox)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.Velocidad_SpinBox = QSpinBox(self.Velocidad_GroupBox)
        self.Velocidad_SpinBox.setObjectName(u"Velocidad_SpinBox")

        self.gridLayout_12.addWidget(self.Velocidad_SpinBox, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.Velocidad_GroupBox, 3, 0, 1, 3)

        self.Color_GroupBox = QGroupBox(self.Datos_GroupBox)
        self.Color_GroupBox.setObjectName(u"Color_GroupBox")
        self.gridLayout_7 = QGridLayout(self.Color_GroupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.Green_SpinBox = QSpinBox(self.Color_GroupBox)
        self.Green_SpinBox.setObjectName(u"Green_SpinBox")
        self.Green_SpinBox.setMaximum(255)

        self.gridLayout_7.addWidget(self.Green_SpinBox, 2, 1, 1, 1)

        self.Red_SpinBox = QSpinBox(self.Color_GroupBox)
        self.Red_SpinBox.setObjectName(u"Red_SpinBox")
        self.Red_SpinBox.setMaximum(255)

        self.gridLayout_7.addWidget(self.Red_SpinBox, 0, 1, 2, 1)

        self.Green_Label = QLabel(self.Color_GroupBox)
        self.Green_Label.setObjectName(u"Green_Label")

        self.gridLayout_7.addWidget(self.Green_Label, 2, 0, 1, 1)

        self.Red_Label = QLabel(self.Color_GroupBox)
        self.Red_Label.setObjectName(u"Red_Label")

        self.gridLayout_7.addWidget(self.Red_Label, 0, 0, 2, 1)

        self.Blue_SpinBox = QSpinBox(self.Color_GroupBox)
        self.Blue_SpinBox.setObjectName(u"Blue_SpinBox")
        self.Blue_SpinBox.setMaximum(255)

        self.gridLayout_7.addWidget(self.Blue_SpinBox, 3, 1, 2, 1)

        self.Blue_Label = QLabel(self.Color_GroupBox)
        self.Blue_Label.setObjectName(u"Blue_Label")

        self.gridLayout_7.addWidget(self.Blue_Label, 3, 0, 2, 1)


        self.gridLayout_13.addWidget(self.Color_GroupBox, 1, 2, 2, 1)

        self.Destino_GroupBox = QGroupBox(self.Datos_GroupBox)
        self.Destino_GroupBox.setObjectName(u"Destino_GroupBox")
        self.gridLayout_2 = QGridLayout(self.Destino_GroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.DestinoX_Label = QLabel(self.Destino_GroupBox)
        self.DestinoX_Label.setObjectName(u"DestinoX_Label")

        self.gridLayout_2.addWidget(self.DestinoX_Label, 0, 0, 1, 1)

        self.DestinoX_SpinBox = QSpinBox(self.Destino_GroupBox)
        self.DestinoX_SpinBox.setObjectName(u"DestinoX_SpinBox")
        self.DestinoX_SpinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.DestinoX_SpinBox, 0, 1, 1, 1)

        self.DestinoY_Label = QLabel(self.Destino_GroupBox)
        self.DestinoY_Label.setObjectName(u"DestinoY_Label")

        self.gridLayout_2.addWidget(self.DestinoY_Label, 0, 2, 1, 1)

        self.DestinoY_SpinBox = QSpinBox(self.Destino_GroupBox)
        self.DestinoY_SpinBox.setObjectName(u"DestinoY_SpinBox")
        self.DestinoY_SpinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.DestinoY_SpinBox, 0, 3, 1, 1)


        self.gridLayout_13.addWidget(self.Destino_GroupBox, 2, 0, 1, 2)

        self.Ordenamiento_GroupBox = QGroupBox(self.Datos_GroupBox)
        self.Ordenamiento_GroupBox.setObjectName(u"Ordenamiento_GroupBox")
        self.gridLayout_8 = QGridLayout(self.Ordenamiento_GroupBox)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.Distancia_PushButon = QPushButton(self.Ordenamiento_GroupBox)
        self.Distancia_PushButon.setObjectName(u"Distancia_PushButon")

        self.gridLayout_8.addWidget(self.Distancia_PushButon, 1, 0, 1, 1)

        self.ID_PushButton = QPushButton(self.Ordenamiento_GroupBox)
        self.ID_PushButton.setObjectName(u"ID_PushButton")

        self.gridLayout_8.addWidget(self.ID_PushButton, 0, 0, 1, 1)

        self.Velocidad_PushButon = QPushButton(self.Ordenamiento_GroupBox)
        self.Velocidad_PushButon.setObjectName(u"Velocidad_PushButon")

        self.gridLayout_8.addWidget(self.Velocidad_PushButon, 2, 0, 1, 1)


        self.gridLayout_13.addWidget(self.Ordenamiento_GroupBox, 4, 0, 1, 1)

        self.Insertar_GroupBox = QGroupBox(self.Datos_GroupBox)
        self.Insertar_GroupBox.setObjectName(u"Insertar_GroupBox")
        self.gridLayout_9 = QGridLayout(self.Insertar_GroupBox)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.AgregarInicio_PushButton = QPushButton(self.Insertar_GroupBox)
        self.AgregarInicio_PushButton.setObjectName(u"AgregarInicio_PushButton")

        self.gridLayout_9.addWidget(self.AgregarInicio_PushButton, 0, 0, 1, 1)

        self.AgregarFinal_PushButton = QPushButton(self.Insertar_GroupBox)
        self.AgregarFinal_PushButton.setObjectName(u"AgregarFinal_PushButton")

        self.gridLayout_9.addWidget(self.AgregarFinal_PushButton, 1, 0, 1, 1)


        self.gridLayout_13.addWidget(self.Insertar_GroupBox, 4, 1, 1, 1)

        self.Mostrar_GroupBox = QGroupBox(self.Datos_GroupBox)
        self.Mostrar_GroupBox.setObjectName(u"Mostrar_GroupBox")
        self.gridLayout_14 = QGridLayout(self.Mostrar_GroupBox)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.Mostrar_PushButon = QPushButton(self.Mostrar_GroupBox)
        self.Mostrar_PushButon.setObjectName(u"Mostrar_PushButon")

        self.gridLayout_14.addWidget(self.Mostrar_PushButon, 0, 0, 1, 1)

        self.Grafo_PushButton = QPushButton(self.Mostrar_GroupBox)
        self.Grafo_PushButton.setObjectName(u"Grafo_PushButton")

        self.gridLayout_14.addWidget(self.Grafo_PushButton, 1, 0, 1, 1)


        self.gridLayout_13.addWidget(self.Mostrar_GroupBox, 4, 2, 1, 1)

        self.Algoritmos_GroupBox = QGroupBox(self.Datos_GroupBox)
        self.Algoritmos_GroupBox.setObjectName(u"Algoritmos_GroupBox")
        self.gridLayout_15 = QGridLayout(self.Algoritmos_GroupBox)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.Dijkstra_PushButton = QPushButton(self.Algoritmos_GroupBox)
        self.Dijkstra_PushButton.setObjectName(u"Dijkstra_PushButton")

        self.gridLayout_15.addWidget(self.Dijkstra_PushButton, 2, 0, 1, 1)

        self.Prim_PushButton = QPushButton(self.Algoritmos_GroupBox)
        self.Prim_PushButton.setObjectName(u"Prim_PushButton")

        self.gridLayout_15.addWidget(self.Prim_PushButton, 0, 1, 1, 1)

        self.Graham_PushButton = QPushButton(self.Algoritmos_GroupBox)
        self.Graham_PushButton.setObjectName(u"Graham_PushButton")

        self.gridLayout_15.addWidget(self.Graham_PushButton, 2, 1, 1, 1)

        self.Kruskal_PushButton = QPushButton(self.Algoritmos_GroupBox)
        self.Kruskal_PushButton.setObjectName(u"Kruskal_PushButton")

        self.gridLayout_15.addWidget(self.Kruskal_PushButton, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.Algoritmos_GroupBox, 5, 0, 1, 3)

        self.Origen_GroupBox.raise_()
        self.Destino_GroupBox.raise_()
        self.ID_GroupBox.raise_()
        self.Velocidad_GroupBox.raise_()
        self.Color_GroupBox.raise_()
        self.Ordenamiento_GroupBox.raise_()
        self.Insertar_GroupBox.raise_()
        self.Mostrar_GroupBox.raise_()
        self.Algoritmos_GroupBox.raise_()

        self.gridLayout_11.addWidget(self.Datos_GroupBox, 0, 1, 3, 1)


        self.gridLayout.addWidget(self.Particulas_GroupBox, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Agregar_Tab, "")
        self.Tabla_Tab = QWidget()
        self.Tabla_Tab.setObjectName(u"Tabla_Tab")
        self.gridLayout_4 = QGridLayout(self.Tabla_Tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.MostrarTabla_PushButton = QPushButton(self.Tabla_Tab)
        self.MostrarTabla_PushButton.setObjectName(u"MostrarTabla_PushButton")

        self.gridLayout_4.addWidget(self.MostrarTabla_PushButton, 1, 0, 1, 1)

        self.Buscar_LineEdit = QLineEdit(self.Tabla_Tab)
        self.Buscar_LineEdit.setObjectName(u"Buscar_LineEdit")

        self.gridLayout_4.addWidget(self.Buscar_LineEdit, 1, 2, 1, 1)

        self.Buscar_PushButton = QPushButton(self.Tabla_Tab)
        self.Buscar_PushButton.setObjectName(u"Buscar_PushButton")

        self.gridLayout_4.addWidget(self.Buscar_PushButton, 1, 3, 1, 1)

        self.Tablita_TableWidget = QTableWidget(self.Tabla_Tab)
        self.Tablita_TableWidget.setObjectName(u"Tablita_TableWidget")

        self.gridLayout_4.addWidget(self.Tablita_TableWidget, 0, 0, 1, 4)

        self.tabWidget.addTab(self.Tabla_Tab, "")
        self.Grafica_Tab = QWidget()
        self.Grafica_Tab.setObjectName(u"Grafica_Tab")
        self.gridLayout_5 = QGridLayout(self.Grafica_Tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.Grafica_GraphicsView = QGraphicsView(self.Grafica_Tab)
        self.Grafica_GraphicsView.setObjectName(u"Grafica_GraphicsView")

        self.gridLayout_5.addWidget(self.Grafica_GraphicsView, 0, 1, 1, 4)

        self.Limpiar_PushButton = QPushButton(self.Grafica_Tab)
        self.Limpiar_PushButton.setObjectName(u"Limpiar_PushButton")

        self.gridLayout_5.addWidget(self.Limpiar_PushButton, 1, 4, 1, 1)

        self.FuerzaBruta_PushButton = QPushButton(self.Grafica_Tab)
        self.FuerzaBruta_PushButton.setObjectName(u"FuerzaBruta_PushButton")

        self.gridLayout_5.addWidget(self.FuerzaBruta_PushButton, 1, 3, 1, 1)

        self.Puntos_PushButton = QPushButton(self.Grafica_Tab)
        self.Puntos_PushButton.setObjectName(u"Puntos_PushButton")

        self.gridLayout_5.addWidget(self.Puntos_PushButton, 1, 2, 1, 1)

        self.Dibujar_PushButton = QPushButton(self.Grafica_Tab)
        self.Dibujar_PushButton.setObjectName(u"Dibujar_PushButton")

        self.gridLayout_5.addWidget(self.Dibujar_PushButton, 1, 1, 1, 1)

        self.tabWidget.addTab(self.Grafica_Tab, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 1, 1, 1)

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

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        self.Particulas_GroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.Datos_GroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Datos", None))
        self.ID_GroupBox.setTitle(QCoreApplication.translate("MainWindow", u"ID", None))
        self.ID_LineEdit.setPlaceholderText("")
        self.Origen_GroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Origen", None))
        self.OrigenX_Label.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.OrigenY_Label.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.Velocidad_GroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.Color_GroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Color", None))
        self.Green_Label.setText(QCoreApplication.translate("MainWindow", u"G:", None))
        self.Red_Label.setText(QCoreApplication.translate("MainWindow", u"R:", None))
        self.Blue_Label.setText(QCoreApplication.translate("MainWindow", u"B:", None))
        self.Destino_GroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.DestinoX_Label.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.DestinoY_Label.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.Ordenamiento_GroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Ordenamiento", None))
        self.Distancia_PushButon.setText(QCoreApplication.translate("MainWindow", u"Distancia", None))
        self.ID_PushButton.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.Velocidad_PushButon.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.Insertar_GroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Insertar", None))
        self.AgregarInicio_PushButton.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.AgregarFinal_PushButton.setText(QCoreApplication.translate("MainWindow", u"Final", None))
        self.Mostrar_GroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.Mostrar_PushButon.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.Grafo_PushButton.setText(QCoreApplication.translate("MainWindow", u"Grafo", None))
        self.Algoritmos_GroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Algoritmos", None))
        self.Dijkstra_PushButton.setText(QCoreApplication.translate("MainWindow", u"Dijkstra", None))
        self.Prim_PushButton.setText(QCoreApplication.translate("MainWindow", u"Prim", None))
        self.Graham_PushButton.setText(QCoreApplication.translate("MainWindow", u"Graham", None))
        self.Kruskal_PushButton.setText(QCoreApplication.translate("MainWindow", u"Kruskal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Agregar_Tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.MostrarTabla_PushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.Buscar_LineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identificador de Particula", None))
        self.Buscar_PushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tabla_Tab), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.Limpiar_PushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.FuerzaBruta_PushButton.setText(QCoreApplication.translate("MainWindow", u"Fuerza Bruta", None))
        self.Puntos_PushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar Puntos", None))
        self.Dibujar_PushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar con Lineas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Grafica_Tab), QCoreApplication.translate("MainWindow", u"Gr\u00e1fica", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

