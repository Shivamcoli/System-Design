from dice import Dice
from board import Board
class Player:
    Player_List = {}
    def __init__(self):
        number=int(input("Enter number of players: "))
        for i in range(number):
            name=input(f"Enter name of player {i+1}: ")
            self.Player_List[name]=0
            
            
    def move_player(self,name,position,roll):
        if position+roll<=len(Board.board):
            position+=roll
            self.Player_List[name] = position
        return self.Player_List[name]
            
