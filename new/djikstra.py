# graph = {
#     0: [(1, 4), (2, 2)],
#     1: [(0, 4), (2, 1), (3, 5)],
#     2: [(0, 2), (1, 1), (3, 8)],
#     3: [(1, 5), (2, 8)]
# }
from numpy import Inf

def Dijkstra(graph, start):
    l = len(graph)
    dist = [Inf for i in range(l)]
    dist[start] = 0
    vis = [False for i in range(l)]
    for i in range(l):
        u = -1
        for x in range(l):
            if not vis[x] and (u == -1 or dist[x] < dist[u]):
                u = x
                
        if dist[u] == Inf:
            break
            
        vis[u] = True
        
        for v, d in graph[u]:
            if dist[u] + d < dist[v]:
                dist[v] = dist[u] + d
                
    return dist

# Take graph input from the user
graph = {}
num_nodes = int(input("Enter the number of nodes: "))

for i in range(num_nodes):
    connections = input(f"Enter the connected nodes for node {i} and their distances (comma-separated): ")
    connections = connections.split(',')
    graph[i] = [(int(connections[j]), int(connections[j+1])) for j in range(0, len(connections), 2)]

# Take starting node input from the user
start_node = int(input("Enter the starting node: "))
print(Dijkstra(graph, start_node))
