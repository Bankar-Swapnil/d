# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }
visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Take graph input from the user
graph = {}
num_nodes = int(input("Enter the number of nodes: "))

for i in range(num_nodes):
    node = input(f"Enter node {i}: ")
    connections = input(f"Enter the connected nodes for {node} (comma-separated): ")
    graph[node] = connections.split(',')

# Take starting node input from the user
start_node = input("Enter the starting node: ")
print('Depth first search:')
dfs(visited, graph, start_node)
