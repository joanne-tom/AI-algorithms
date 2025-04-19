from collections import deque
def bfs(graph,start):
    frontier=deque([start])
    visited=set()
    visited.add(start)
    while frontier:
        vertex=frontier.popleft()
        print(vertex,end=" ")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                frontier.append(neighbour)
graph={'0':['1','3'],'1':['0','3','2','5','6'],'2':['1','3','5','4'],'3':['0','1','2','4'],'4':['2','3','6'],'5':['1','2'],'6':['1','4']}
bfs(graph,'0')