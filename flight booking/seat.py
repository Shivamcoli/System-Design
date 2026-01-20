class Seat:
    def __init__(self,flight_number):
        self. flight_number = flight_number
        self.is_booked = False

    def book(self):
        if self.is_booked == False:
            print("Your seat has been booked")
            self.is_booked = True
            return True
        else:
            print("Seat is already booked try another seat")
            return False