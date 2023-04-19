from particula import Particula

class Cumulo:
    def __init__(self) -> None:
        self.__cumulos = []
    
    def agregar_final(self, particula:Particula):
        self.__cumulos.append(particula)
    
    def agregar_inicio(self, particula:Particula):
        self.__cumulos.insert(0,particula)
        

    def mostrar(self):
        for particula in self.__cumulos:
            print(particula)
            
    def __str__(self):
        return "".join(
            str(c) + "\n" for c in self.__cumulos
        )