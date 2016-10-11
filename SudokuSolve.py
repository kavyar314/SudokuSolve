import math

boarda=[1,0,3,4,
        0,0,2,0,
        0,4,0,0,
        2,0,4,0]
boarduse=[0,0,9,7,3,0,0,0,2,
          3,0,6,0,0,0,0,0,1,
          0,0,0,0,1,0,0,0,0,
          0,0,5,3,0,0,9,0,6,
          0,9,0,0,0,0,0,3,0,
          4,0,3,0,0,1,5,0,0,
          0,0,0,0,2,0,0,0,0,
          1,0,0,0,0,0,8,0,5,
          5,0,0,0,9,7,2,0,0]
WIDTH=int(math.sqrt((len(boarduse))))
BOXLEN=int(math.sqrt(WIDTH))
def pprint(board):
    n=int(math.sqrt(len(board)))
    for i in range(n):
        for j in range(n):
            print board[i*n+j],
        print

    
def boxes(n):
    boxes=[]
    for rclass in range(n):
        for cclass in range(n):
            currbox=[]
            for row in range(n):
                for col in range(n):
                    currbox.append((rclass*n+row)*n*n+cclass*n+col)
            boxes.append(currbox)
    return boxes

def whichbox(cell):
    listbox=boxes(BOXLEN)
    for i in range(WIDTH):
        for j in range(WIDTH):
            if listbox[i][j]==cell:
                return listbox[i]

def legal(board,cell):
    '''Takes in board state and cell no. and returns list of possibilities for that cell
       e.g. legal([1,0,3,4,0,0,2,0,0,4,0,0,2,0,4,0],5)-->[3]'''
    row=cell/WIDTH
    column=cell%WIDTH
    restrictions=[]
    for i in range(WIDTH):
        restrictions.append(board[row*WIDTH+i])
    for i in range(WIDTH):
        restrictions.append(board[WIDTH*i+column])
    for i in whichbox(cell):
        restrictions.append(board[i])
    restrictions=list(set(restrictions))
    out=[i for i in range(1,WIDTH+1) if i not in restrictions]
    return out

def solve(board):
    try:
        a=board.index(0)
    except:
        return board, True
    p1=legal(board,a)
    if p1==[]:
        return board, False
    for v in p1:
        board1=board[:a]+[v]+board[a+1:]
        board1, success=solve(board1)
        if success:
            return board1, True
    return board, False
import random
def sample(solution,m):
    indices=[]
    while len(indices)<len(solution)-m:
        index=random.randint(0,len(solution)-1)
        if index not in indices:
            indices.append(index)
            solution[index]=0
    return solution

def makesudoku(n,m):
    seed=[0]*n
    for i in range(int(math.sqrt(n)-3)):
        index=random.randint(0,n-1)
        seed[index]=random.choice(range(1,10))
    solution,success=solve(seed)
    return sample(solution, m)


    

puzzle=makesudoku(81,17)
pprint(puzzle)    
solution, success=solve(puzzle)
raw_input()
pprint(solution)
