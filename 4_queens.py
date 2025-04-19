def is_safe(row,col,board):
    for i in range(row):
        if board[i]==col or board[i]-i==col-row or board[i]+i==col+row:
            return False
    return True

def n_queens_csp(row,N,board):
    if row==N:
        return True
    for col in range(N):
        if is_safe(row,col,board):
            board[row]=col
            if n_queens_csp(row+1,N,board):
                return True
        board[row]=-1
    return False

def solve_n_queens(N):
    board=[-1]*N
    if n_queens_csp(0,N,board):
        soln=[]
        for row in range(N):
            row_soln=[' ']*N
            row_soln[board[row]]='Q'
            soln.append("|".join(row_soln))
        return soln
    return None
N=4
soln=solve_n_queens(N)
if soln:
    print('------------')
    for line in soln:
        print('|',line,'|')
        print('------------')
else:
    print('No solution found')