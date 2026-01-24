# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
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
# food delivery:
# food ,  user, order, restraunt, food delivery system
from food_delivery_system import FoodDeliverySystem
if "__main__" == __name__:
    food_delivery_system = FoodDeliverySystem()
    while True:
        choice=int(input(f"1)Add restraunt 2)Add Food 3)order Food 4)Exit : "))
        if choice == 1:
            food_delivery_system.add_restraunt()
        if choice == 2:
            food_delivery_system.add_food_to_restraunt()
        if choice == 3:
            food_delivery_system.order_food()
        if choice == 4:
            break