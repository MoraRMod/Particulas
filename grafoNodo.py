class Nodo:
	def __init__(self, vertice, peso = 0):
		self.vertice = vertice
		self.peso = peso
 
	def __lt__(self, other):
		return self.peso < other.peso
 
class Grafo:
	def __init__(self, borde, n):
		self.adjList = [[] for _ in range(n)]
 
		for (source, dest, peso) in borde:
			self.adjList[source].append((dest, peso))