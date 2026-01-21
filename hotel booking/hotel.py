from room import Room

class Hotel:
    def __init__(self,hotel_id,type1_room_count,type2_room_count,type1_room_cost,type2_room_cost,place):
        self.hotel_id = hotel_id
        self.place=place
        self.type1_room_count = type1_room_count
        self.type2_room_count= type2_room_count
        self.type1_room_cost = type1_room_cost
        self.type2_room_cost = type2_room_cost
        self.type1="common"
        self.type2="premium"
        self.global_room_id=1
        self.rooms={}
        for i in range(type1_room_count):
            self.rooms[self.global_room_id] = Room(self.global_room_id,self.type1_room_cost,self.type1)
            self.global_room_id+=1

        for i in range(type2_room_count):
            self.rooms[self.global_room_id] = Room(self.global_room_id,self.type2_room_cost,self.type2)
            self.global_room_id+=1

    def book_room(self):
        self.cnt=0
        for key,value in self.rooms.items():
            if value.is_available:
                self.cnt+=1
                print(f"The room with room_id : {key} is available for booking")

        if self.cnt==0:
            print(f"The rooms is not available for booking")
            return False
        self.room_id=int(input("Enter the room ID : "))
        self.status=self.rooms[self.room_id].book(self.room_id)
        if self.status==True:
            if self.rooms[self.room_id].type=="common":
                self.type1_room_count-=1
            else:
                self.type2_room_count-=1

        return self.status