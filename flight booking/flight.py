from seat import Seat

class Flight:

    def __init__(self, flight_number, capacity,boarding,destination):
        self.flight_number = flight_number
        self.capacity = capacity
        self.boarding = boarding
        self.destination = destination
        self.seats = {}

        for i in range(capacity):
            self.seats[i]=Seat(flight_number)


    def get_available_seats(self):
        c=0
        for key,value in self.seats.items():
            if value.is_booked == False:
                c+=1
                print(f"seat number{key +1} is available" )
        return c


    def book_seat(self,seat_id):
        try:
            seat_id = int(seat_id)
        except ValueError:
            print("Please enter a valid number")
            return False
        seat_id-=1
        if seat_id in self.seats:
            return self.seats[seat_id].book()
        else:
            print("Invalid Seat ID")
            return False