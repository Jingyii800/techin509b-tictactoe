class Board:
    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.winner = None
    
    def __getitem__(self, index):
        return self.board[index]

    def print_board(self):
        symbols = {None: " ", "X": "X", "O": "O"}
        for row in self.board:
            print("| " + " | ".join(symbols[cell] for cell in row) + " |")
        print()

    def update_board(self, row, col, player):
        if self.board[row][col] == None:
                self.board[row][col] = player.symbol

    def check_winner(self):
        #check rows
        for row in self.board:
            if len(set(row)) == 1 and row[0]!= None:
                self.winner = row[0]
                return self.winner
        #check columns
        for i in range(3):
            col = [self.board[j][i] for j in range(len(self.board))]
            if len(set(col)) == 1 and self.board[0][i] != None:
                self.winner = self.board[0][i]
                return self.winner
        #check diagnols
        top_left_to_bot_right = [self.board[i][i] for i in range(len(self.board))]
        if len(set(top_left_to_bot_right)) == 1 and self.board[0][0]!= None:
            self.winner = self.board[0][0]
            return self.winner
        top_right_to_bot_left = [self.board[i][len(self.board)-1 - i] for i in range(len(self.board))]
        if len(set(top_right_to_bot_left)) == 1 and self.board[0][len(self.board)-1] != None :
            self.winner = self.board[0][len(self.board)-1]
            return self.winner
        return None
        
    def is_draw(self): # check if it's draw
        for row in self.board:
            for cell in row:
                if cell is None:
                    return False
        return True