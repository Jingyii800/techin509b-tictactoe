import unittest
from unittest.mock import patch
from oop_class.board import Board
from oop_class.game import Game
from oop_class.player import HumanPlayer, BotPlayer


class TestLogic(unittest.TestCase):

    # check initial empty board
    def test_make_empty_board(self):
        board = Board()
        self.assertEqual(len(board.board), 3) # check 3 rows
        for row in board.board:
            self.assertEqual(len(row), 3) # check 3 columns
            for cell in row:
                self.assertEqual(cell, None) # check if initial cell is none

    # check taking turns
    def test_switch_player(self):
        board = Board()
        game = Game('X','O', board)
        game.switch_player()
        self.assertNotEqual(game.current_player,'X')
        game.switch_player()
        self.assertEqual(game.current_player, 'X')
    
    # check winner
    def test_check_winner(self):
        board = Board()
        board.board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(board.check_winner(), 'X')
        board.board = [
            ['X', 'O', 'O'],
            ['O', 'X', 'X'],
            ['X', 'O', 'O'],
        ]
        self.assertEqual(board.check_winner(), None)
        board.board = [
            ['X', 'O', 'X'],
            ['O', 'O', 'O'],
            ['O', 'X', 'X'],
        ]
        self.assertEqual(board.check_winner(), 'O')

    # check if can get winner after several turns
    def test_play(self):
        board = Board()
        player1 = HumanPlayer('X')
        player2 = HumanPlayer('O')
        game = Game(player1,player2,board)
        moves = [(1,1), (0,2),(0,0),(0,1),(2,2)]
        # mock 
        with patch('oop_class.player.HumanPlayer.move', side_effect=moves):
            with patch('oop_class.board.Board.print_board'):  # Mock print_board to suppress output during test
                game.play()
                self.assertEqual(board.winner, 'X')  # Validate 'X' is the winner

    # check player can be assigned to bot
    def test_bot(self):
        board = Board()
        human = HumanPlayer('X')
        bot = BotPlayer('O')
        game = Game(human, bot, board)
        # mock bot, make it always move to 0,0
        with patch.object(BotPlayer, 'move', return_value=(0,0)):
            # human move
            game.play_turn(1,1)
            # bot move
            bot_move = bot.move(board)
            game.play_turn(*bot_move)

            # assertion, human move(1,1), bot move (0,0)
            self.assertEqual(board.board[1][1], 'X')
            self.assertEqual(board.board[0][0], 'O')


if __name__ == '__main__':
    unittest.main()
