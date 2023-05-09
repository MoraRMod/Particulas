from disjoinset import DisjointSet
import json

def kruskalAlgorithm(edges, n):
	# Almacena los bordes presentes en MST
	MST = []
        
	# Crea un conjunto singleton para cada elemento del universo.
	ds = DisjointSet()
	ds.makeSet(n)

	index = 0
	# Ordena los bordes aumentando el peso
	edges.sort(key=lambda x: x[2])
        
	# MST contiene exactamente aristas `V-1`
	while len(MST) != n - 1:    
		# Considerar el borde siguiente con peso mínimo del graph
		(src, dest, weight) = edges[index]
		index = index + 1        
		# Encontrar la raíz de los conjuntos a los que se unen dos extremos
        # vértices de la siguiente arista pertenecen
		x = ds.find(src)
		y = ds.find(dest)        
		# Si ambos extremos tienen diferentes padres, pertenecen a
        # diferentes componentes conectados y se pueden incluir en MST
		if x != y:
			MST.append((src, dest, weight))
			ds.union(x, y)

	return MST

def runKruskal(filepath):
        edges = []
        
        with open(filepath) as f:
            data = json.load(f)
            n = len(data)
            
            for i in range(n):
                for j in range(i+1, n):
                    origen = (data[i]['origen']['x'], data[i]['origen']['y'])
                    destino = (data[j]['origen']['x'], data[j]['origen']['y'])
                    distancia = ((origen[0]-destino[0])**2 + (origen[1]-destino[1])**2)**0.5
                    
                    edges.append((i, j, distancia))    
        # grafo de construcción
        e = kruskalAlgorithm(edges, n)

        return e