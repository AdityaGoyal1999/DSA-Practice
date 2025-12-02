class DisjointSet:

    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
    
    def find(self, node):
        if self.parent[node] == node:
            return node
        
        ultimate_parent = self.find(self.parent[node])
        self.parent[node] = ultimate_parent
        return ultimate_parent

    def union(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)

        if parent_u == parent_v:
            return

        if self.rank[parent_u] < self.rank[parent_v]:
            self.parent[parent_u] = parent_v
        elif self.rank[parent_u] > self.rank[parent_v]:
            self.parent[parent_v] = parent_u
        else:
            self.parent[parent_u] = parent_v
            self.rank[parent_v] += 1


ds = DisjointSet(5)

# 0 - 1 - 2 - 3 - 4

ds.union(1, 2)
ds.union(3, 4)

print(ds.find(1) == ds.find(3))

ds.union(2, 3)
print(ds.find(1) == ds.find(3))

# For the path compression version, instead of calculating the parent for a node each time, mark the immediate parent of a node as the ultimate parent.
# this is a memoization technique that can fasten up the complexity of Find. 