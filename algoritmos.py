import math

def distanciaEuclideana(x_1, y_1, x_2, y_2):
    return math.sqrt(math.pow((x_2 - x_1), 2) + math.pow((y_2 - y_1), 2))

def puntosMasCercanos(puntos_list) -> list:
    resultado = []

    for puntoI in puntos_list:
        one_origenX = puntoI[0]
        one_origenY = puntoI[1]
        one_destinoX = puntoI[2]
        one_destinoY = puntoI[3]

        min = 1000
        cercano = (0,0)

        for puntoJ in puntos_list:
            if puntoI != puntoJ:
                two_origenX = puntoJ[0]
                two_origenY = puntoJ[1]
                two_destinoX = puntoJ[2]
                two_destinoY = puntoJ[3]

                origen = distanciaEuclideana(one_origenX, one_origenY, two_origenX, two_origenY)
                destino = distanciaEuclideana(one_destinoX, one_destinoY, two_destinoX, two_destinoY)

                if origen < min:
                    min = origen
                    cercano = (two_origenX, two_origenY, two_destinoX, two_destinoY)

                if destino < min:
                    min = destino
                    cercano = (two_destinoX, two_destinoY, two_origenX, two_origenY)
        
        resultado.append((puntoI, cercano))
    
    return resultado