# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_winner, other_player, input_update_board

# Reminder to check all the tests

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    player = 'X'
    while winner == None:
        print("Take a turn!")

        # Show the board to the user.
        print(board)
        
        # input the move and upda
        input_update_board(player, board)
        # check if there is winner
        winner = get_winner(board)
        if winner:
             print(winner, "won")
             break

        # Update who's turn it is.
        player = other_player(player)

        # input the move and upda
        input_update_board(player, board)
        # check if there is winner
        winner = get_winner(board)
        if winner:
             print(winner, "won")

        # Update who's turn it is.
        player = other_player(player)
    
