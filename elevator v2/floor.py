class Floor:
    def __init__(self,floor_number):
        self.floor_number= floor_number
        self.up_button=0
        self.down_button=0

    def press_up(self):
        self.up_button=1
        return self.up_button

    def press_down(self):
        self.down_button=1
        return self.down_button

    def reset_button(self, direction):
        if direction=="up":
            self.up_button=0
        else:
            self.down_button=0