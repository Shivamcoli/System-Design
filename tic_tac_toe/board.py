# board.py
class Board:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Board, cls).__new__(cls)
            cls.__instance.grid = [[' ' for _ in range(3)] for _ in range(3)]
        return cls.__instance

    def display(self):
        for i, row in enumerate(self.grid):
            print(' | '.join(row))
            if i < 2:
                print('-' * 9)

    def reset(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]
