from flight import Flight

class Flight_Service:
    def __init__(self):
        self.new_flight = None

    def addFlight(self):
        self.flight_number = input("Enter Flight Number")
        self.capacity = int(input("Enter Capacity"))
        self.boarding = input("Enter Boarding")
        self.destination = input("Enter Destination")
        self.new_flight = Flight(self.flight_number, self.capacity,self.boarding, self.destination)

        return self.new_flight

