class PaymentProcessor:
    def __init__(self,method,amount):
        self.amount=amount
        self.method=method
    def pay(self):
        method = self.method.lower()
        if method=="paypal":
            return PayPal(self.amount).pay()
        elif method=="creditcard":
            return Creditcard(self.amount).pay()
        else: 
            raise valueerror("Provide a correct payment method")
            
class PayPal:
    
    def __init__(self,amount):
        self.amount=amount
        
    def pay(self):
        print(f"amont pay by PayPal ${self.amount}")
        
class Creditcard:
    def __init__(self,amount):
        self.amount=amount
        
    def pay(self):
        print(f"amont pay by credit card ${self.amount}")
        
payment1=PaymentProcessor("paypal",1000)
payment1.pay()