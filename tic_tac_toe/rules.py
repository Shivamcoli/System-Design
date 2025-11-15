# rules.py
from board import Board

class Rules:
    def check_winner(self):
        board = Board()

        for i in range(3):
            if board.grid[i][0] == board.grid[i][1] == board.grid[i][2] != ' ':
                return True
            if board.grid[0][i] == board.grid[1][i] == board.grid[2][i] != ' ':
                return True

        if board.grid[0][0] == board.grid[1][1] == board.grid[2][2] != ' ':
            return True

        if board.grid[0][2] == board.grid[1][1] == board.grid[2][0] != ' ':
            return True

        return False
