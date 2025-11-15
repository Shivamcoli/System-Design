# game.py
from board import Board
from rules import Rules

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.rules = Rules()

    def switch_player(self):
        self.current_player = (
            self.player2 if self.current_player == self.player1 else self.player1
        )

    def _get_move(self):
        try:
            row = int(input(f"{self.current_player.name} enter row (0-2): "))
            col = int(input(f"{self.current_player.name} enter col (0-2): "))
            return row, col
        except ValueError:
            print("Invalid input! Enter numbers only.")
            return None

    def play(self):
        board = Board()
        board.reset()

        moves = 0
        while moves < 9:
            board.display()
            coords = None

            while coords is None:
                coords = self._get_move()

            row, col = coords
            if self.current_player.make_move(row, col):
                moves += 1
            else:
                continue

            if self.rules.check_winner():
                board.display()
                print(f"{self.current_player.name} wins!")
                return

            self.switch_player()

        board.display()
        print("It's a draw!")
