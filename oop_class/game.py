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
        while self.board.winner is None:
            print("Take a Turn")
            self.board.print_board()
            row, col = self.current_player.move(self.board)
            self.play_turn(row, col)
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