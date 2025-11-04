"""
Represent a graph in adjacency list representation given a list of edges

Dictionary with list as values
"""

def getAdjList(edges: list) -> dict:
    
    adj_list = {}

    for u, v in edges:
        if u not in adj_list:
            adj_list[u] = []
        if v not in adj_list:
            adj_list[v] = []
    
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    return adj_list


edges = [
    [1, 2],
    [2, 3],
    [1, 3],
    [3, 4]
]

print(getAdjList(edges))