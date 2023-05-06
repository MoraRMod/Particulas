from algoritmos import distanciaEuclideana

class Particula:
    def __init__(self, id = 0, origen = None, destino = None, color = None, velocidad = 0) -> None:
        self.__id = id

        if origen is None:
            self.__origenX = 0
            self.__origenY = 0
        else:
            self.__origenX = origen["x"]
            self.__origenY = origen["y"]

        if destino is None:
            self.__destinoX = 0
            self.__destinoY = 0
        else:
            self.__destinoX = destino["x"]
            self.__destinoY = destino["y"]

        if color is None:
            self.__red = 0
            self.__green = 0
            self.__blue = 0
        else:
            self.__red = color["red"]
            self.__green = color["green"]
            self.__blue = color["blue"]

        self.__velocidad = velocidad
        self.__distancia = distanciaEuclideana(self.__origenX, self.__origenY, self.__destinoX, self.__destinoY)
		
    def __str__(self):
        return(
            "Identificador: " + str(self.__id) + "\n" +
            "OrigenX: " + str(self.__origenX) + "\n" +
            "OrigenY: " + str(self.__origenY) + "\n" +
            "DestinoX: " + str(self.__destinoX) + "\n" +
            "DestinoY: " + str(self.__destinoY )+ "\n" +
            "Red: " + str(self.__red) + "\n" +
            "Green: " + str(self.__green) + "\n" +
            "Blue: " + str(self.__blue) + "\n" +
            "Velocidad: " + str(self.__velocidad) + "\n" +
            "Distancia: " + str(self.__distancia) + "\n"
        )
    
    def to_dict(self):
        return {
            "id": self.__id,
            "origen": {
                "x": self.__origenX,
                "y": self.__origenY
            },
            "destino": {
                "x": self.__destinoX,
                "y": self.__destinoY
            },
            "color": {
                "red": self.__red,
                "green": self.__green,
                "blue": self.__blue
            },
            "velocidad": self.__velocidad
        }
    
    @property
    def id(self):
        return self.__id

    @property
    def origenX(self):
        return self.__origenX
    
    @property
    def origenY(self):
        return self.__origenY

    @property
    def destinoX(self):
        return self.__destinoX
    
    @property
    def destinoY(self):
        return self.__destinoY
    
    @property
    def red(self):
        return self.__red
    
    @property
    def green(self):
        return self.__green
    
    @property
    def blue(self):
        return self.__blue
    
    @property
    def velocidad(self):
        return self.__velocidad
    
    @property
    def distancia(self):
        return self.__distancia