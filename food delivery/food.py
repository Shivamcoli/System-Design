class Food:
    def __init__(self, name, price, quantity,category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def is_available(self):
        return self.quantity > 0

    def food_order(self):
        self.quantity -= 1
        print(f"{self.name} is ordered")
        return True