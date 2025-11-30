class ParkingSpot:
    def __init__(self, spot_id,size):
        self.spot_id = spot_id
        self.vehicle=None
        self.size = size  # 1: Small, 2: Medium, 3: Large
        self.is_occupied = False
        
    def is_available(self):
        return not self.is_occupied
    
    def assign_vehicle(self,vehicle):
        self.vehicle = vehicle
        self.is_occupied = True
        
    def remove_vehicle(self):
        self.vehicle = None
        self.is_occupied = False
        
    def get_spot_id(self):
        return self.spot_id