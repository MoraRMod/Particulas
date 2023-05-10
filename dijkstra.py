import sys
import json
from heapq import heappop, heappush
from grafoNodo import *

def ruta(prev, i, route):
    if i >= 0:
        ruta(prev, prev[i], route)
        route.append(i)

def caminoDijkstra(Grafo, source, n):
	pq = []

	heappush(pq, Nodo(source))
	
	dist = [sys.maxsize] * n
	dist[source] = 0
	completo = [False] * n
	completo[source] = True
	prev = [-1] * n
 
	while pq:
		nodo = heappop(pq)
		u = nodo.vertice

		for (i, peso) in Grafo.adjList[u]:
			if not completo[i] and (dist[u] + peso) < dist[i]:
				dist[i] = dist[u] + peso
				prev[i] = u

				heappush(pq, Nodo(i, dist[i]))
 
		completo[u] = True
 
	res = []
	for i in range(n):
		if i != source and dist[i] != sys.maxsize:
			route = []

			ruta(prev, i, route)
			res.append(str(f"({source},{i}): {dist[i]}"))
	
	return res
 
def correrDijkstra(archivo):
	with open(archivo) as f:
		data = json.load(f)

	edges = [(int(item['source']), int(item['dest']), int(item['weight'])) for item in data]

	n = 30
	digrafo = Grafo(edges, n)

	return [caminoDijkstra(digrafo, source, n) for source in range(n)]