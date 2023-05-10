import math
import json

def anguloPolar(pOne, pTwo):
	return math.atan2(pTwo[1]-pOne[1], pTwo[0]-pOne[0])

def orientacion(pOne, pTwo, pThree):
    resultado = (pTwo[1] - pOne[1]) * (pThree[0] - pTwo[0]) - (pTwo[0] - pOne[0]) * (pThree[1] - pTwo[1])
    if resultado == 0:
        return 0
    elif resultado > 0:
        return 1
    else:
        return 2

def graham(puntos):
	n = len(puntos)
	puntoMinimo = min(puntos, key=lambda x: x[1])
	puntosSinMin = [p for p in puntos if p != puntoMinimo]
        
	puntosSinMin.sort(key=lambda x: anguloPolar(puntoMinimo, x))
        
	stack = [puntoMinimo, puntosSinMin[0]]
        
	for i in range(1, n-1):
		while len(stack) > 1 and orientacion(stack[-2], stack[-1], puntosSinMin[i]) != 2:
			stack.pop()
                        
		stack.append(puntosSinMin[i])
                
	stack.append(puntos[-1])
        
	return stack

def coordenadas(filepath):
	with open(filepath) as f:
		data = json.load(f)
		coord = []

		for i in data:
			origen = (i['origen']['x'], i['origen']['y'])
			destino = (i['destino']['x'], i['destino']['y'])

			coord.append(origen)
			coord.append(destino)

		return coord