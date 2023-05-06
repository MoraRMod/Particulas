import math

def distanciaEuclideana(x_1, y_1, x_2, y_2):
    return math.sqrt(math.pow((x_2 - x_1), 2) + math.pow((y_2 - y_1), 2))

def puntosMasCercanos(puntos_list) -> list:
    resultado = []

    for punto_i in puntos_list:
        origenX = punto_i[0]
        origenY = punto_i[1]
        min = 1000
        cercano = (0,0)

        for punto_j in puntos_list:
            if punto_i != punto_j:
                destinoX = punto_j[0]
                destinoY = punto_j[1]
                d = distanciaEuclideana(origenX, origenY, destinoX, destinoY)

                if d < min:
                    min = d
                    cercano = (destinoX, destinoY)
        
        resultado.append((punto_i, cercano))
    
    return resultado