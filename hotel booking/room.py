class Room:

    def __init__(self,room_id,room_cost,type):
        self.id = room_id
        self.cost = room_cost
        self.type = type
        self.is_available = True

    def book(self,room_id):
        if self.is_available== False:
            print(f"The room with id {room_id} is not available")
            return False
        self.id = room_id
        self.is_available = False
        print(f"The room {room_id} is succesfully booked")
        return True