board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

# uses backtracking to solve a sudoku board
def solve(board):
    blank = findBlank(board)

    if not blank:
        return True # solution has been found (base case) 
    else: 
        row, col = blank # position found through findBlank(board)

    # loop through and test numbers to see if they are valid placements
    for i in range(1,10):
        if validPlacement(board, i, (row,col)):
            board[row][col] = i

            if solve(board):
                return True

            # try a different number
            board[row][col] = 0 
    
    # backtrack
    return False

def validPlacement(board, n, pos): # n is number you are testing
    # check row
    for i in range(len(board[0])):  
        if board[pos[0]][i] == n and pos[1] != i:
            return False

    # check col
    for i in range(len(board)):  
        if board[i][pos[1]] == n and pos[0] != i:
            return False

    # check subgrid (3x3)
    x0 = pos[1]//3 
    y0 = pos[0]//3
    for i in range(y0*3, y0*3+3):
        for j in range(x0*3, x0*3+3):
            if board[i][j] == n and (i,j) != pos:
                return False
    return True

# finds a blank space on the board (0)
def findBlank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return(i, j) # row, col
    return None

def printBoard(board): 
    for i in range(len(board)):
        if i % 3 == 0 and i!=0:
            print("- - - - - - - - - - - -")
            
        for j in range (len(board[0])):
            if j % 3 == 0 and j != 0: 
                print (" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")





print("Original Board:")
printBoard(board)
solve(board)
print()
print("Solution:")
printBoard(board)