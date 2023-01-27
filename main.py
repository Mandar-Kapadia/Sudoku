import numpy as np


board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
UserBoards = []

def userInput(): 
    UserBoard=[]
    rows = []
    rowSize = int(input("How many do you have rows? "))
    columSize = int(input("How many colums do you have? "))
    for i in range(columSize):
        for j in range(rowSize):
            print("input: [" + str(i) +"][" + str(j)+"]")
            rows.append(int(input()))
        UserBoard.append(rows)
        print(UserBoard)
        rows = []
    return UserBoard
#takes In the board Data to print the data by making sqaures
# every 3 it adds a horizontal and verital

def printBoard(board):
    print("- - - - - - - - - - ")
    for i in range(len(board)):
        if (i % 3 == 0) and i != 0:
            print("- - - - - - - - - - ")
        for j in range(len(board[i])):
            if (j % 3 == 0) and (j != 0) :
                print("|", end="")
            if(j == 8):
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
    print("- - - - - - - - - - ")
def Empty(Board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] == 0):
                return(i,j)
    return None
def Valid(Board,Number,Position):
    #Checking row
    for i in range(len(board[0])):
        if Board[Position[0]][i] == Number and Position[1]!= i:
            return False

    
    #Checking Column

    for i in range(len(board)):
        if(Board[i][Position[1]]== Number and Position[0]!= i):
            return False 

    #Check the Box
    boxX = Position[1] // 3
    boxY = Position[0] // 3

    for i in range(boxY * 3, boxY * 3 + 3):
        for j in range(boxX * 3,boxX * 3 + 3):
            if(board[i][j]== Number and (i,j) != Position):
                return False
    return True


def Solve(Board):
    #find an empty spot. if No empty spot then weere don
    find = Empty(Board) 
    if not find:
        return True
    else:
        row, col = find
# go through the rang and put items inside and check if its valid is so then we recursively do Solve
# if something fails then we go back to board [row][colum] and get new inputs. 
    for i in range(1,10):
        if Valid(Board,i,(row,col)):
            board[row][col] = i
            if Solve(Board):
                return True
            board[row][col] = 0
    return False


UserBoards= userInput()
printBoard(UserBoards)
#$print(Solve(board))
#print("--------------------New solution------------------------")
#printBoard(board)