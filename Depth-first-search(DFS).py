graph={
    'A':set(['B','C']),
    'B':set(['A','D','E']),
    'C':set(['A','F']),
    'D':set(['B']),
    'E':set(['B']),
    'F':set(['C'])
    }

def dfs(graph,node,visited):
    if node not in visited:
        visited.append(node)
        neighbours=graph[node]
        for neighbour in neighbours:
            dfs(graph,neighbour,visited)
    return visited;

path=dfs(graph,'A',[])
print(path)
