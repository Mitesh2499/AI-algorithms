import copy
size=4
solutions=[]
#This function just create board as two dimentional array with 0
'''
[[0,0,0,0],
 [0,0,0,0],
 [0,0,0,0],
 [0,0,0,0]]
'''
def get_board(size):        
    board=[]
    for k in range(size):
        row=[]
        for j in range(size):
            row.append(0)
        board.append(row)
    return board

#This function prints the number of solutions obtained for N-quuen Puzzle
def print_solutions(solutions,size):
    for solution in solutions:
        for row in solution:
            print(row)
        print()

#Here check in board is queen is safe such that there wont be any queen in digonal, horizontal,vertical directions
def is_safe(board,row,col,size):
    '''
        row index is fixed and column indexes are changing
        [0,0,0,0] check for single row i.e horizontal
    '''
    for j in range(col):
        if board[row][j]==1:
            return False
    '''
        check for upper diagonal
    '''
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j] == 1:
            return False
    '''
        Check for lower diagonal
    '''
    for i,j in zip(range(row,size),range(col,-1,-1)):
        if board[i][j] ==1:
            return False
    '''
        if none of above condition satisfied then
        queen is safe to place
    '''
    return True

#To solve N-queen 
def solve(board,col,size):
    '''
        chcek if all columns are visited i.e col>=size
    '''
    if col>=size:
        return
    
    for i in range(size):
        if is_safe(board,i,col,size):
            board[i][col]=1
            if col == size-1:
                add_solution(board) #add solution
                #board[i][col]=0
                return
            solve(board,col+1,size)
            board[i][col]=0

#to copy the board which is solved
def add_solution(board):
    global solutions
    saved_board=copy.deepcopy(board)
    solutions.append(saved_board)

board=get_board(size)
solve(board,0,size)
print_solutions(solutions,size)
