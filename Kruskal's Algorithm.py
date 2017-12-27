class Graph:
    def __init__(self,vertice):
        self.V = vertice
        self.graph = []

    def kruskalMST(self):

        result = []

        i = 0 # an index variable, used for sorted edges
        r = 0 # an index variable, used for result[]

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = [] ; rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while r < self.V -1:
            u,v,w = self.graph[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)

            if x != y:
                r = r + 1
                result.append([u,v,w])
                self.union(parent, rank, x, y)

        for u,v,weight in result:
            print("%d -- %d == %d" %(u,v,weight))

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])

    def union(self, parent, rank, a, b):
        rootA = self.search(parent, a)
        rootB = self.search(parent, b)

        if rank [rootA] < [rootB]:
            parent[rootA] = rootB

        elif rank [rootA] > rank[rootB]:
            parent[rootB] = rootA

        else:
            parent[rootB] = rootA
            rank [rootA] += 1


g = Graph(4)
dataSet = []
for k in input().split(","):
    dataSet.append(k)
    if len(dataSet) % 3 == 0:
        g.addEdge(int(dataSet[k]), int(dataSet[k+1]), int(dataSet[k+2]))

g.kruskalMST()
