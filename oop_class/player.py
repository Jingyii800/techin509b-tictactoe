import random

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def move(self, board):
        pass

class HumanPlayer(Player):
    def move(self, board):
        while True:
            try:
                row = int(input(f"Player {self.symbol}, enter your row number 0-2: "))
                col = int(input(f"Player {self.symbol}, enter your column number 0-2: "))
                if row not in range(3) or col not in range(3):
                    print("Invalid Input. Please try again")
                    continue
                if board[row][col] is not None:
                    print("That position is already taken. Please try again.")
                    continue
                return (row, col)
            except (IndexError, ValueError, UnboundLocalError,TypeError):
                print ("Invalid move. Please enter row and column numbers from 0 to 2")


    
class BotPlayer(Player):
    def move(self, board):
        move = [(i,j) for i in range(3) for j in range(3) if board[i][j] is None]
        return random.choice(move)
