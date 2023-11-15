# NOT USED in OOP 

# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def check_winner(board):
    pass

def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
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


def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return player 


def input_update_board(player, board):
    #  Input a move from the player.
    row_player = int(input("Put %s in row:" %player))
    col_player = int(input("Put %s in col:" %player))
    #  Update the board.
    try:
        board[row_player][col_player] = player
    except (ValueError, IndexError):
        print("Invalid input. Please enter numbers between 0 and 2.")

