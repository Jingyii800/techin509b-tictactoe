import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_make_empty_board(self):
        board = logic.make_empty_board()
        self.assertEqual(len(board), 3) # check 3 rows
        for row in board:
            self.assertEqual(len(row), 3) # check 3 columns
            for cell in row:
                self.assertEqual(cell, None) # check if initial cell is none

    def test_other_player(player):
        pass
    
    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')




if __name__ == '__main__':
    unittest.main()
