# graph = [[0, 1, 1, 1],
#          [1, 0, 1, 0],
#          [1, 1, 0, 1],
#          [1, 0, 1, 0]]
# num_colors = 3
def graph_coloring(graph, num_colors):
    colors = [0] * len(graph)
    if not graph_coloring_helper(graph, num_colors, colors, 0):
        return None
    return colors

def graph_coloring_helper(graph, num_colors, colors, v):
    if v == len(graph):
        return True
    for c in range(1, num_colors+1):
        if is_safe(graph, colors, v, c):
            colors[v] = c
            if graph_coloring_helper(graph, num_colors, colors, v+1):
                return True
            colors[v] = 0
    return False

def is_safe(graph, colors, v, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and colors[i] == c:
            return False
    return True

n = int(input("Enter the number of vertices: "))
graph = []
print("Enter the adjacency matrix:")
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

num_colors = int(input("Enter the number of colors: "))

colors = graph_coloring(graph, num_colors)
if colors is None:
    print("No valid coloring exists.")
else:
    print("Vertex colors:", colors)