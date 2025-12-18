from elevator import Elevator

class Elevator_logic:

    def step(self, elevator):

        if elevator.direction == "idle":
            if elevator.request_up:
                elevator.direction = "up"
            elif elevator.request_down:
                elevator.direction = "down"
            else:
                print(f"Elevator {elevator.id} idle at floor {elevator.current_floor}")
                return

        if elevator.direction == "up":
            next_floor = elevator.request_up.pop(0)
            elevator.current_floor = next_floor
            print(f"Elevator {elevator.id} moving UP to floor {next_floor}")

            if not elevator.request_up:
                elevator.direction = "down" if elevator.request_down else "idle"

        elif elevator.direction == "down":
            next_floor = elevator.request_down.pop(0)
            elevator.current_floor = next_floor
            print(f"Elevator {elevator.id} moving DOWN to floor {next_floor}")

            if not elevator.request_down:
                elevator.direction = "up" if elevator.request_up else "idle"

            
        