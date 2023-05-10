from disjoinset import DisjointSet
import json

def kruskalAlgorithm(bordes, n):
    MST = []
        
    ds = DisjointSet()
    ds.makeSet(n)

    indice = 0
    bordes.sort(key=lambda x: x[2])
        
    while len(MST) != n - 1:    
        (src, dest, peso) = bordes[indice]
        indice = indice + 1        
        x = ds.find(src)
        y = ds.find(dest)        
        if x != y:
            MST.append((src, dest, peso))
            ds.union(x, y)
            
    return MST

def runKruskal(filepath):
    bordes = []

    with open(filepath) as f:
        data = json.load(f)
        n = len(data)

        for i in range(n):
            for j in range(i + 1, n):
                origen = (data[i]['origen']['x'], data[i]['origen']['y'])
                destino = (data[j]['origen']['x'], data[j]['origen']['y'])
                distancia = int(((origen[0] - destino[0]) ** 2 + (origen[1] - destino[1]) ** 2) ** 0.5)

                bordes.append((i, j, distancia))
    e = kruskalAlgorithm(bordes, n)

    return e