from elevator import Elevator
from floor import Floor
from logic import Logic

class Manager:
    def __init__(self, max_floor,total_elevator):
        self.floors=[]
        self.elevators=[]
        for i in range(max_floor):
            new_floor=Floor(i+1)
            self.floors.append(new_floor)

        for i in range(total_elevator):
            new_elevator=Elevator(i+1,max_floor)
            self.elevators.append(new_elevator)

    def find_best_elevator(self, floor_number):
        best_elevator = self.elevators[0]
        min_score = float('inf')

        for elevator in self.elevators:
            distance = abs(floor_number - elevator.current_floor)
            # Calculate 'load' (how many tasks it already has)
            load = len(elevator.up_direction_floors) + len(elevator.down_direction_floors)
            
            # Score = Distance + Penalty for being busy
            # A penalty of 2 floors per task usually balances things well
            score = distance + (load * 2)

            if score < min_score:
                min_score = score
                best_elevator = elevator
                
        return best_elevator

    def press_floor_button(self, floor_number,direction):
        self.slected_floor=None
        for floor in self.floors:
            if floor.floor_number==floor_number:
                self.slected_floor=floor
        if direction == "up":
                self.slected_floor.press_up()
        else:
                self.slected_floor.press_down()
        self.best_elevator=self.find_best_elevator(floor_number)
        self.best_elevator.append_floor(direction,floor_number)

    def press_elevator_button(self,floor_number,elevator_index):
        self.elevators[elevator_index].append_floor_inside(floor_number)


    def run(self):
        for current_elevator in self.elevators:
            self.logic=Logic()
            self.logic.move(current_elevator)

if __name__ == "__main__":
    manager=Manager(15,3)
    manager.press_floor_button(12,"up")
    manager.press_floor_button(5,"down")
    manager.press_elevator_button(7,0)
    manager.run()
    manager.press_floor_button(9,"up")
    manager.press_floor_button(1,"up")
    
    manager.press_elevator_button(6,0)
    manager.run()

        
