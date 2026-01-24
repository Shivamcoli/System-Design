from restraunt import Restraunt
from user import User

class FoodDeliverySystem:
    def __init__(self):
        self.restraunt_list={}
        self.global_restraunt_cnt=1

    def add_restraunt(self):

        self.name=input("Please enter your name of restraunt: ")
        self.new_restraunt = Restraunt(self.name)
        self.restraunt_list[self.global_restraunt_cnt] = self.new_restraunt
        self.global_restraunt_cnt+=1

    def add_food_to_restraunt(self):
        for res_id,res in self.restraunt_list.items():
            print(f"{res_id}) Restraunt is {res.name}")
        self.selected_restraunt_id = int(input("Please enter your restraunt id_number to add food item: "))
        if self.selected_restraunt_id not in self.restraunt_list:
            print("Enter a vaild restraunt id_number")
            return False
        self.is_added=self.restraunt_list[self.selected_restraunt_id].add_food()
        if self.is_added:
            print(f"Food item is added to restraunt {self.name}")
            return True
        else:
            print(f"Food item is not added to restraunt {self.name}")
            return False

    def order_food(self):
        print("Select 1 restrant to continue food odering")
        for res_id,res in self.restraunt_list.items():
            print(f"{res_id}) Restraunt is {res.name}")
        self.selected_restraunt_id = int(input("Please enter your restraunt id_number to order: "))
        if self.selected_restraunt_id not in self.restraunt_list:
            print("Enter a vaild restraunt id_number")
            return False
        self.is_ordered=self.restraunt_list[self.selected_restraunt_id].order_food()
        if self.is_ordered == False:
            print("Unable to order food")
            return False
        print("Food ordering is successful")
        return True
