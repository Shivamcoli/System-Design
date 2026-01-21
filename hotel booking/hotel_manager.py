from hotel import Hotel

class HotelManager:
    def __init__(self):
        self.hotels = {}
        self.hotel_id=1

    def add_hotel(self):
        self.type1_room_count=int(input("Enter type 1 room count: "))
        self.type2_room_count=int(input("Enter type 2 room count: "))
        self.type1_room_cost=int(input("Enter type 1 room cost: "))
        self.type2_room_cost=int(input("Enter type 2 room cost: "))
        self.place=input("Enter place where hotel located: ")
        self.hotels[self.hotel_id] = Hotel(self.hotel_id,self.type1_room_count,self.type2_room_count,self.type1_room_cost,self.type2_room_cost,self.place)

        print(f"Hotel added with id {self.hotel_id} ")
        self.hotel_id += 1

    def book_hotel_room(self,place):
        self.cnt=0
        for key,value in self.hotels.items():
            if value.place==place:
                self.cnt+=1
                if value.type1_room_count>0 or value.type2_room_count>0:
                    print(f"The hotel with hotel id {value.hotel_id} with rooms available 1) Common:{value.type1_room_count}, 2)Premium:{value.type2_room_count} ")

        if self.cnt==0:
            print("No hotel at place found")
            return False
        else:
            self.selected_hotel_id=int(input("Select hotel id: "))
            self.status = self.hotels[self.selected_hotel_id].book_room()
            return True