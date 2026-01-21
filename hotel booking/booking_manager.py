from hotel_manager import HotelManager

class Booking_Manager:
    def __init__(self):
        self.name=input("Enter your name: ")
        self.place=input("Enter place in which you want to book hotel: ")

    def book(self,manger_obj):
        self.status=manger_obj.book_hotel_room(self.place)
        if self.status==False:
            print("Booking manager Failed")
        return self.status