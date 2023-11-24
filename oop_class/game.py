import time

class Game:
    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.board = board
    
    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
    
    def play_turn(self, row, col):
        self.board.update_board(row, col, self.current_player)
        self.board.check_winner()
        self.switch_player()

    def play(self):
        from cli_oop import log_game_result
        # logging
        start_time = time.time()
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
        
        end_time = time.time()
        game_duration = end_time - start_time
        winner_symbol = self.board.winner if self.board.winner else "Draw"
        log_game_result(self.player1, self.player2, winner_symbol, game_duration, move_count)