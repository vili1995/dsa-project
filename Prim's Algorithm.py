import sys

class Graph ():
    def __init__(self, vertice):
        self.V = vertice
        self.graph = [[0 for column in range(vertice)]
                      for row in range(vertice)]

    def primMST(self):
        key = [sys.maxint] * self.V
        parent = [None] * self.V
        key[0] = 0
        mst = [False] * self.V
        parent[0] = -1

        for count in range(self.V):
            u = self.minKey(key, mst)

            mst [u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and mst[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        self.printMST(parent)

    def minKey(self, key,mst):
        min = sys.maxint

        for v in range(self.V):
            if key[v] < min and mst[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def printMST(self, parent):
        print "Edge\tWeight"
        for k in range(1,self.V):
            print parent[k], "-",k,"\t",self.graph[k][parent[k]]


g = Graph(5)
g.graph = [[1, 2, 3, 6, 8],
           [2, 0, 3, 8, 5],
           [6, 3, 0, 4, 7],
           [6, 8, 1, 8, 9],
           [0, 5, 7, 9, 0],
           ]

g.primMST();
