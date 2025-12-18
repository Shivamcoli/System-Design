
class Floor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.up_button_pressed = False
        self.down_button_pressed = False
        
    def press_up_button(self):
        self.up_button_pressed = True
        print(f"Up button on floor {self.floor_number} pressed.")
        return self.up_button_pressed
        
    def press_down_button(self):
        self.down_button_pressed = True
        print(f"Down button on floor {self.floor_number} pressed.")
        return self.down_button_pressed