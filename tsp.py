def calculate_total_distance(path,distance_matrix):
    total_distance=0
    for i in range(len(path)-1):
        total_distance+=distance_matrix[path[i]][path[i+1]%len(path)]
    return total_distance

def hill_climbing(distance_matrix):
    num_cities=len(distance_matrix)
    current_path=list(range(num_cities))
    start=int(input('Enter the Starting city index:'))
    current_path.pop(start)
    current_path.append(start)
    current_distance=calculate_total_distance(current_path,distance_matrix)
    while True:
        neighbour_found=False
        for i in range(num_cities-1):
            for j in range(i+1,num_cities-1):
                neighbour_path=current_path[:]
                neighbour_path[i],neighbour_path[j]=neighbour_path[j],neighbour_path[i]
                neighbour_distance=calculate_total_distance(neighbour_path,distance_matrix)
                if neighbour_distance<current_distance:
                    current_path=neighbour_path
                    current_distance=neighbour_distance
                    neighbour_found=True
                    break
                if not neighbour_found:
                    break
        return current_path,current_distance,start

distance_matrix=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
optimal_path,optimal_value,start=hill_climbing(distance_matrix)
optimal_path=[start]+optimal_path
print('Optimal path=',optimal_path)
print('Optimal distance=',optimal_value+distance_matrix[start][optimal_path[1]])