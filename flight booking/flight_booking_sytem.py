from seat import Seat
from ticket import Ticket
from flight import Flight
from flight_service import Flight_Service

class Flight_Booking_System:
    def __init__(self,):
        self.name = input("Enter your name ")
        self.flight={}
        self.ticket=[]

    def add_flight(self):
        self.new_flight=Flight_Service().addFlight()
        self.flight[self.new_flight.flight_number]=self.new_flight
        print("New flight added")

    def book(self):
        self.boarding=input("Enter boarding station ")
        self.destination=input("Enter destination ")
        print("Showing the available flights")
        c=0
        for key,value in self.flight.items():
            if value.boarding == self.boarding and value.destination == self.destination:
                c=c+1
                print(value.flight_number)
        if c==0:
            print("No flights available")
        else:
            self.book_flight_number=input("Enter Flight Number for booking")
            available_flights=self.flight[self.book_flight_number].get_available_seats()
            if available_flights==0:
                print("All seats booked")
            else:
                self.seat_book=int(input("Enter seat you want to book: "))
                self.booked =self.flight[self.book_flight_number].book_seat(self.seat_book)
                if self.booked is True:
                    self.tkt=Ticket(self.seat_book,self.book_flight_number,self.name)
                    self.ticket.append(self.tkt)


