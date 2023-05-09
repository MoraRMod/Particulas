import json
import heapq

def calcularMSTDesdeNodo(nodo_inicio):
    # Leer archivo JSON y crear lista de diccionarios
    with open("grafo.json", "r") as f:
        grafo_json = json.load(f)

    # Crear grafo como un diccionario de listas de tuplas
    grafo = {}
    for arista in grafo_json:
        origen = (arista["origen"]["x"], arista["origen"]["y"])
        destino = (arista["destino"]["x"], arista["destino"]["y"])
        peso = arista["velocidad"]

        if origen not in grafo:
            grafo[origen] = []

        if destino not in grafo:
            grafo[destino] = []

        grafo[origen].append((destino, peso))
        grafo[destino].append((origen, peso))

    # Implementar algoritmo de Prim
    aristas_mst = []
    visitados = set()
    origen = nodo_inicio
    visitados.add(origen)
    aristas = [(peso, origen, destino) for destino, peso in grafo[origen]]

    heapq.heapify(aristas)

    while aristas:
        peso, origen, destino = heapq.heappop(aristas)

        if destino not in visitados:
            visitados.add(destino)
            aristas_mst.append((origen, destino, peso))

            for vecino, peso in grafo[destino]:
                if vecino not in visitados:
                    heapq.heappush(aristas, (peso, destino, vecino))

    # Imprimir resultado
    print(f"Aristas del árbol generador mínimo desde el nodo {nodo_inicio}:")
    for origen, destino, peso in aristas_mst:
        print(f"{origen} - {destino}: {peso}")