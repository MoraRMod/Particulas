from PySide2.QtWidgets import *
from PySide2.QtCore import Slot
from PySide2.QtGui import *
from ui_mainwindow import Ui_MainWindow
from cumulo import Cumulo
from particula import Particula
from algoritmos import puntosMasCarcanos
from pprint import pprint
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.cumulo = Cumulo()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.scene = QGraphicsScene()
        self.ui.Grafica_GraphicsView.setScene(self.scene)


        self.ui.AgregarInicio_PushButton.clicked.connect(self.clickAgregarInicio)
        self.ui.AgregarFinal_PushButton.clicked.connect(self.clickAgregar)
        self.ui.Mostrar_PushButon.clicked.connect(self.clickMostrar)

        self.ui.actionAbrir.triggered.connect(self.actionAbrirArchivo)
        self.ui.actionGuardar.triggered.connect(self.actionGuardarArchivo)

        self.ui.Buscar_PushButton.clicked.connect(self.buscarID)
        self.ui.MostrarTabla_PushButton.clicked.connect(self.mostrarTabla)

        self.ui.Dibujar_PushButton.clicked.connect(self.dibujarEscena)
        self.ui.Limpiar_PushButton.clicked.connect(self.limpiarEscena)

        self.ui.ID_PushButton.clicked.connect(self.ordenarID)
        self.ui.Distancia_PushButon.clicked.connect(self.ordenarDistancia)
        self.ui.Velocidad_PushButon.clicked.connect(self.ordenarVelocidad)

        self.ui.Puntos_PushButton.clicked.connect(self.dibujarPuntos)
        self.ui.FuerzaBruta_PushButton.clicked.connect(self.fuerzaBruta)


    @Slot()
    def clickAgregarInicio(self):
        id = self.ui.ID_LineEdit.text()
        origenX = self.ui.OrigenX_SpinBox.value()
        origenY = self.ui.OrigenY_SpinBox.value()
        destinoX = self.ui.DestinoX_SpinBox.value()
        destinoY = self.ui.DestinoY_SpinBox.value()
        velocidad = self.ui.Velocidad_SpinBox.value()
        red = self.ui.Red_SpinBox.value()
        green = self.ui.Green_SpinBox.value()
        blue = self.ui.Blue_SpinBox.value()

        particula = Particula(id, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue)
        self.cumulo.agregarInicio(particula)

    @Slot()
    def clickAgregar(self):
        id = self.ui.ID_LineEdit.text()
        origenX = self.ui.OrigenX_SpinBox.value()
        origenY = self.ui.OrigenY_SpinBox.value()
        destinoX = self.ui.DestinoX_SpinBox.value()
        destinoY = self.ui.DestinoY_SpinBox.value()
        velocidad = self.ui.Velocidad_SpinBox.value()
        red = self.ui.Red_SpinBox.value()
        green = self.ui.Green_SpinBox.value()
        blue = self.ui.Blue_SpinBox.value()

        particula = Particula(id, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue)
        self.cumulo.agregarFinal(particula)

    @Slot()
    def clickMostrar(self):
        self.ui.Contenido_PlainTextEdit.clear()
        self.ui.Contenido_PlainTextEdit.insertPlainText(str(self.cumulo))

    @Slot()
    def actionGuardarArchivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]

        if self.cumulo.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo crear el archivo " + ubicacion
            )
            
    @Slot()
    def actionAbrirArchivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]

        if self.cumulo.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo abrir el archivo " + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo abrir el archivo " + ubicacion
            )

    @Slot()
    def buscarID(self):
        id = self.ui.Buscar_LineEdit.text()

        encontrado = False

        for particula in self.cumulo:
            if id == str(particula.id):
                self.ui.Tablita_TableWidget.clear()
                self.ui.Tablita_TableWidget.setRowCount(1)

                id_widget = QTableWidgetItem(str(particula.id))
                origenX_widget = QTableWidgetItem(str(particula.origenX))
                origenY_widget = QTableWidgetItem(str(particula.origenY))
                destinoX_widget = QTableWidgetItem(str(particula.destinoX))
                destinoY_widget = QTableWidgetItem(str(particula.destinoY))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))

                self.ui.Tablita_TableWidget.setItem(0, 0, id_widget)
                self.ui.Tablita_TableWidget.setItem(0, 1, origenX_widget)
                self.ui.Tablita_TableWidget.setItem(0, 2, origenY_widget)
                self.ui.Tablita_TableWidget.setItem(0, 3, destinoX_widget)
                self.ui.Tablita_TableWidget.setItem(0, 4, destinoY_widget)
                self.ui.Tablita_TableWidget.setItem(0, 5, velocidad_widget)
                self.ui.Tablita_TableWidget.setItem(0, 6, red_widget)
                self.ui.Tablita_TableWidget.setItem(0, 7, green_widget)
                self.ui.Tablita_TableWidget.setItem(0, 8, blue_widget)
                self.ui.Tablita_TableWidget.setItem(0, 9, distancia_widget)

                encontrado = True

                return
            if not encontrado:
                QMessageBox.warning(
                    self,
                    "Atencion",
                    f'La particula con el identificador "{id}" no fue encontrado.'
                )

    @Slot()
    def mostrarTabla(self):
        self.ui.Tablita_TableWidget.setColumnCount(10)

        headers = ["ID", "OrigenX", "OrigenY", "DestinoX", "DestinoY", "Velocidad", "Red", "Green", "Blue", "Distancia"]

        self.ui.Tablita_TableWidget.setHorizontalHeaderLabels(headers)
        self.ui.Tablita_TableWidget.setRowCount(len(self.cumulo))

        row = 0
        for particula in self.cumulo:
            id_widget = QTableWidgetItem(str(particula.id))
            origenX_widget = QTableWidgetItem(str(particula.origenX))
            origenY_widget = QTableWidgetItem(str(particula.origenY))
            destinoX_widget = QTableWidgetItem(str(particula.destinoX))
            destinoY_widget = QTableWidgetItem(str(particula.destinoY))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.Tablita_TableWidget.setItem(row, 0, id_widget)
            self.ui.Tablita_TableWidget.setItem(row, 1, origenX_widget)
            self.ui.Tablita_TableWidget.setItem(row, 2, origenY_widget)
            self.ui.Tablita_TableWidget.setItem(row, 3, destinoX_widget)
            self.ui.Tablita_TableWidget.setItem(row, 4, destinoY_widget)
            self.ui.Tablita_TableWidget.setItem(row, 5, velocidad_widget)
            self.ui.Tablita_TableWidget.setItem(row, 6, red_widget)
            self.ui.Tablita_TableWidget.setItem(row, 7, green_widget)
            self.ui.Tablita_TableWidget.setItem(row, 8, blue_widget)
            self.ui.Tablita_TableWidget.setItem(row, 9, distancia_widget)

            row += 1
    
    @Slot()
    def dibujarEscena(self):
        pen = QPen()
        pen.setWidth(2)

        for particula in self.cumulo:
            origenX = int(self.ui.OrigenX_SpinBox.value())
            origenY = int(self.ui.OrigenY_SpinBox.value())
            destinoX = int(self.ui.DestinoX_SpinBox.value())
            destinoY = int(self.ui.DestinoY_SpinBox.value())
            red = int(self.ui.Red_SpinBox.value())
            green = int(self.ui.Green_SpinBox.value())
            blue = int(self.ui.Blue_SpinBox.value())

            color = QColor(red, green, blue)
            pen.setColor(color)

            self.scene.addEllipse(origenX, origenY, 6, 6, pen)
            self.scene.addEllipse(destinoX, destinoY, 6, 6, pen)
            self.scene.addLine(origenX, origenY, destinoX, destinoY, pen)

    @Slot()
    def limpiarEscena(self):
        self.scene.clear()

    @Slot()
    def wheelEvent(self, event):
        print(event.delta())

        if event.delta() > 0:
            self.ui.Grafica_GraphicsView.scale(1.2, 1.2)
        else:
            self.ui.Grafica_GraphicsView.scale(0.8, 0.8)

    @Slot()
    def ordenarID(self):
        self.cumulo.ordenarID(self)
    
    @Slot()
    def ordenarDistancia(self):
        self.cumulo.ordenarDistancia(self)

    @Slot()
    def ordenarVelocidad(self):
        self.cumulo.ordenarVelocidad(self)

    @Slot()
    def dibujarPuntos(self):
        pen = QPen()
        pen.setWidth(2)

        for molecula in self.cumulo:
            origenX = int(self.ui.OrigenX_SpinBox.value())
            origenY = int(self.ui.OrigenY_SpinBox.value())
            destinoX = int(self.ui.DestinoX_SpinBox.value())
            destinoY = int(self.ui.DestinoY_SpinBox.value())
            red = int(self.ui.Red_SpinBox.value())
            green = int(self.ui.Green_SpinBox.value())
            blue = int(self.ui.Blue_SpinBox.value())

            color = QColor(red, green, blue)
            pen.setColor(color)

            self.scene.addEllipse(origenX, origenY, 6, 6, pen)
            self.scene.addEllipse(destinoX, destinoY, 6, 6, pen)

    @Slot()
    def fuerzaBruta(self):
        resultado = puntosMasCarcanos(self.cumulo)
        pprint(resultado)
        for punto1, punto2 in resultado:
            x1 = punto1[0]
            y1 = punto1[1]
            x2 = punto2[0]
            y2 = punto2[1]
            
            self.scene.addLine(x1+3,y1+3,x2+3,y2+3)