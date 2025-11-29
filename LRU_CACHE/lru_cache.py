from collections import OrderedDict

class LRU_CACHE:

    def __init__(self,capacity):
        self.capacity=capacity
        self.cache=OrderedDict()
        
    def put(self,key,value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache)>=self.capacity:
            self.cache.popitem(last=True)
        self.cache[key]=value   
        self.cache.move_to_end(key,last=False)
        for k,v in self.cache.items():
            print(f"{k}:{v}",end=" ")
        print(" ")
        
    def get(self,key):
        if key not in self.cache:
            print(-1)
            return
        
        print(self.cache[key])
        self.cache.move_to_end(key,last=False)
        
        for k,v in self.cache.items():
            print(f"{k}:{v}",end=" ")
        print(" ")
        
            
if __name__=="__main__":
    lru=LRU_CACHE(3)
    lru.put(1,'A')
    lru.put(2,'B')
    lru.put(3,'C')
    lru.get(2)
    lru.put(4,'D')
    lru.get(1)
    lru.get(3)
    lru.get(4)