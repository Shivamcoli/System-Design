# player.py
from board import Board

class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def make_move(self, row, col):
        board = Board()

        if not (0 <= row < 3 and 0 <= col < 3):
            print("Invalid coordinates.")
            return False

        if board.grid[row][col] == ' ':
            board.grid[row][col] = self.marker
            return True

        print("Cell already occupied!")
        return False
