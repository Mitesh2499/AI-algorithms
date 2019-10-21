graph={
    'A':set(['B','C']),
    'B':set(['A','D','E']),
    'C':set(['A','F']),
    'D':set(['B']),
    'E':set(['B']),
    'F':set(['C'])
 
    }

def bfs(graph,start):
    queue=[start]
    visited=[]
    while queue:
        node = queue.pop(0)
        visited.append(node)
        neighbours=graph[node]
        for n in neighbours:
            if n not in visited and n not in queue:
                queue.append(n)
    return visited

path=bfs(graph,'A')
print(path)
