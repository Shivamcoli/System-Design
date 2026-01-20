from seat import Seat
from flight import Flight

class Ticket:
    global_id = 1
    def __init__(self,seat_id,flight_number,passenger_name):
        self. ticket_id = Ticket.global_id
        self.seat_id = seat_id
        self.flight_number = flight_number
        self.passenger_name = passenger_name
        Ticket.global_id +=1
        print(f"Tickect had been cretaed with ticket id {self.ticket_id} on seat {seat_id} with flight number {flight_number}")