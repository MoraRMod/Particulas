import sys
import json
from heapq import heappop, heappush
from grafoNodo import *

def ruta(prev, i, route):
    if i >= 0:
        ruta(prev, prev[i], route)
        route.append(i)

def caminoDijkstra(Grafo, source, n):
    # Crea un min-heap y empuja el nodo de origen con una distancia de 0
    pq = []
    heappush(pq, Nodo(source))
    # Establece la distancia inicial desde la fuente a "v" como infinito
    dist = [sys.maxsize] * n
    dist[source] = 0
    # Lista para rastrear vértices para los cuales ya se encontró el costo mínimo
    done = [False] * n
    done[source] = True
    # Almacena el predecesor de un vértice
    prev = [-1] * n
 
    while pq:
 
        Nodo = heappop(pq)
        u = Nodo.vertex
 
        # hacer para cada vecino "v" de "u"
        for (v, weight) in Grafo.adjList[u]:
            if not done[v] and (dist[u] + weight) < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u
                heappush(pq, Nodo(v, dist[v]))
 
        # marca el vértice "u" como hecho para que no se vuelva a recoger
        done[u] = True
 
    route = []
    for i in range(n):
        if i != source and dist[i] != sys.maxsize:
            ruta(prev, i, route)
            print(f'({source},{i}): {dist[i]}, {route}\n')
            route.clear()
 
 
def correrDijkstra(filepath):
    with open(filepath) as f:
        data = json.load(f)

    # Convertir la lista en una lista de tuplas con el mismo formato que la variable "edges"
    edges = [(int(item['source']), int(item['dest']), int(item['weight'])) for item in data]

    n = 30
    digrafo = Grafo(edges, n)

    for source in range(n):
        caminoDijkstra(digrafo, source, n)