"""
Represent a graph in adjacency matrix representation.

A[1][2] means there's an edge between 1 and 2
"""

def getAdjMat(edges: list, v: int) -> list:

    adj_mat = [[0] * v for _ in range(v)]
    print(adj_mat)

    for u, v in edges:
        adj_mat[u][v] = 1
    
    return adj_mat


edges = [
    [0, 1],
    [1, 2], 
    [0, 2]
]
print(getAdjMat(edges, 3))