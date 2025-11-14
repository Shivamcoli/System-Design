



curreny={"INR":[["USD",80.8],["DHR",22.7],["EUR",88.9]],"USD":[["INR",0.012],["DHR",0.28],["EUR",1.1]],
         "DHR":[["INR",0.044],["USD",3.5],["EUR",4.0]],"EUR":[["INR",0.011],["USD",0.9],["DHR",0.25]]}

# def Convert(c1,c2,amt,vis):
#     if c1 in vis:
#         return -1
#     vis[c1]=True
#     if c1==c2:
#         return amt
#     x = -1
#     for convertion_rate in curreny[c1]:
        
#        x=Convert(convertion_rate[0],c2,convertion_rate[1]*amt,vis)
#        if x!=-1:
#            return x
    
#     return -1

# print(Convert("INR","EUR",1,{}))
# print("Yo")

from abc import ABC,abstractmethod

class CurrencyCoverter:
    def __init__(self,curreny_rates):
        self.curreny_rates=curreny_rates
    @abstractmethod
    def convert(self):
        pass
    
class Converter(CurrencyCoverter):
    
    def convert(self,c1,c2,amt,vis):
        if c1 in vis:
            return -1
        vis[c1]=True
        if c1==c2:
            return amt
        x = -1
        for convertion_rate in self.curreny_rates[c1]:
            
           x=self.convert(convertion_rate[0],c2,convertion_rate[1]*amt,vis)
           if x!=-1:
               return x
        
        return -1
    
convertion1=Converter(curreny)
print(convertion1.convert("INR","EUR",1,{}))