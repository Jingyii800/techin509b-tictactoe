# This file contains the Command Line Interface (CLI) for OOP designed Tic-tac-toe
# the Tic-Tac-Toe game. This is where input and output happens.

from oop_class.player import BotPlayer, HumanPlayer
from oop_class.board import Board
from oop_class.game import Game
import time

import csv
import datetime

if __name__ == '__main__':
    # for week 10 assignment, play the game 30 times:
    for _ in range(30):
        # initialize the board
        board = Board() 
        # choose game type, single or 2 players
        # game_type = int(input("Please enter 1 for single player or 2 for two players: "))
        # player1 = HumanPlayer('X')
        # player2 = BotPlayer('O') if game_type == 1 else HumanPlayer('O')
        # for week 10 assignment, use to bot to play 30 games
        player1 = BotPlayer('X')
        player2 = BotPlayer('O')
        # initialize the game
        game = Game(player1, player2, board)
        # game start
        game.play()


# for logging  
def log_game_result(player1, player2, winner, total_moves, first_move, first_move_result):
    with open('logs/game_logs.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.datetime.now(), player1.symbol, player2.symbol, winner, total_moves, first_move, first_move_result])