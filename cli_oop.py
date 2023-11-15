# This file contains the Command Line Interface (CLI) for OOP designed Tic-tac-toe
# the Tic-Tac-Toe game. This is where input and output happens.

from oop_class.player import BotPlayer, HumanPlayer
from oop_class.board import Board
from oop_class.game import Game

# Reminder to check all the tests

if __name__ == '__main__':
    # initialize the board
    board = Board() 
    # choose game type, single or 2 players
    game_type = int(input("Please enter 1 for single player or 2 for two players: "))
    player1 = HumanPlayer('X')
    player2 = BotPlayer('O') if game_type == 1 else HumanPlayer('O')
    # initialize the game
    game = Game(player1, player2, board)
    # game start
    game.play()
    
    
