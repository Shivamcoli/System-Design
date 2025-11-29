from player import Player
from dice import Dice  
from board import Board

class GameEngine:
    def __init__(self):
        self.board=Board()
        self.dice=Dice()
        self.player=Player()
    
    def check_winner(self,position):
        if position==len(self.board.board):
            return True
        return False
        
    def start_game(self):
        print("Game Started")
        game_state=True
        while game_state==True:
            for name,position in self.player.Player_List.items():
                roll=self.dice.roll_dice()
                position=self.player.move_player(name,position,roll)

                print(f"Player {name} rolled a {roll} and moved to position {position}")
                
                if position in self.board.snake:
                    position=self.board.snake[position]

                    print(f"Player {name} encountered a snake and moved to position {position}")
                    
                elif position in self.board.ladder:
                    position=self.board.ladder[position]

                    print(f"Player {name} climbed a ladder and moved to position {position}")  
                    
                if self.check_winner(position):
                    print(f"Player {name} won the game!")
                    game_state=False
                    break
                    
                    
if __name__=="__main__":
    game=GameEngine()
    game.start_game()
            