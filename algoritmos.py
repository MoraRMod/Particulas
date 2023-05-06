import math

def distanciaEuclidiana(x_1, y_1, x_2, y_2):
    return math.sqrt(math.pow((x_2 - x_1), 2) + math.pow((y_2 - y_1), 2))

def puntosMasCercanos(puntos_list)->list:
    resultado = []

    for punto_i in puntos_list:
        one_origenX = punto_i[0]
        one_origenY = punto_i[1]

        min = 1000
        cercano = (0,0)

        for punto_j in puntos_list:
            if punto_i != punto_j:
                two_origenX = punto_j[0]
                two_origenY = punto_j[1]

                o = distanciaEuclidiana(one_origenX, one_origenY, two_origenX, two_origenY)

                if o < min:
                    min = o
                    cercano = (two_origenX, two_origenY)
                
        resultado.append((punto_i, cercano))
        
    return resultado