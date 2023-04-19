from algoritmos import distancia_euclideana

class Particula:
    def __init__(self, id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue, distancia) -> None:
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancia_euclideana(origen_x, origen_y, destino_x, destino_y)
		
    def __str__(self):
        return(
            "Identificador: " + self.__id + "\n" +
            "Origen X: " + self.__origen_x + "\n" +
            "Origen Y: " + self.__origen_y + "\n" +
            "Destino X: " + self.__destino_x + "\n" +
            "Destino Y: " + self.__destino_y + "\n" +
            "Velocidad: " + self.__velocidad + "\n" +
            "Distancia: " + str(self.__distancia) + "\n"
        )