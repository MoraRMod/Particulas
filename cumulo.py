from particula import Particula
import json

class Cumulo:
    def __init__(self) -> None:
        self.__cumulos = []
    
    def agregar_inicio(self, particula:Particula):
        self.__cumulos.insert(0, particula)

    def agregar_final(self, particula:Particula):
        self.__cumulos.append(particula)
        
    def mostrar(self):
        for p in self.__cumulos:
            print(p)

    def ordenarID(self, particula: Particula):
        self.__cumulos.sort(key = lambda particula: particula.id)

    def ordenarDistancia(self, particula: Particula):
        self.__cumulos.sort(reverse = True, key = lambda particula: particula.distancia)
    
    def ordenarVelocidad(self, particula: Particula):
        self.__cumulos.sort(key = lambda particula: particula.velocidad)
            
    def __str__(self):
        return "".join(
            str(p) + "\n" for p in self.__cumulos
        )
    
    def __len__(self):
        return(
            len(self.__cumulos)
        )
    
    def __iter__(self):
        self.cont = 0

        return self
    
    def __next__(self):
        if self.cont < len(self.__cumulos):
            quark = self.__cumulos[self.cont]

            self.cont += 1

            return quark
        else:
            raise StopIteration
    
    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__cumulos]

                print(lista)

                json.dump(lista, archivo, indent = 4)

                return 1
        except:
            return 0
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)

                self.__cumulos = [Particula(**particula) for particula in lista]

                return 1
        except:
            return 0