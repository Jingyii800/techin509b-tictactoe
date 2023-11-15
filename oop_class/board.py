class Board:
    def __init__(self):
        self.board = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
        ]
        self.winner = None
    
    def __getitem__(self, index):
        return self.board[index]

    def print_board(self):
        symbols = {None: " ", "X": "X", "O": "O"}
        for row in self.board:
            print("| " + " | ".join(symbols[cell] for cell in row) + " |")
        print()

    def update_table(self, row, col, player):
        if self.board[row][col] == None:
                self.board[row][col] = player.symbol

    def get_winner(self):
        #check rows
        for row in self.board:
            if len(set(row)) == 1 and row[0]!= None:
                self.winner = row[0]
                return
        #check columns
        for i in range(3):
            col = [self.board[j][i] for j in range(len(self.board))]
            if len(set(col)) == 1 and self.board[0][i] != None:
                self.winner = self.board[0][i]
                return
        #check diagnols
        top_left_to_bot_right = [self.board[i][i] for i in range(len(self.board))]
        if len(set(top_left_to_bot_right)) == 1 and self.board[0][0]!= None:
            self.winner = self.board[0][0]
            return
        top_right_to_bot_left = [self.board[i][len(self.board)-1 - i] for i in range(len(self.board))]
        if len(set(top_right_to_bot_left)) == 1 and self.board[0][len(self.board)-1] != None :
            self.winner = self.board[0][len(self.board)-1]
            return
        
    def is_draw(self): # check if it's draw
        for row in self.board:
            for cell in row:
                if cell is None:
                    return False
        return True