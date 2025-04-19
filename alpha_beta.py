MAX,MIN=float('infinity'),-float('infinity')
def alpha_beta(depth,nodeIndex,maximizingPlayer,values,alpha,beta,path,current_path):
    if depth==maxdepth:
        return values[nodeIndex],current_path
    if (maximizingPlayer):
        best=MIN
        for i in range(0,2):
            val,sub_path=alpha_beta(depth+1,nodeIndex*2+i,False,values,alpha,beta,path,current_path+[nodeIndex*2+i])   
            if best<val:
                best=val
                path[:]=sub_path
            alpha=max(alpha,best)
            if beta>alpha:
                remaining_nodes.add(val)
            if beta<=alpha:
                print(f"Pruning is done at depth {depth}, alpha {alpha}, beta {beta}")
                print_remaining_tree(remaining_nodes,values)
                break
 
        return best,path
    else:
        best=MAX
        for i in range(0,2):
            val,sub_path=alpha_beta(depth+1,nodeIndex*2+i,True,values,alpha,beta,path,current_path+[nodeIndex*2+i])   
            if best>val:
                best=val
                path[:]=sub_path
            beta=min(beta,best)
            if beta>alpha:
                remaining_nodes.add(val)
            if beta<=alpha:
                print(f"Pruning is done at depth {depth}, alpha {alpha}, beta {beta}")
                print_remaining_tree(remaining_nodes,values)
                break

        return best,path

def print_remaining_tree(remaining_nodes, values):
    print("Remaining tree after pruning:")
    for node in remaining_nodes:
        print(f"Value: {node}")
    print("------------------------------")

values=[]
remaining_nodes=set()
optimal_path=[]
maxdepth=int(input("Enter the depth of the tree:"))
nodes=int(input("Enter the number of terminal nodes:"))
for i in range(nodes):
    value=int(input("Enter the value of the node:"))
    values.append(value)
optimal_value,optimal_path=alpha_beta(0,0,True,values,MIN,MAX,optimal_path,[0])
print("Optimal value =",optimal_value)
print("Optimal path=",optimal_path)