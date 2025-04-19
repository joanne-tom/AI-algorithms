def dfs(graph,start,visited=None):
    if visited is None:
        visited=set()
    visited.add(start)
    print(start,end=" ")
    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)
graph={'0':['1','3'],'1':['0','3','2','5','6'],'2':['1','3','5','4'],'3':['0','1','2','4'],'4':['2','3','6'],'5':['1','2'],'6':['1','4']}
dfs(graph,'0')