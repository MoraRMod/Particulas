from algoritmos import distanciaEuclideana

class Particula:
    def __init__(self, id, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue) -> None:
        self.__id = id
        self.__origenX = origenX
        self.__origenY = origenY
        self.__destinoX = destinoX
        self.__destinoY = destinoY
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distanciaEuclideana(origenX, origenY, destinoX, destinoY)
		
    def __str__(self):
        return(
            "Identificador: " + str(self.__id) + "\n" +
            "OrigenX: " + str(self.__origenX) + "\n" +
            "OrigenY: " + str(self.__origenY) + "\n" +
            "DestinoX: " + str(self.__destinoX) + "\n" +
            "DestinoY: " + str(self.__destinoY )+ "\n" +
            "Velocidad: " + str(self.__velocidad) + "\n" +
            "Red: " + str(self.__red) + "\n" +
            "Green: " + str(self.__green) + "\n" +
            "Blue: " + str(self.__blue) + "\n" +
            "Distancia: " + str(self.__distancia) + "\n"
        )
    
    def to_dict(self):
        return {
            "id": self.__id,
            "origenX": self.__origenX,
            "origenY": self.__origenY,
            "destinoX": self.__destinoX,
            "destinoY": self.__destinoY,
            "velocidad": self.__velocidad,
            "red": self.__red,
            "green": self.__green,
            "blue": self.__blue
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
    def velocidad(self):
        return self.__velocidad
    
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
    def distancia(self):
        return self.__distancia