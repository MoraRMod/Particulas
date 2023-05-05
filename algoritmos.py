import math
from random import randint

def distanciaEuclideana(x_1, y_1, x_2, y_2):
    return math.sqrt(math.pow((x_2 - x_1), 2) + math.pow((y_2 - y_1), 2))

def getPuntos(n: int) -> list:
    puntos = []

    for i in range(n):
        x = randint(0, 500)
        y = randint(0, 500)

        punto = (x, y)
        puntos.append(punto)
    
    return puntos

def puntosMasCarcanos(puntos_list) -> list:
    resultado = []

    for punto_i in puntos_list:
        x1 = punto_i[0]
        y1 = punto_i[1]
        min = 1000
        cercano = (0,0)

        for punto_j in puntos_list:
            if punto_i != punto_j:
                x2 = punto_j[0]
                y2 = punto_j[1]
                d = distanciaEuclideana(x1, y1, x2, y2)

                if d < min:
                    min = d
                    cercano = (x2, y2)
        
        resultado.append((punto_i, cercano))
    
    return resultado
        