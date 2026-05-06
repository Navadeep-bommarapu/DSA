class Account:
    
    def __init__(self, bal, acc_pass): # constructor
        self.bal = bal
        self.__acc_pass = acc_pass # private attribute
    
    @staticmethod # decorator
    def say_hi(): 
        print("hi")
        
    def __hello(self, acc_pass): # private method
        print(acc_pass)
        
    
    def print_acc_pass(self):
        self.__hello(self.__acc_pass)
    

class Person:
    name = "Tom"
    
    @classmethod # decorator
    def change_name(cls, name):
        cls.name = name
    
# p1 = Person()
# print(p1.name)
# p1.change_name("George")
# print(p1.name)

class Student:
    
    def __init__(self, math, phy, chem):
        self.math = math
        self.phy = phy
        self.chem = chem
        
    @property #decorator
    def percentage(self):
        return str((self.math + self.phy + self.chem)/3) + "%"
        
# s1 = Student(89, 90, 100)
# print(s1.percentage)
        

# Abstraction - Hiding complexity, show only what's needed
class Car:
    def start(self):
        self.__ignite_engine()
        self.__control_fuel()
        print("Car starts")
    
    def __ignite_engine(self):
        print("Engine ignition...")
        
    def __control_fuel(self):
        print("Fuel System active...")

# car = Car()
# car.start()

# Encapsulation - wrapping data or function
class Phone:
    def __init__(self, model, brand):
        self.__model = model
        self.__brand = brand
    
    def access_phone_details(self):
        print(self.__model, self.__brand)
    
    def change_model(self, model):
        self.__model = model
        print("Model changed to:", self.__model)

# phone = Phone("s24", "samsung")
# phone.access_phone_details()
# phone.change_model("s25 ultra")

# Inheritance - class having access to its parent's attributes
class AmericanChef:
    
    location = "America"
    
    def makes_chicken(self):
        print("The chef makes chicken")
        return "Chicken"
    
    def makes_steak(self):
        print("The chef makes steak")

class ItalianChef(AmericanChef): # single inheritance
    
    location = "Italy"
        
    def makes_pasta(self):
        print("The chef makes pasta ")
    
    def makes_pizza(self):
        print("The chef makes pizza")

class IndianChef(ItalianChef): # multi-level inheritance
    
    location = "Indian"
        
    def makes_biryani(self):
        print("The chef makes biryani")

    def makes_butter_chicken(self):
        print("The chef makes butter chicken")
        
class Ingredients:
    
    def dishes(self):
        print("chicken, pasta, chilli powder, salt, oil, water, eggs, butter, flour, milk, tomatos, onions")
        
    
class Chef(IndianChef, Ingredients, AmericanChef): # multiple inheritance
    
    def chef_attributes(self):
        print(self.location) # prints the location from the first inherited class
        print("The Chef lives in",self.location, "and he prepares", self.makes_chicken())

# chef = Chef()
# chef.chef_attributes()

# Polymorphism
class Complex:
     
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def show_complex(self):
        print(self.real ,"i +", self.img, "j")
    
    def add(self, num):
        newReal = self.real + num.real
        newImg = self.img + num.img
        return Complex(newReal, newImg)
    
    def __add__(self, num):
        newReal = self.real + num.real
        newImg = self.img + num.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num):
        newReal = self.real - num.real
        newImg = self.img - num.img
        return Complex(newReal, newImg)
        
# num1 = Complex(1,3)
# num1.show_complex()

# num2 = Complex(4,5)
# num2.show_complex()

# num3 = num1 + num2
# num3.show_complex()


# super() method - used to access parent's methods or constructors from the child class
class Parent:
    def __init__(self, name):
        self.name = name
        
    def show(self):
        print("Name:", self.name)
        
    
class Child(Parent):
    def __init__(self, name):
        super().__init__(name)
        
child = Child("Tom")
