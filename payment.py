from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self,amount):
        self.amount=amount
    @abstractmethod   
    def pay(self):
         pass   
            
class PayPal(Payment):
    def pay(self):
        print(f"amount paid using PayPal: ${self.amount}")
        
class CreditCard(Payment):
    def pay(self):
        print(f"amount paid using Credit Card: ${self.amount}")
        
class PaymentProcessor:
    def __init__(self,method):

        self.method=method
        
    def pay(self):
        self.method.pay()

        
payment1=PaymentProcessor(PayPal(1500))
payment1.pay()