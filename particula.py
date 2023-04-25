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
            "Identificador: " + str(self.__id) + "\n" +
            "Origen X: " + str(self.__origen_x) + "\n" +
            "Origen Y: " + str(self.__origen_y) + "\n" +
            "Destino X: " + str(self.__destino_x) + "\n" +
            "Destino Y: " + str(self.__destino_y )+ "\n" +
            "Velocidad: " + str(self.__velocidad) + "\n" +
            "Distancia: " + str(self.__distancia) + "\n"
        )
    
    def to_dict(self):
        return {
            "id": self.__id,
            "origenX": self.__origen_x,
            "origenY": self.__origen_y,
            "destinoX": self.__destino_x,
            "destinoY": self.__destino_y,
            "velocidad": self.__velocidad,
            "red": self.__red,
            "green": self.__green,
            "blue": self.__blue,
            "distancia": self.__distancia
        }