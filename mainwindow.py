from PySide2.QtWidgets import *
from PySide2.QtCore import Slot
from PySide2.QtGui import *
from ui_mainwindow import Ui_MainWindow
from cumulo import Cumulo
from particula import Particula
from algoritmos import puntosMasCercanos
from kruskal import kruskalAlgorithm, runKruskal
from pprint import pprint

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.cumulo = Cumulo()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.scene = QGraphicsScene()
        self.ui.Grafica_GraphicsView.setScene(self.scene)


        self.ui.AgregarInicio_PushButton.clicked.connect(self.agregarInicio)
        self.ui.AgregarFinal_PushButton.clicked.connect(self.agregarFinal)
        self.ui.Mostrar_PushButon.clicked.connect(self.mostrar)

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

        self.ui.Grafo_PushButton.clicked.connect(self.mostrarGrafo)

        self.ui.Kruskal_PushButton.clicked.connect(self.kruskal)

    @Slot()
    def agregarInicio(self):
        id = self.ui.ID_LineEdit.text()
        origenX = self.ui.OrigenX_SpinBox.value()
        origenY = self.ui.OrigenY_SpinBox.value()
        destinoX = self.ui.DestinoX_SpinBox.value()
        destinoY = self.ui.DestinoY_SpinBox.value()
        red = self.ui.Red_SpinBox.value()
        green = self.ui.Green_SpinBox.value()
        blue = self.ui.Blue_SpinBox.value()
        velocidad = self.ui.Velocidad_SpinBox.value()

        origen = {"x": origenX, "y": origenY}
        destino = {"x": destinoX, "y": destinoY}
        color = {"red": red, "green": green, "blue": blue}

        particula = Particula(id, origen, destino, color, velocidad)
        self.cumulo.agregarInicio(particula)

    @Slot()
    def agregarFinal(self):
        id = self.ui.ID_LineEdit.text()
        origenX = self.ui.OrigenX_SpinBox.value()
        origenY = self.ui.OrigenY_SpinBox.value()
        destinoX = self.ui.DestinoX_SpinBox.value()
        destinoY = self.ui.DestinoY_SpinBox.value()
        red = self.ui.Red_SpinBox.value()
        green = self.ui.Green_SpinBox.value()
        blue = self.ui.Blue_SpinBox.value()
        velocidad = self.ui.Velocidad_SpinBox.value()

        origen = {"x": origenX, "y": origenY}
        destino = {"x": destinoX, "y": destinoY}
        color = {"red": red, "green": green, "blue": blue}

        particula = Particula(id, origen, destino, color, velocidad)
        self.cumulo.agregarFinal(particula)

    @Slot()
    def mostrar(self):
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

                origen = "(" + str(particula.origenX) + ", " + str(particula.origenY) + ")"
                destino = "(" + str(particula.destinoX) + ", " + str(particula.destinoY) + ")"
                color = "(" + str(particula.red) + ", " + str(particula.green) + ", " + str(particula.blue) + ")"

                id_widget = QTableWidgetItem(str(particula.id))
                origen_widget = QTableWidgetItem(origen)
                destino_widget = QTableWidgetItem(destino)
                color_widget = QTableWidgetItem(color)
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                distancia_widget = QTableWidgetItem(str(particula.distancia))

                self.ui.Tablita_TableWidget.setItem(0, 0, id_widget)
                self.ui.Tablita_TableWidget.setItem(0, 1, origen_widget)
                self.ui.Tablita_TableWidget.setItem(0, 2, destino_widget)
                self.ui.Tablita_TableWidget.setItem(0, 3, color_widget)
                self.ui.Tablita_TableWidget.setItem(0, 4, velocidad_widget)
                self.ui.Tablita_TableWidget.setItem(0, 5, distancia_widget)

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
        self.ui.Tablita_TableWidget.setColumnCount(6)

        headers = ["ID", "Origen", "Destino", "Color", "Velocidad", "Distancia"]

        self.ui.Tablita_TableWidget.setHorizontalHeaderLabels(headers)
        self.ui.Tablita_TableWidget.setRowCount(len(self.cumulo))

        row = 0
        for particula in self.cumulo:
            origen = "(" + str(particula.origenX) + ", " + str(particula.origenY) + ")"
            destino = "(" + str(particula.destinoX) + ", " + str(particula.destinoY) + ")"
            color = "(" + str(particula.red) + ", " + str(particula.green) + ", " + str(particula.blue) + ")"

            id_widget = QTableWidgetItem(str(particula.id))
            origen_widget = QTableWidgetItem(origen)
            destino_widget = QTableWidgetItem(destino)
            color_widget = QTableWidgetItem(color)
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.Tablita_TableWidget.setItem(row, 0, id_widget)
            self.ui.Tablita_TableWidget.setItem(row, 1, origen_widget)
            self.ui.Tablita_TableWidget.setItem(row, 2, destino_widget)
            self.ui.Tablita_TableWidget.setItem(row, 3, color_widget)
            self.ui.Tablita_TableWidget.setItem(row, 4, velocidad_widget)
            self.ui.Tablita_TableWidget.setItem(row, 5, distancia_widget)

            row += 1
    
    @Slot()
    def dibujarEscena(self):
        pen = QPen()
        pen.setWidth(2)

        for particula in self.cumulo:
            origenX = int(particula.origenX)
            origenY = int(particula.origenY)
            destinoX = int(particula.destinoX)
            destinoY = int(particula.destinoY)
            red = int(particula.red)
            green = int(particula.green)
            blue = int(particula.blue)

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

        for particula in self.cumulo:
            origenX = int(particula.origenX)
            origenY = int(particula.origenY)
            destinoX = int(particula.destinoX)
            destinoY = int(particula.destinoY)
            red = int(particula.red)
            green = int(particula.green)
            blue = int(particula.blue)

            color = QColor(red, green, blue)
            pen.setColor(color)

            self.scene.addEllipse(origenX, origenY, 6, 6, pen)
            self.scene.addEllipse(destinoX, destinoY, 6, 6, pen)
        
    @Slot()
    def fuerzaBruta(self):
        puntos = []
        pen = QPen()
        pen.setWidth(2)

        for particula in self.cumulo:
            p1 = (particula.origenX, particula.origenY, particula.destinoY, particula.destinoY)
            p2 = (particula.origenX, particula.origenY, particula.destinoY, particula.destinoY)

            puntos.append(p1)
            puntos.append(p2)
        
        res = puntosMasCercanos(puntos)

        for particula in self.cumulo:
            color = QColor(particula.red, particula.green, particula.blue)
            pen.setColor(color)

            for punto1, punto2 in res:
                origenX = punto1[0]
                origenY = punto1[1]
                destinoX = punto2[0]
                destinoY = punto2[1]

                self.scene.addLine(origenX, origenY, destinoX, destinoY, pen)
    
    @Slot()
    def mostrarGrafo(self):
        grafo = {}

        for particula in self.cumulo:
            origen = (particula.origenX, particula.origenY)
            destino = (particula.destinoX, particula.destinoY)
            distancia = int(particula.distancia)

            if origen not in grafo:
                grafo[origen] = []

            grafo[origen].append([destino, distancia])

            if destino not in grafo:
                grafo[destino] = []

            grafo[destino].append([origen, distancia])

        pprint(str(grafo))
        self.ui.Contenido_PlainTextEdit.clear()
        self.ui.Contenido_PlainTextEdit.insertPlainText(str(grafo))

    @Slot()
    def kruskal(self):
        res = runKruskal('particulas.json')

        self.ui.Contenido_PlainTextEdit.clear()
        self.ui.Contenido_PlainTextEdit.insertPlainText(str(res))