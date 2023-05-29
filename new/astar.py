# The `astaralgo` function takes `start_node` and `stop_node` as input parameters.
def astaralgo(start_node, stop_node):
    # It initializes the `open_set` as a set containing the `start_node` and the `closed_set` as an empty set.
    open_set = set(start_node)
    closed_set = set()
    # It creates empty dictionaries `g` and `parents` to store the cost and parent node for each visited node.
    g = {}
    parents = {}
    # The cost from the `start_node` to itself is set to 0, and the parent of the `start_node` is itself.
    g[start_node] = 0
    parents[start_node] = start_node
    # The while loop executes until the `open_set` is not empty.
    while len(open_set) > 0:
        n = None
        # Inside the loop, it selects a node `n` with the lowest cost (`g` value + heuristic) from the `open_set`.
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        # If the selected node `n` is equal to the `stop_node` or there are no neighbors for `n` in the graph, the algorithm passes and continues to the next iteration.
        if n == stop_node or Graph_nodes[n] == None:
            pass
        # Otherwise, it iterates over the neighbors of `n` obtained from the `get_neighbors` function.
        else:
            for(m, weight) in get_neighbors(n):
                # For each neighbor `m`, it checks if `m` is not in the `open_set` and not in the `closed_set`. If true, it adds `m` to the `open_set`, sets its parent as `n`, and calculates the cost `g` from the start node to `m`.
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    # If `m` is already in the `open_set` or `closed_set`, it checks if the cost from the start node to `m` through `n` is lower than its current cost. If true, it updates the cost `g` and parent node for `m`.
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        # If `m` was in the `closed_set`, it removes it from the `closed_set` and adds it back to the `open_set`.
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        # If `n` is `None`, it means that a path does not exist between the start and stop nodes. It prints "Path does not exist" and returns `None`.
        if n == None:
            print('Path does now exist!')
            return None
        # If `n` is equal to the `stop_node`, it means that the path has been found. It backtracks from the `stop_node` to the `start_node` using the `parents` dictionary to construct the path.
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            # The path is then reversed and printed as "Path found: [path]".
            path.reverse()
            print('Path found: {}'.format(path))
            return path
        open_set.remove(n)
        closed_set.add(n)
    # Finally, if the while loop completes without finding the stop node, it means that a path does not exist between the start and stop nodes. It prints "Path does not exist" and returns `None`.
    print('Path does not exist')
    return None

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def heuristic(n):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0

    }
    return H_dist[n]

Graph_nodes = {
    'A':[('B',2),('E',3)],
    'B':[('A',2),('C',1),('G',9)],
    'C':[('B',1)],
    'D':[('E',6),('G',1)],
    'E':[('A',3),('D',1)],
    'G':[('B',9),('D',1)]

}
astaralgo('A','G')