import heapq
import json

def prim(filepath):
    # Leer archivo JSON y crear grafo como un diccionario de listas de tuplas
    with open(filepath, "r") as f:
        data = json.load(f)
        grafo = {}
        for arista in data:
            origen = arista["source"]
            destino = arista["dest"]
            peso = arista["weight"]

            if origen not in grafo:
                grafo[origen] = []

            if destino not in grafo:
                grafo[destino] = []

            grafo[origen].append((destino, peso))
            grafo[destino].append((origen, peso))

    # Implementar algoritmo de Prim
    visitados = set()
    origen = list(grafo.keys())[0]
    destino = list(grafo.keys())[-1]
    visitados.add(origen)
    aristas = [(peso, origen, destino) for destino, peso in grafo[origen]]

    heapq.heapify(aristas)

    while aristas:
        peso, origen, destino = heapq.heappop(aristas)

        if destino not in visitados:
            visitados.add(destino)

            if destino == destino:
                break

            for vecino, peso in grafo[destino]:
                if vecino not in visitados:
                    heapq.heappush(aristas, (peso, destino, vecino))

    return f"Árbol generador mínimo:\n({origen}, {destino}): {peso}"