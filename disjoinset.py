# Es una clase para representar un conjunto disjunto
class DisjointSet:
	parent = {}

	def makeSet(self, n):
		# Crea "n" conjuntos disjuntos (uno para cada vértice)
		for i in range(n):
			self.parent[i] = i

	# Encuentra la raíz del conjunto al que pertenece el elemento "k"
	def find(self, k):
		if self.parent[k] == k:
			return k

		# Recurre para el padre hasta que encontramos la raíz
		return self.find(self.parent[k])

	# Realiza la unión de dos subconjuntos
	def union(self, a, b):
		# Encontrar la raíz de los conjuntos a los que pertenecen los elementos "x" y "y"
		x = self.find(a)
		y = self.find(b)

		self.parent[x] = y