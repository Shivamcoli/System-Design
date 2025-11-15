# main.py
from player import Player
from game import Game

if __name__ == "__main__":
    p1 = Player("Alice", "X")
    p2 = Player("Bob", "O")

    game = Game(p1, p2)
    game.play()
