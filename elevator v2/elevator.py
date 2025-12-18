

class Elevator:
    def __init__(self,id,max_floor):
        self.id=id
        self.current_floor=0
        self.direction="idle"
        self.min_floor=1
        self.max_floor=max_floor
        self.up_direction_floors=[]
        self.down_direction_floors=[]

    def append_floor(self,direction,floor_number):
        if direction=="up":
            self.up_direction_floors.append(floor_number)
        else :
            self.down_direction_floors.append(floor_number)

    def append_floor_inside(self,floor_number):
        if self.current_floor <floor_number:
            self.up_direction_floors.append(floor_number)
        elif self.current_floor > floor_number:
            self.down_direction_floors.append(floor_number)  
        else:
            print("This is current floor")
        