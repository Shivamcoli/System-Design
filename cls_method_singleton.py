#  Payment:
#     classdef __init__(self, amount):
#         self.amount = amount

#     @classmethod
#     def create_paypal(cls, amount):
#         return cls(amount)
    
# p = Payment.create_paypal(500)
# print(f"Payment amount via PayPal: ${p.amount}")

class User:
    user_count = 0
    def __init__(self,name):
        self.name=name
    @classmethod   
    def create_user(cls,name):
        cls.user_count+=1
        return cls(name)
    
    
u1 = User.create_user("Shivam")
u2 = User.create_user("Coli")
u3 = User.create_user("Aman")

print(User.user_count)   # 3
print(u1.name, u2.name, u3.name)


class Database:
    _instance=None
    def __new__(cls,*args,**kwargs):
        if not cls._instance:
            cls._instance=super(Database,cls).__new__(cls)
        return cls._instance
    

a=Database()
b=Database()
print(a is b)  # True
