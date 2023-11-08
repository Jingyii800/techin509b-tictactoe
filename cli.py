# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board
from logic import get_winner
from logic import other_player
from logic import input_update_board

# Reminder to check all the tests

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    player = 'X'
    while winner == None:
        # Show the board to the user.
        print("Take a turn!")
        print(board)
        
        # input the move and upda
        input_update_board(player, board)
        # check if there is winner
        winner = get_winner(board)
        if winner:
             # print the final board
             print(board)
             print(winner, "won")
             break
        player = other_player(player)
    
