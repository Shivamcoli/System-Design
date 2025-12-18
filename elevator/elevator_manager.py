from elevator import Elevator
from elevator_logic import Elevator_logic
from floor import Floor

class Elevator_manager:
    
    def __init__(self, min_floor, max_floor, num_elevators):
        self.elevators = [
            Elevator(i, min_floor, max_floor)
            for i in range(num_elevators)
        ]
        self.floors = [Floor(floor_number) for floor_number in range(min_floor, max_floor + 1)]
        self.elevator_logic = Elevator_logic()
        
    def find_best_elevator(self, floor_number, direction):
        best_elevator = None
        best_distance = float('inf')
        
        for elevator in self.elevators:
            if elevator.direction == "idle":
                distance = abs(elevator.current_floor - floor_number)
                if distance < best_distance:
                    best_distance = distance
                    best_elevator = elevator
            elif elevator.direction == direction:
                if (direction == "up" and elevator.current_floor <= floor_number) or \
                   (direction == "down" and elevator.current_floor >= floor_number):
                    distance = abs(elevator.current_floor - floor_number)
                    if distance < best_distance:
                        best_distance = distance
                        best_elevator = elevator
        return best_elevator
        
    def request_elevator_from_floor(self, floor_number, direction):
        print(f"Requesting elevator to floor {floor_number} to go {direction}.")
        best_elevator = self.find_best_elevator(floor_number, direction)
        if best_elevator is not None:
            best_elevator.add_request(floor_number)
            print(f"Elevator at floor {best_elevator.current_floor} assigned to floor {floor_number}.")
        else:
            print("No available elevator to handle the request at this time.")
            
    def request_elevator_from_elevator(self, elevator_index, floor_number):
        if 0 <= elevator_index < len(self.elevators):
            elevator = self.elevators[elevator_index]
            print(f"Elevator {elevator_index} requested to go to floor {floor_number}.")
            elevator.add_request(floor_number)
        else:
            print("Invalid elevator index.")
    
    
    def move_elevators(self):
        for elevator in self.elevators:
            self.elevator_logic.step(elevator)
            
if __name__ == "__main__":
    manager = Elevator_manager(min_floor=0, max_floor=10, num_elevators=2)
    
    # Simulate floor requests
    manager.request_elevator_from_floor(3, "up")
    manager.request_elevator_from_floor(7, "down")
    manager.request_elevator_from_floor(1, "up")
    manager.move_elevators()
    manager.request_elevator_from_floor(9, "down")
    manager.request_elevator_from_floor(5, "up")
    manager.move_elevators()
    manager.request_elevator_from_floor(0, "up")    
    manager.request_elevator_from_floor(11, "down")
    manager.request_elevator_from_floor(4, "down")
    
    # Simulate elevator internal requests
    manager.request_elevator_from_elevator(0, 6)
    manager.request_elevator_from_elevator(1, 2)
    manager.request_elevator_from_elevator(0, 10)
    manager.move_elevators()
    manager.request_elevator_from_elevator(1, 0)
    manager.request_elevator_from_elevator(2, 5)  # Invalid elevator index
    manager.move_elevators()
    # Simulate floor requests  
    manager.request_elevator_from_floor(2, "up")
    manager.request_elevator_from_floor(8, "down")
    manager.request_elevator_from_floor(4, "up")
    manager.move_elevators()
    manager.request_elevator_from_floor(6, "down")
    manager.request_elevator_from_floor(10, "down")
    manager.move_elevators()