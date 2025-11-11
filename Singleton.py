class Car:
    _instance = None
    
    def __new__(cls, name):
        if cls._instance is None:
            cls._instance = super(Car, cls).__new__(cls)
            cls._instance.name = name
        return cls._instance
    
    def drive(self):
        print( f"{self.name} is driving.")
    
    def stop(self):
        print ( f"{self.name} has stopped.")
    
obj1 = Car("Toyota")
obj1.drive()
obj1.stop()    
obj2= Car("Honda")
obj2.drive()

class Bike:
    _instance = None
    
    def __new__(cls,name):
        if cls._instance is None:
            cls._instance = super(Bike,cls).__new__(cls)
            cls._instance.name=name
        return cls._instance
    
    def ride(self):
        print(f"{self.name} is riding.")    
        
    def park(self):
        print(f"{self.name} is parked.")
        
obj3 = Bike("Yamaha")
obj3.ride()
obj3.park()
obj4 = Bike("Ducati")
obj4.ride()