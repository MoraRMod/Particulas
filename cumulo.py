from particula import Particula
import json

class Cumulo:
    def __init__(self) -> None:
        self.__cumulos = []
    
    def agregar_final(self, particula:Particula):
        print('Se agrega al final.')
        self.__cumulos.append(particula)
    
    def agregar_inicio(self, particula:Particula):
        print('Se agrega al inicio.')
        self.__cumulos.insert(0,particula)
        

    def mostrar(self):
        for particula in self.__cumulos:
            print(particula)
            
    def __str__(self):
        return "".join(
            str(c) + "\n" for c in self.__cumulos
        )
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)

                self.__cumulos = [Particula(**particula) for particula in lista]
        except:
            return 0
    
    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [Particula.to_dict() for Particula in self.__cumulos]

                print(lista)

                json.dump(lista, archivo, indent = 4)
        except:
            return 0
    
cumulo = Cumulo()
cumulo.mostrar()