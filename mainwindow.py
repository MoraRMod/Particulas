from PySide2.QtWidgets import *
from PySide2.QtCore import Slot
from PySide2.QtGui import *
from ui_mainwindow import Ui_Dialog
from cumulo import Cumulo
from particula import Particula
from random import randint
import math

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.cumulo = Cumulo()
        
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.AgregarInicio_PushButton.clicked.connect(self.click_agregar)
        self.ui.AgregarFinal_PushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.Mostrar_PushButon.clicked.connect(self.click_mostrar)

        self.ui.actionAbrir_2.triggered.connect(self.action_Abrir_Archivo)
        self.ui.actionGuardar_3.triggered.connect(self.action_Guardar_Archivo)

    @Slot()
    def action_Abrir_Archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]

        if self.aeropuerto.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo abrir el archivo." + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo abrir el archivo." + ubicacion
            )

    @Slot()
    def action_Guardar_Archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]

        print(ubicacion)

        if self.aeropuerto.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo." + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo crear el archivo." + ubicacion
            )
    
    @Slot()
    def click_agregar(self):
        id = randint(0, 9999)
        origenX = randint(0, 50)
        origenY = randint(0, 50)
        destinoX = self.ui.DestinoX_SpinBox.value()
        destinoY = self.ui.DestinoY_SpinBox.value()
        velocidad = self.ui.Valocidad_SpinBox.value()
        red = self.ui.Red_SpinBox.value()
        green = self.ui.Green_SpinBox.value()
        blue = self.ui.Blue_SpinBox.value()
        distancia = math.sqrt((destinoX - origenX)^2 + (destinoY - origenY)^2)

        particula = Particula(id, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue, distancia)
        self.cumulo.agregar_final(particula)


    
    @Slot()
    def click_agregar_inicio(self):
        id = randint(0, 9999)
        origenX = randint(0, 50)
        origenY = randint(0, 50)
        destinoX = self.ui.DestinoX_SpinBox.value()
        destinoY = self.ui.DestinoY_SpinBox.value()
        velocidad = self.ui.Valocidad_SpinBox.value()
        red = self.ui.Red_SpinBox.value()
        green = self.ui.Green_SpinBox.value()
        blue = self.ui.Blue_SpinBox.value()
        distancia = math.sqrt((destinoX - origenX)^2 + (destinoY - origenY)^2)

        particula = Particula(id, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue, distancia)
        self.cumulo.agregar_inicio(particula)

    @Slot()
    def click_mostrar(self):
        self.ui.Contenido_PlainTextEdit.clear()
        self.ui.Contenido_PlainTextEdit.insertPlainText(str(self.cumulo))