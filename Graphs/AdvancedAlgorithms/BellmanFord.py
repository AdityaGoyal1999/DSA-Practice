
def bellmanFord(edges, V, source):
    dist = [float("inf")] * V
    dist[source] = 0

    for _ in range(V-1):
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = w + dist[u]
    
    for u, v, w in edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            print("Negative cycle detected")
            return None
    
    return dist

# O(V.E) - O(V)
edges = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 1, 3)]
V = 4
source = 0
result = [0, 1, 2, 3]
print(bellmanFord(edges, V, source) == result)