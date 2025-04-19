cost={}
parent={}
node=[]
n=int(input("Enter the number of nodes:"))
print("Enter the nodes:")
for i in range(n):
    m=input()
    cost[m]=float('inf')
    node.append(m)
graph={}
weight={}
for i in node:
    graph[i]=[]
    weight[i]={}
    x=int(input(f"Enter the number of neighbours of {i}:"))
    print("Enter the neighbours:")
    for j in range(x):
        k=input()
        graph[i].append(k)
        c=int(input(f"Enter the cost from {i} to {k}:"))
        weight[i][k]=c

start=input("Enter the starting node:")
cost[start]=0
parent[start]=None

def dijkstra(node,bcost):
    for i in graph[node]:
        c=bcost+weight[node][i]
        if c<cost[i]:
            cost[i]=c
            parent[i]=node
            dijkstra(i,c)

dijkstra(start,0)
path={}
for i in node:
    path[i]=i
    t=i
    while parent[t] != None:
        path[i]=parent[t]+"->"+path[i]
        t=parent[t]
for i in node:
    print(f"Shortest path to {i} is",path[i])
    print(f"Lowest cost to {i} is",cost[i])