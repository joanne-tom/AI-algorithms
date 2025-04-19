def CheckforWin():
    if board[1]==board[2] and board[1]==board[3] and board[1]!=' ':
        return True
    elif board[4]==board[5] and board[5]==board[6] and board[4]!=' ':
        return True
    elif board[7]==board[8] and board[8]==board[9] and board[7]!=' ':
        return True
    elif board[1]==board[4] and board[4]==board[7] and board[1]!=' ':
        return True
    elif board[2]==board[5] and board[5]==board[8] and board[2]!=' ':
        return True
    elif board[3]==board[6] and board[6]==board[9] and board[3]!=' ':
        return True
    elif board[1]==board[5] and board[5]==board[9] and board[1]!=' ':
        return True
    elif board[3]==board[5] and board[5]==board[7] and board[3]!=' ':
        return True
    else:
        return False

def CheckWhichMarkWon(mark):
    if board[1]==board[2] and board[1]==board[3] and board[1]==mark:
        return True
    elif board[4]==board[5] and board[5]==board[6] and board[4]==mark:
        return True
    elif board[7]==board[8] and board[8]==board[9] and board[7]==mark:
        return True
    elif board[1]==board[4] and board[4]==board[7] and board[1]==mark:
        return True
    elif board[2]==board[5] and board[5]==board[8] and board[2]==mark:
        return True
    elif board[3]==board[6] and board[6]==board[9] and board[3]==mark:
        return True
    elif board[1]==board[5] and board[5]==board[9] and board[1]==mark:
        return True
    elif board[3]==board[5] and board[5]==board[7] and board[3]==mark:
        return True
    else:
        return False

def minmax(board,depth,ismaximizing):
    if CheckWhichMarkWon(bot):
        return 1
    elif CheckWhichMarkWon(player):
        return -1
    elif CheckDraw():
        return 0
    if (ismaximizing):
        bestScore=-800
        for key in board.keys():
            if board[key]==' ':
                board[key]=bot
                score=minmax(board,depth+1,False)
                board[key]=' '
                if score>bestScore:
                    bestScore=score
        return bestScore
    else:
        bestScore=800
        for key in board.keys():
            if board[key]==' ':
                board[key]=player
                score=minmax(board,depth+1,True)
                board[key]=' '
                if score<bestScore:
                    bestScore=score
        return bestScore

def compMove():
    bestScore=-800
    bestMove=0
    for key in board.keys():
        if board[key]==' ':
            board[key]=bot
            score=minmax(board,0,False)
            board[key]=' '
            if score>bestScore:
                bestScore=score
                bestMove=key
    insertLetter(bot,bestMove)
    return

def is_space_free(pos):
    if board[pos]!=' ':
        return False
    return True

def printBoard(board):
    print(board[1],"|",board[2],'|',board[3])
    print('--+---+-')
    print(board[4],"|",board[5],'|',board[6])
    print('--+---+-')
    print(board[7],"|",board[8],'|',board[9])
    print()

def CheckDraw():
    for key in board.keys():
        if board[key]==' ':
            return False
    return True

def insertLetter(letter,pos):
    if is_space_free(pos):
        board[pos]=letter
        printBoard(board)
        if CheckDraw():
            print("Draw")
            exit(0)
        elif CheckforWin():
            if letter=='O':
                print('Player wins')
                exit(0)
            else:
                print('Bot wins')
                exit(0)
        return
    else:
        print("Incorrect position.Enter the right position")
        new_pos=int(input("Ënter the new position:"))
        insertLetter(letter,new_pos)
        return

def playerMove():
    pos=int(input("Enter the position to enter O:"))
    insertLetter(player,pos)
    return
board={1:" ",2:' ',3:' ',
       4:' ',5:' ',6:' ',
       7:' ',8:' ',9:' '}
print("You play first. Good luck!!")
print('The board positions are:')
print("1 2 3")
print("4 5 6")
print('7 8 9')
player='O'
bot='X'
while not CheckforWin():
    playerMove()
    compMove()