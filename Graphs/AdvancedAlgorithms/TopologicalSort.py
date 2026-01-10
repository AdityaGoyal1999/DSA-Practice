# Given a DAG, give the linear ordering of nodes

def topoSort(edges, V):

    # create adj_map
    adj_map = {i: [] for i in range(V)}
    for u, v in edges:
        adj_map[u].append(v)

    # have visited set and stack for storing results
    visited = set() # only add to the set when all neighbouring nodes have been visited
    stack = []

    # create dfs function
    def dfs(node):
        if node in visited:
            return
        else:
            for nei in adj_map[node]:
                if nei not in visited:
                    dfs(nei)
            
            visited.add(node)
            stack.append(node)
    
    # call dfs function on all nodes
    for node in range(V):
        if node not in visited:
            dfs(node)

    # return stack - linear ordering of nodes
    return stack


edges = [[5, 0], [4, 0], [4, 1], [5, 2], [2, 3], [3, 1]]
print(topoSort(edges, 6))