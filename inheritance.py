# 1. Basic Inheritance

class Animal:
    def speak(self):
        print("Sound")
        
class Dog(Animal):
    pass

d=Dog()
d.speak()

# 2. Method Overriding

class Animal:
    def speak(self):
        print("Sound")
        
class Dog(Animal):
    def speak(self):
        print("Bark")

d=Dog()
d.speak()

# 3. super() — calling parent method

class Animal:
    def __init__(self,name):
        self.name=name
        
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
        print(f"Dog's created")
        
d=Dog("Buddy")
print(d.name)

# MULTI-INHERITANCE PROBLEMMULTI-INHERITANCE PROBLEM

class User:
    def __init__(self,name):
        self.name=name
        
    def get_name(self):
        return f"My name is {self.name}"
        
class Role:
    def __init__(self,role):
        self.role=role
        
    def get_role(self):
        return f"My role is {self.role}"
        
class AdminUser(User,Role):
    def __init__(self,name,role):
        super().__init__(name)
        Role.__init__(self,role)
        
    def get_details(self):
        print(self.get_name())
        print(self.get_role())

        
A1=AdminUser("Shivam","Administrator")
A1.get_details()