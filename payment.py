from abc import ABC, abstractmethod


# /* payment method for startegic patten*/
# class Payment(ABC):
#     def __init__(self,amount):
#         self.amount=amount
#     @abstractmethod   
#     def pay(self):
#          pass   
            
# class PayPal(Payment):
#     def pay(self):
#         print(f"amount paid using PayPal: ${self.amount}")
        
# class CreditCard(Payment):
#     def pay(self):
#         print(f"amount paid using Credit Card: ${self.amount}")
        
# class PaymentProcessor:
#     def __init__(self,method):

#         self.method=method
        
#     def pay(self):
#         self.method.pay()

        
# payment1=PaymentProcessor(PayPal(1500))
# payment1.pay()

# Paymrnt method for factory pattern

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

class PaymentFactory:
    def get_payment_method(method,amount):
        method=method.lower()
        if method=="paypal":
            return PayPal(amount)
        elif method=="creditcard":
            return CreditCard(amount)        
        else:
            raise ValueError("Provide a correct payment method")
        
payment1=PaymentFactory.get_payment_method("paypal",1000)
processor=PaymentProcessor(payment1)
processor.pay()