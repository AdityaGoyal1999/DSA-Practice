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
            return 
        
        if self.size[parent_u] < self.size[parent_v]:
            self.parent[parent_u] = parent_v
            self.size[parent_v] += self.size[parent_u]
        elif self.size[parent_u] > self.size[parent_v]:
            self.parent[parent_v] = parent_u
            self.size[parent_u] += self.size[parent_u]
        else:
            self.parent[parent_u] = parent_v
            self.size[parent_v] += self.size[parent_u]

ds = DisjointSet(5)

# 0 - 1 - 2 - 3 - 4

ds.union(1, 2)
ds.union(3, 4)

print(ds.find(1) == ds.find(3))

ds.union(2, 3)
print(ds.find(1) == ds.find(3)) 
        
# O(n) - O(n)