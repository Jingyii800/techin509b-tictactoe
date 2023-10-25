# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board


def check_winner(board):
    #check rows
    for row in board:
        if len(set(row)) == 1 and row[0]!= None:
            return row[0]
    #check columns
    for i in range(3):
        col = [board[j][i] for j in range(len(board))]
        if len(set(col)) == 1 and board[0][i] != None:
            return board[0][i]
    #check diagnols
    top_left_to_bot_right = [board[i][i] for i in range(len(board))]
    if len(set(top_left_to_bot_right)) == 1 and board[0][0]!= None:
        return board[0][0]
    top_right_to_bot_left = [board[i][len(board)-1 - i] for i in range(len(board))]
    if len(set(top_right_to_bot_left)) == 1 and board[0][len(board)-1] != None :
        return board[0][len(board)-1]
    

# Reminder to check all the tests

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    while winner == None:

        print("Take a turn!")

        # Show the board to the user.
        print(board)

        #  Input a move from the player.
        row_x = int(input("Put X in row:"))
        col_x = int(input("Put X in col:"))

        #  Update the board.
        if board[row_x][col_x]== None:
            board[row_x][col_x] = 'X'

        # check if there is winner
        winner = check_winner(board)
        if winner:
             break

        # Update who's turn it is.
        row_o = int(input("Put O in row:"))
        col_o = int(input("Put O in col:"))
        if board[row_o][col_o]== None:
            board[row_o][col_o] = 'O'

        # check if there is winner
        winner = check_winner(board)
    
