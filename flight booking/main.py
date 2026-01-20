# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# flight booking system
# entittes = ticket ,booking, seat, flight

from flight_booking_sytem import Flight_Booking_System

if __name__ == "__main__":
    flight_booking_system = Flight_Booking_System()
    while(True):
        x=int(input("Enter choice 1) Register flight 2) Exit "))
        if x==2:
            break
        flight_booking_system.add_flight()

    while(True):
        x = int(input("Enter choice 1) Book flight 2) Exit "))
        if x == 2:
            break
        flight_booking_system.book()