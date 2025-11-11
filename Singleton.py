class Car:
    def __init__(self, name):
        self.name = name
    
    def drive(self):
        return f"{self.name} is driving."
    
    def stop(self):
        return f"{self.name} has stopped."
    
obj1 = Car("Toyota")
obj1.drive()
obj1.stop()    
