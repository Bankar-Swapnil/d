# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

visited = []
queue = []


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Take graph input from the user
graph = {}
num_nodes = int(input("Enter the number of nodes: "))

for i in range(num_nodes):
    node = input(f"Enter node {i+1}: ")
    connections = input(f"Enter the connected nodes for {node} (comma-separated): ")
    graph[node] = connections.split(',')

# Take starting node input from the user
start_node = input("Enter the starting node: ")
bfs(visited, graph, start_node)

# a b c d e f h n