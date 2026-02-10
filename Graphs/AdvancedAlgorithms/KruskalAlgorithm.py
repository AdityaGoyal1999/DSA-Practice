class DisjointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size
    
    def find(self, node):
        if self.parent[node] == node:
            return node
        
        ultimate_parent = self.find(self.parent[node])
        self.parent[node] = ultimate_parent
        return ultimate_parent
    
    def union(self, u, v) -> None:
        parent_u = self.find(u)
        parent_v = self.find(v)

        if parent_u == parent_v:
            return False
        
        if self.size[parent_u] < self.size[parent_v]:
            self.parent[parent_u] = parent_v
            self.size[parent_v] += self.size[parent_u]
        elif self.size[parent_u] > self.size[parent_v]:
            self.parent[parent_v] = parent_u
            self.size[parent_u] += self.size[parent_u]
        else:
            self.parent[parent_u] = parent_v
            self.size[parent_v] += self.size[parent_u]
        return True

def kruskal(edges, V):
    """
    edges: list of edges in the graph
    V: number of vertices in the graph
    """
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(V)
    cost = 0
    num_edges = 0

    i  = 0
    while num_edges < V - 1 or i < len(edges):
        u, v, w = edges[i]
        if ds.union(u, v):  
            cost += w
            num_edges += 1
        i += 1
    return cost

edges = [[0, 1, 10], [1, 3, 15], [2, 3, 4], [2, 0, 6], [0, 3, 5]]
V = 4
print(kruskal(edges, V) == 19)  

# O(E log E + E log V) - O(E + V)