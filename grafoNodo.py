class Nodo:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight
 
    def __lt__(self, other):
        return self.weight < other.weight
 
class Grafo:
    def __init__(self, edges, n):
        # Asigna memoria para la lista de adyacencia
        self.adjList = [[] for _ in range(n)]
 
        # Agrega bordes al Grafo dirigido
        for (source, dest, weight) in edges:
            self.adjList[source].append((dest, weight))