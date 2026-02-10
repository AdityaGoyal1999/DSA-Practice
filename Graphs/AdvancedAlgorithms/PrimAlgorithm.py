import heapq

def prim(V, edges):

    adj_map = {i: [] for i in range(V)}
    for u, v, w in edges:
        adj_map[u].append((v, w))
        adj_map[v].append((u, w))
    
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, (0, 0))
    visited = set()
    cost = 0

    while heap:
        w, u = heapq.heappop(heap)

        if u in visited:
            continue
        
        cost += w
        visited.add(u)

        for v, wt in adj_map[u]:
            if v not in visited:
                heapq.heappush(heap, (wt, v))
    
    return cost

# O(E log E + E log V) - O(E + V)
V = 3
edges = [(0, 1, 5), (1, 2, 3), (0, 2, 1)]
print(prim(V, edges) == 4)