from PySide2.QtWidgets import *
from ui_mainwindow import Ui_Dialog
from PySide2.QtGui import *
from PySide2.QtCore import Slot

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.AgregarInicio_PushButton.clicked.connect(self.dibujar)
        self.ui.AgregarFinal_PushButton.clicked.connect(self.limpiar)

    @Slot()
    def dibujar(self):
        print("dibujar")
    
    @Slot()
    def limpiar(self):
        print("limpiar")