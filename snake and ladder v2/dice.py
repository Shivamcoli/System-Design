import random
class Dice:
    number_of_faces = 0
    def __init__(self):
        self.number_of_faces=input("Enter the max number you want in dice: ")
        
    def roll_dice(self):
        input("Press Enter to roll the dice...")
        return random.randint(1,int(self.number_of_faces))