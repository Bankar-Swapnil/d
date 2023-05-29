# v=6
# 0 1 4
# 0 2 3
# 1 2 1
# 1 3 2
# 2 3 4
# 3 4 2
# 4 5 6

class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []
        
    def add_edge(self, u, v, w):
        self.graph.append((w, u, v))
        
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
            
    def kruskal(self):
        result = []
        self.graph.sort()
        parent = list(range(self.V))
        rank = [0] * self.V
        
        for edge in self.graph:
            w, u, v = edge
            if self.find(parent, u) != self.find(parent, v):
                result.append((u, v, w))
                self.union(parent, rank, u, v)
                
        for u, v, weight in result:
            print("Edge:", u, v, "-", weight)

# Take input from the user
V = int(input("Enter the number of vertices: "))
g = Graph(V)
a=0
print("Enter the edges (u v w) [separated by space]:")
while a<=V:
    edge = input().split()
    if len(edge) != 3:
        break
    u, v, w = map(int, edge)
    g.add_edge(u, v, w)
    a+=1

g.kruskal()