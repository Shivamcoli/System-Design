from ticket import Ticket
from payment import Payment
from vehicle import Vehicle

class ParkingLot:
    def __init__(self):
        self.type1_spots = int(input("Enter number of Small vehicle spots: "))
        self.type2_spots = int(input("Enter number of Medium vehicle spots: "))
        self.type3_spots = int(input("Enter number of Large vehicle spots: "))
        
    def interact(self):
        while True:
            self.choice = int(input("1. Park Vehicle\n2. Exit Vehicle\n3. Exit\nEnter your choice: "))
            if self.choice == 1:
                vehicle = Vehicle()
                if vehicle.type == 1 and self.type1_spots <=0:
                    print("No spots available for Small vehicles.")
                elif vehicle.type == 2 and self.type2_spots <=0:
                    print("No spots available for Medium vehicles.")
                elif vehicle.type == 3 and self.type3_spots <=0:
                    print("No spots available for Large vehicles.")
                else:
                    ticket = Ticket(vehicle.license_plate, vehicle.type)
                    if vehicle.type == 1:
                        self.type1_spots -= 1
                    elif vehicle.type == 2:
                        self.type2_spots -= 1
                    elif vehicle.type == 3:
                        self.type3_spots -= 1
                    print(f"Vehicle parked. Ticket issued for {vehicle.license_plate}.")
            elif self.choice == 2:
                vehicle_number = input("Enter license plate number to exit: ")
                if vehicle_number in Ticket.ticket_list:
                    vehicle_type = Ticket.ticket_list[vehicle_number]
                    payment_processor = Payment()
                    payment_processor.make_payment(vehicle_type)
                    if vehicle_type == 1:
                        self.type1_spots += 1
                    elif vehicle_type == 2:
                        self.type2_spots += 1    
                    elif vehicle_type == 3:
                        self.type3_spots += 1
                    del Ticket.ticket_list[vehicle_number]
                    print(f"Vehicle with license plate {vehicle_number} exited.")
                else:
                    print("Invalid license plate number.")
            elif self.choice == 3:
                print("Exiting Parking Lot System.")
                break
            
if __name__ =="__main__":
    parking_lot = ParkingLot()
    parking_lot.interact()