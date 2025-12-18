class Elevator:
    
    def __init__(self,id,min_floor, max_floor):
        self.id = id
        self.current_floor = 0
        self.direction = "idle"  # can be "up", "down", or "idle"
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.request_up =[]
        self.request_down =[]
        
    def add_request(self, floor):
        if floor > self.current_floor:
            if floor not in self.request_up:
                self.request_up.append(floor)
                self.request_up.sort()
                print(f"Request added to go up to floor {floor}. Current up requests: {self.request_up}")
        elif floor < self.current_floor:
            if floor not in self.request_down:
                self.request_down.append(floor)
                self.request_down.sort(reverse=True)
                print(f"Request added to go down to floor {floor}. Current down requests: {self.request_down}")
                
        