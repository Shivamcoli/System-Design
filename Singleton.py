class Car:
    def __init__(self, name):
        self.name = name
    
    def drive(self):
        print( f"{self.name} is driving.")
    
    def stop(self):
        print ( f"{self.name} has stopped.")
    
obj1 = Car("Toyota")
obj1.drive()
obj1.stop()    
