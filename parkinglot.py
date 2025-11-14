# Requirements (minimal):

# ParkingLot(capacity) — constructor sets capacity (immutable after creation).

# park(vehicleId: string) — parks a vehicle and returns assigned slot number (or -1 / error if full).

# leave(slotNumber: int) — frees the slot.

# getAvailableSlots() — returns number of free slots.

# getOccupiedSlots() — returns a list/map of slot -> vehicleId.


class parkingLot:
    

    def __init__(self,capacity):
        self._slotsEmpty=capacity
        self._capacity=capacity
        self._parking=[]
    
    def getAvailableSlots(self):
        return self._slotsEmpty
    def getOccupiedSlots(self):
        
        return self._parking.copy()
    
    def park(self,vehicleId):
        if self._slotsEmpty==0:
            return "sorry parking lot is full"
        else:
            self._parking.append(vehicleId)
            self._slotsEmpty-=1
            
    def leave(self,vehicleId):
        if vehicleId in self._parking:
            self._parking.remove(vehicleId)
            self._slotsEmpty+=1
            
lot=parkingLot(5)
print(lot.getAvailableSlots())
lot.park("KA-01-HH-1234")
print(lot.getOccupiedSlots())
lot.park("KA-01-HH-9999")
print(lot.getOccupiedSlots())
lot.leave("KA-01-HH-1234")
print(lot.getOccupiedSlots())