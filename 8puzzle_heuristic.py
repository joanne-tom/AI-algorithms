def is_goal(state,goal):
    return state==goal
 
def get_neighbours(state):
    neighbours=[]
    empty_pos=state.index(0)
    row,col=divmod(empty_pos,3)
    if col>0:
        new_path=state[:]
        new_path[empty_pos],new_path[empty_pos-1]=new_path[empty_pos-1],new_path[empty_pos]
        neighbours.append(new_path)
    if col<2:
        new_path=state[:]
        new_path[empty_pos],new_path[empty_pos+1]=new_path[empty_pos+1],new_path[empty_pos]
        neighbours.append(new_path)
    if row>0:
        new_path=state[:]
        new_path[empty_pos],new_path[empty_pos-3]=new_path[empty_pos-3],new_path[empty_pos]
        neighbours.append(new_path)
    if row<2:
        new_path=state[:]
        new_path[empty_pos],new_path[empty_pos+3]=new_path[empty_pos+3],new_path[empty_pos]
        neighbours.append(new_path)
    return neighbours
    
def heuristic(state,goal):
    h=0
    for i in range(9):
        if state[i]!=goal[i]:
            h+=1
    return h
    
def best_first_search(initial,goal):
    stack=([(initial,[],heuristic(initial,goal))])
    visited=set()
    visited.add(tuple(initial))
    while stack:
        stack.sort(key=lambda x:x[2])
        state,path,h=stack.pop(0)
        if is_goal(state,goal):
            return path+[state]
        for neighbour in get_neighbours(state):
            if tuple(neighbour) not in visited:
                visited.add(tuple(neighbour))
                stack.append((neighbour,path+[state],heuristic(neighbour,goal)))
    return None


def get_state(prompt):
    while True:
        try:
            state=list(map(int,input(prompt).strip().split()))
            if len(state)!=9 or set(state)!=set(range(9)):
                return ValueError
            return state
        except ValueError:
            print("Enter the right state")

print("Enter the initial state from 0 to 8 separated by spaces")
initial_state=get_state("initial state:")
print("Enter the goal state from 0 to 8 separated by spaces:")
goal_state=get_state("goal state:")
moves=0
soln_path=best_first_search(initial_state,goal_state)
if soln_path:
    for i,step in enumerate(soln_path):
        if step==initial_state:
            print(step[0:3])
            print(step[3:6])
            print(step[6:9])
            moves+=1
            print()
        elif step==goal_state:
            print(step[0:3])
            print(step[3:6])
            print(step[6:9])
            moves+=1
            print()
        else:
            print(step[0:3])
            print(step[3:6])
            print(step[6:9])
            moves+=1
            print()
    print("Number of moves=",moves)
else:
    print("No solution found")