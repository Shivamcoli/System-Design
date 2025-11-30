from parkingspot import ParkingSpot
from payment import PaymentProcessor
from vehicle import Vehicle
from ticket import Ticket

class ParkingLot:
    def __init__(self,capacity):
        self.spots=[]
        for i in range(1,capacity+1):
            if i <= capacity//3:
                size=1  # Small spot
            elif i <= 2*capacity//3:
                size=2  # Medium spot
            else:
                size=3  # Large spot
            self.spots.append(ParkingSpot(i,size))
            
            
    def find_spot(self,vehicle_type):
        for spot in self.spots:
            if spot.is_available() and spot.size == vehicle_type:
                return spot
        return None
    
    def park_vehicle(self,vehicle):
        spot = self.find_spot(vehicle.type)
        if spot:
            spot.assign_vehicle(vehicle)
            ticket = Ticket(spot.get_spot_id())
            print(f"Vehicle parked in spot {spot.get_spot_id()}. Ticket ID: {ticket.get_ticket_id()}")
            return ticket
        else:
            print("No available spot for this vehicle type.")
            return None
        
        
    def unpark_vehicle(self,ticket):
        spot_id = ticket.get_spot_id()
        spot = self.spots[spot_id - 1]  
        if spot.is_occupied:
            payment_processor = PaymentProcessor()
            payment_processor.pay(spot.vehicle.type)
            spot.remove_vehicle()
            print(f"Vehicle unparked from spot {spot.get_spot_id()}.")
        else:
            print("Spot is already empty.")
            
    def get_status(self):
        for spot in self.spots:
            status = "Occupied" if spot.is_occupied else "Available"
            print(f"Spot ID: {spot.get_spot_id()}, Size: {spot.size}, Status: {status}")
            
if __name__ == "__main__":
    parking_lot = ParkingLot(9)  # Create a parking lot with 9 spots
    while True:
        print("\n1. Park Vehicle\n2. Unpark Vehicle\n3. Get Parking Lot Status\n4. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            vehicle = Vehicle()
            parking_lot.park_vehicle(vehicle)
        elif choice == 2:
            ticket_id = int(input("Enter Ticket ID: "))
            # In a real system, we would look up the ticket by ID
            # Here we will assume the ticket ID corresponds to the spot ID for simplicity
            ticket = Ticket(ticket_id)  # Vehicle is None for unpark operation
            parking_lot.unpark_vehicle(ticket)
        elif choice == 3:
            parking_lot.get_status()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")
        