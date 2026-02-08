"""
Given a graph and a source vertex in the graph, find the shortest paths from the source to all vertices in the given graph.
"""
import heapq

def dijkstra(adj_map, source):
    """
    graph: adjacency list of the graph
    source: source vertex
    """
    n = len(adj_map)
    distances = [float("inf")] * n

    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, (0, source))

    distances[source] = 0

    while heap:
        dist, u = heapq.heappop(heap)
        if dist > distances[u]:
            continue
            
        for v, w in adj_map[u]:
            v_dist = dist + w
            if v_dist < distances[v]:
                distances[v] = v_dist
                heapq.heappush(heap, (v_dist, v))
            
    return distances

# O((V+E) log E) - O(V + E)
adj_list = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: [],
}

source = 0
result = [0, 3, 1, 4]

print(result == dijkstra(adj_list, source))