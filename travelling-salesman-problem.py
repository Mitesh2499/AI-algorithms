import random,math
graph={
    'A':{'B':10,'C':5,'D':5},
    'B':{'A':10,'C':20,'D':5},
    'C':{'B':20,'A':5,'D':15},
    'D':{'B':5,'C':15,'A':5}
    }



def dfs(graph,node,visited):
    if node not in visited:
        visited.append(node)
        neighbours=list(graph[node])
        random.shuffle(neighbours)
        for neighbour in neighbours:
            dfs(graph,neighbour,visited)
    
    return visited;
global paths
paths=[]

def findpath(graph,start):
    cord=list(graph.keys())
    l=math.factorial(len(cord)-1)
    path=dfs(graph,start,[])
    if path not in paths:
        paths.append(path)
    if len(paths)==l:
        return paths
    return findpath(graph,start)
        
def calcpath(path,graph):
    sum=0
    for i in range(len(path)-1):
        start=path[i]
        next=path[i+1]
        nodes=graph[start]
        sum=sum+nodes[next]    
    return sum
    
    

paths=findpath(graph,'A')



bestcost=10000

for path in paths:
    
    if calcpath(path,graph)<bestcost:
        bestcost=calcpath(path,graph)
        bestpath=path
    

    
    
print(bestpath,bestcost)



    
    
