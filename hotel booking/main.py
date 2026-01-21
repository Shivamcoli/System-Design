# # This is a sample Python script.
# from Demos.win32ts_logoff_disconnected import username
# from torch.ao.ns.fx.utils import rekey_logger_info_on_node_name_of_model
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
# 1)hotel
# 2)booking
# 3)user
# 4)room
# 5) room_type
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
from booking_manager import Booking_Manager
from hotel_manager import HotelManager
if __name__ =="__main__":
    hotel_manager = HotelManager()
    while True:
        x=int(input("Enter your choice: 1) Add hotel 2) Book Hotel 3) Exit "))
        if x==3:
            break
        if x==1:
            hotel_manager.add_hotel()
        elif x==2:
            bm=Booking_Manager()
            bm.book(hotel_manager)

