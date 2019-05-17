from numpy import random
board = [" "] * 10
def checkWin(b,m):
    return((b[1] == m and b[2] == m and b[3] == m) or  #Top Row
           (b[4] == m and b[5] == m and b[6] == m) or  #Middle Row
           (b[7] == m and b[8] == m and b[9] == m) or  #Bottom Row
           (b[1] == m and b[4] == m and b[7] == m) or  #Left Column
           (b[2] == m and b[5] == m and b[8] == m) or  #Centre Column
           (b[3] == m and b[6] == m and b[9] == m) or  #Right Column
           (b[1] == m and b[5] == m and b[9] == m) or  #Left to Right Diagonal
           (b[3] == m and b[5] == m and b[7] == m))    #Right to Left Diagonal
#Lets give the computer a proper thought process now.
#First create a copy of the board
def getBoardCopy(b):
    dpboard = []
    for x in b:
        dpboard.append(x)
    return dpboard
#tesing if by making a move in sqaure i will win the game.
def testWinMove(b, mark, i):
    bcopy = getBoardCopy(b)
    bcopy[i] = mark
    return checkWin(bcopy, mark)
def reset():
    #Reseting the board for if they want to play again.
    for i in board[]:
        board[i] = " "
def Compute_turn():
    #After checking that no one will win next turn it finds a spot to go
    def check_again():
        numberthing = random.randint(1,9)
        if board[numberthing] == "X" or board[numberthing] == "O":
            numerthing = random.randint(1,9)
        else:
            board[numberthing] = "X"

    #Checking if either player wins through his turn
    def check():
        for i in range(1,10):
            if board[i] == "X" or board[i] == "O":
                pass
            elif testWinMove(board, "X", i):
                board[i] = "X"
                break
            elif testWinMove(board, "O", i):
                board[i] = "X"
                break
            elif i == 9:
                check_again()
    check()
