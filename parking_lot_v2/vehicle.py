class Vehicle:
    def __init__(self):
        self.license_plate = input("Enter license plate number: ")
        self.type = 0
        while True:
            choice = int(input("Enter vehicle type (1. Small, 2. Medium, 3. Large): "))
            if choice in [1, 2, 3]:
                self.type = choice
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")