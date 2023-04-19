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