# G = [
#     [0, 19, 5, 0, 0, 0],
#     [19, 0, 5, 9, 2, 0],
#     [5, 5, 0, 1, 6, 0],
#     [0, 9, 1, 0, 1, 0],
#     [0, 3, 6, 1, 0, 1],
#     [0, 2, 6, 1, 0, 0]
# ]

INF = 99999999
V = int(input("Enter the number of vertices: "))

selected_node = [0] * V
selected_node[0] = True
no_edge = 0
total_weight = 0

G = []
for i in range(V):
    row = list(map(int, input(f"Enter the distances for vertex {i} (space-separated): ").split()))
    G.append(row)

while no_edge < V - 1:
    min_dist = INF
    a = 0
    b = 0

    for m in range(V):
        if selected_node[m]:
            for n in range(V):
                if not selected_node[n] and G[m][n]:
                    if min_dist > G[m][n]:
                        min_dist = G[m][n]
                        a = m
                        b = n

    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    total_weight+=G[a][b]
    selected_node[b] = True
    no_edge += 1

print("Total Weight : ",total_weight)
