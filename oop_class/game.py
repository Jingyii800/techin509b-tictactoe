import time

class Game:
    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.board = board
        # store the first move position
        self.first_move = None
        # check if the first move has been made
        self.check_first_move = False
    
    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
    
    def play_turn(self, row, col):
        if not self.check_first_move:
            self.first_move = row * 3 + col + 1 # change it to index from 1-9
            self.check_first_move = True
        self.board.update_board(row, col, self.current_player)
        self.board.check_winner()
        self.switch_player()

    def play(self):
        from cli_oop import log_game_result
        move_count = 0
        while self.board.winner is None:
            print("Take a Turn")
            self.board.print_board()
            row, col = self.current_player.move(self.board)
            self.play_turn(row, col)
            # count move to log
            move_count += 1
            # get winner
            if self.board.winner:
                self.board.print_board()
                print(self.board.winner, "won")
                break
            # or check if draw
            elif self.board.is_draw():
                self.board.print_board()
                print("It's a draw!")
                break

        # check if the first player won the game or not
        if self.board.winner == self.player1.symbol:
            first_move_result = "Win"
        elif self.board.winner == self.player2.symbol:
            first_move_result = 'Loss'
        else:
            first_move_result = "Draw"

        # logging
        winner_symbol = self.board.winner if self.board.winner else "Draw"
        log_game_result(self.player1, self.player2, winner_symbol,move_count,self.first_move, first_move_result)