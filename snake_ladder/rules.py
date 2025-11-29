from board import Board
from dice import dice

class rule:
    def __init__(self):
        pass
    

    def valid_move(self,position,roll,board_size):
        if position + roll <= board_size:
            return True
        else:
            return False
        
    def move_player(self,position,roll):
        if not self.valid_move(position, roll, board_size=100):  # Assuming default board size is 100
            return position
        return position + roll
    
    def check_snake_ladder(self,position,board):
        snake_tail = board.is_snake_head(position)
        if snake_tail != -1:
            return snake_tail
        ladder_top = board.is_ladder_base(position)
        if ladder_top != -1:
            return ladder_top
        return position
    
    def display_position(self,player_name,position):
        print(f"{player_name} is now at position {position}")
        
    def check_winner(self,position,board_size):
        if position == board_size:
            return True
        else:
            return False
        
        
    def display_winner(self,player_name):
        print(f"Congratulations {player_name}! You have won the game!")
        
