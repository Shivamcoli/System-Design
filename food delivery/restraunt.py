from food import Food

class Restraunt:
    def __init__(self,name):
        self.food_category={}
        self.name=name

    def add_food(self):
        self.food_type=int(input("Enter food type: 1) Indian 2) Chinese 3) Italian "))
        self.food_name=input("Enter food name: ")
        self.food_price=int(input("Enter food price: "))
        self.food_quantity=int(input("Enter food quantity: "))
        self.food=Food(self.food_name,self.food_price,self.food_quantity,self.food_type)
        if(self.food_type==1 or self.food_type==2 or self.food_type==3):
            self.food_category.setdefault(self.food_type,[]).append(self.food)
            print(f"{self.food_name} with food type {self.food_type} added to restraunt Menu")
            return True
        else:
            print("Invalid food type")
            return False

    def order_food(self):

        self.select_category=int(input("Select food category:1) Indian 2) Chinese 3) Italian  "))
        if self.select_category not in self.food_category:
            if(self.food_type==1 or self.food_type==2 or self.food_type==3):
                print("No food available for selected category")
            else:
                print("Invalid food category")
            return False
        self.cnt=0
        for i in self.food_category[self.select_category]:
            if i.is_available():
                print(f" {self.cnt}) {i.name} is available at price {i.price}")
                self.cnt+=1
        if self.cnt==0:
            print("Invalid food category")
            return False
        self.select_item=int(input("Enter food item number: "))
        if self.select_item >= len(self.food_category[self.select_category]):
            print("Invalid food item")
            return False
        return self.food_category[self.select_category][self.select_item].food_order()