from board import Board
from dice import dice
from rules import rule # Assuming filename is rules.py

class Game:
    def __init__(self):
        pass

    def play(self):
        total_players =int(input("Enter number of player: "))
        player_list = []
        for i in range(total_players):
            name=input("Enter player name")
            player_list.append(name)
        board_size = int(input("Enter board size: "))
        snake_count = int(input("Enter number of snakes: "))
        ladder_count = int(input("Enter number of ladders: "))
        snake = {}
        ladder = {}
        for i in range(snake_count):
            head = int(input(f"Enter snake {i+1} head position: "))
            tail = int(input(f"Enter snake {i+1} tail position: "))
            snake[head] = tail
        for i in range(ladder_count):
            base = int(input(f"Enter ladder {i+1} base position: "))
            top = int(input(f"Enter ladder {i+1} top position: "))
            ladder[base] = top
        player_positions = {player: 0 for player in player_list}
        board = Board(board_size, snake, ladder, [])
        dice_obj = dice()
        rule_obj = rule()
        game_over = False
        print("Lets start the game!")
        while(game_over==False): # 1. Use the flag in the loop condition
            for player in player_list:
                input(f"{player}'s turn. Press Enter to roll the dice...")
                roll = dice_obj.roll_dice()
                new_position = rule_obj.move_player(player_positions[player], roll)
                new_position = rule_obj.check_snake_ladder(new_position, board)
                player_positions[player] = new_position
                rule_obj.display_position(player, new_position)
                if rule_obj.check_winner(new_position, board_size):
                    rule_obj.display_winner(player)
                    game_over = True # 3. Set flag to True
                    break
                
if __name__ == "__main__":
    g=Game()
    g.play()