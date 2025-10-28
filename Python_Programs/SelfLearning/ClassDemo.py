"""
class Student:
    def __init__(self, name, age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name:{self.name}, Age: {self.age}, Grade:{self.grade}")


s1=Student("John",22,"A")
s2=Student("Alice",22,"B")
s1.display_info()
s2.display_info()

#Bank Account class

class BankAccount:
    def __init__(self, account_no,balance):
        self.account_no = account_no
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    def withdraw(self,amount):
        self.balance -= amount
        return self.balance
    def check_balance(self):
        print(f"Account No:{self.account_no}, Balance:{self.balance}")

b1=BankAccount(12345,100)
b2=BankAccount(123,200)

b1.deposit(1000)
b1.check_balance()
b1.withdraw(200)
b1.check_balance()
b2.check_balance()
b2.deposit(1000)
b2.check_balance()

class Rectangle:
    def __init__(self, length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

    def perimeter(self):
       return 2*(self.length + self.width)

r1=Rectangle(10,20)
print(r1.area())
print(r1.perimeter())

"""
import math


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_person(self):
        return f"Name:{self.name}, Age:{self.age}"

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name,age)
        self.grade = grade
    def display_student(self):
        return f"Name:{self.name}, Age:{self.age}, Grade:{self.grade}"

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name,age)
        self.subject = subject
    def display_teacher(self):
        return f"Name:{self.name}, Age:{self.age}, Subject:{self.subject}"

p=Person("John",22)
print(p.display_person())

s=Student("Riya",16,"A")
print(s.display_student())

t=Teacher("Akhil",30,"Math")
print(t.display_teacher())

print("-----------------------------------------")

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def display_info(self):
        print(f"Brand:{self.brand}, Year:{self.year}")

class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model
    def display_car(self):
        print(f"Brand:{self.brand}, Year:{self.year}, Model:{self.model}")

class ElectricCar(Car):
    def __init__(self, brand, year, model,battery_capacity):
        super().__init__(brand,year,model)
        self.battery_capacity = battery_capacity
    def display_electric_car(self):
        print(f"Brand:{self.brand}, Year:{self.year}, Model:{self.model}, Battery Capacity:{self.battery_capacity}")

e=ElectricCar("Tesla",2023,"Model S", "100kwh")
e.display_info()
e.display_car()
e.display_electric_car()

print("-----------------------------------------")

class Shape:
    def __init__(self, color):
        self.color = color
    def display_color(self):
        print(f"Color:{self.color}")

class Circle(Shape):
    def __init__(self, color,radius):
        super().__init__(color)
        self.radius = radius
    def carea(self):
        return 3.14* (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self,color,length,width):
        super().__init__(color)
        self.length = length
        self.width = width
    def rarea(self):
        return  self.length * self.width

c=Circle("Red",2)
c.display_color()
print("Area of Circle:",c.carea())

r=Rectangle("Blue",10,20)
r.display_color()
print("Area of Rectangle:", r.rarea())

