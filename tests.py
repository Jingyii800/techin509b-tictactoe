import unittest
from unittest.mock import patch
from oop_class.board import Board
from oop_class.game import Game
from oop_class.player import HumanPlayer, BotPlayer


class TestLogic(unittest.TestCase):

    # check initial empty board
    def test_empty_board(self):
        board = Board()
        self.assertEqual(len(board.board), 3) # check 3 rows
        for row in board.board:
            self.assertEqual(len(row), 3) # check 3 columns
            for cell in row:
                self.assertEqual(cell, None)

    # check game initialized with either 2 human players or 1 human + 1bot
    # also check players will be assigned to unique piece'X', 'O'
    def test_initial_player(self):
        # 2 human players
        player1 = HumanPlayer('X')
        player2 = HumanPlayer('O')
        # check unique piece assigned to players
        self.assertEqual(player1.symbol, 'X')
        self.assertEqual(player2.symbol, 'O')
        board=Board()
        # check 2 human players
        game_two_human=Game(player1,player2,board)
        self.assertIsInstance(game_two_human.player1, HumanPlayer)
        self.assertIsInstance(game_two_human.player2, HumanPlayer)
        
        # 1 human + 1 bot
        player1 = HumanPlayer('X')
        player2 = BotPlayer('O')
        # check unique piece assigned to players
        self.assertEqual(player1.symbol, 'X')
        self.assertEqual(player2.symbol, 'O')
        board=Board()
        # check 1 human player + 1 bot player
        game_bot_human=Game(player1,player2,board)
        self.assertIsInstance(game_bot_human.player1, HumanPlayer)
        self.assertIsInstance(game_bot_human.player2, BotPlayer)

    # check player can be assigned to bot (mock bot)
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


    # check taking turns
    def test_switch_player(self):
        board = Board()
        game = Game('X','O', board)
        game.switch_player()
        self.assertNotEqual(game.current_player,'X')
        game.switch_player()
        self.assertEqual(game.current_player, 'X')

    # check players can only moves to viable spots (unoccupied)
    def test_move_viability(self):
        # use bot player to test
        player = BotPlayer('O')
        board = Board()

        board.board[0][0] = 'X'
        board.board[1][1] = 'O'

        row, col = player.move(board)
        # check if bot player choose the unoccupied spot
        self.assertEqual(board.board[row][col], None)
    
    # check winner or draw from the board
    def test_check_winner(self):
        board = Board()
        # X win
        board.board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(board.check_winner(), 'X')
        # draw
        board.board = [
            ['X', 'O', 'O'],
            ['O', 'X', 'X'],
            ['X', 'O', 'O'],
        ]
        self.assertEqual(board.check_winner(), None)
        self.assertEqual(board.is_draw(), True)
        # O win
        board.board = [
            ['X', 'O', 'X'],
            ['O', 'O', 'O'],
            ['O', 'X', 'X'],
        ]
        self.assertEqual(board.check_winner(), 'O')

    # check if can detect winner after game over (mock real inputs)
    def test_play(self):
        board = Board()
        player1 = HumanPlayer('X')
        player2 = HumanPlayer('O')
        game = Game(player1,player2,board)
        moves = [(1,1), (0,2),(0,0),(0,1),(2,2)] # in this case, winner is 'X'
        # mock 
        with patch('oop_class.player.HumanPlayer.move', side_effect=moves):
            with patch('oop_class.board.Board.print_board'):  # mock print_board to suppress output during test
                game.play()
                self.assertEqual(board.winner, 'X')  # validate 'X' is the winner


if __name__ == '__main__':
    unittest.main()
