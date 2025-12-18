class Logic:
    def move(self, elevator):
        # Continue while there are any floors left to visit
        while elevator.up_direction_floors or elevator.down_direction_floors:
            
            # 1. UPWARD PHASE
            if elevator.up_direction_floors:
                elevator.direction = "up"
                elevator.up_direction_floors.sort() # Ensure we hit floors in order
                
                # Filter for floors that are actually above us
                above = [f for f in elevator.up_direction_floors if f >= elevator.current_floor]
                
                if above:
                    for floor in above:
                        print(f"Elevator {elevator.id} moving UP from {elevator.current_floor} to {floor}")
                        elevator.current_floor = floor
                        elevator.up_direction_floors.remove(floor)
                else:
                    # If floors remain but they are BELOW us, we must pivot
                    # We move to the lowest floor in that list to start the next cycle
                    lowest = min(elevator.up_direction_floors)
                    print(f"Elevator {elevator.id} resetting to floor {lowest} to handle remaining UP tasks")
                    elevator.current_floor = lowest
            
            # 2. DOWNWARD PHASE
            if elevator.down_direction_floors:
                elevator.direction = "down"
                elevator.down_direction_floors.sort(reverse=True) # Sort descending
                
                # Filter for floors that are actually below us
                below = [f for f in elevator.down_direction_floors if f <= elevator.current_floor]
                
                if below:
                    for floor in below:
                        print(f"Elevator {elevator.id} moving DOWN from {elevator.current_floor} to {floor}")
                        elevator.current_floor = floor
                        elevator.down_direction_floors.remove(floor)
                else:
                    # If floors remain but they are ABOVE us, we must pivot
                    highest = max(elevator.down_direction_floors)
                    print(f"Elevator {elevator.id} resetting to floor {highest} to handle remaining DOWN tasks")
                    elevator.current_floor = highest
        
        elevator.direction = "idle" # Finish and wait