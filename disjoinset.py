class DisjointSet:
	parent = {}

	def makeSet(self, n):
		for i in range(n):
			self.parent[i] = i

	def find(self, k):
		if self.parent[k] == k:
			return k

		return self.find(self.parent[k])

	def union(self, a, b):
		x = self.find(a)
		y = self.find(b)

		self.parent[x] = y