# Object-Oriented Programming (OOP) in Python
# ===========================================
# OOP is a programming paradigm that uses objects and classes to structure code.

# 1. Class and Object
class Car:
    def __init__(self, brand, model):
        # Initialize attributes brand and model with values passed during object creation
        self.brand = brand  # Attribute to store the brand of the car
        self.model = model  # Attribute to store the model of the car

    def display_info(self):
        # Method to print the car's brand and model
        print(f"Car: {self.brand} {self.model}")

# Creating an object (instance) of the Car class
car1 = Car("Toyota", "Corolla")
car1.display_info()  # Output: Car: Toyota Corolla

# 2. Inheritance
class ElectricCar(Car):  # ElectricCar inherits from Car
    def __init__(self, brand, model, battery_capacity):
        # Call the parent class's constructor to initialize common attributes
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity  # New attribute specific to ElectricCar

    def display_info(self):
        # Override the parent class's display_info method to include battery capacity
        super().display_info()  # Call the parent class's method
        print(f"Battery Capacity: {self.battery_capacity} kWh")

# Creating an object of the derived class ElectricCar
e_car = ElectricCar("Tesla", "Model S", 100)
e_car.display_info()
# Output:
# Car: Tesla Model S
# Battery Capacity: 100 kWh

# 3. Polymorphism
class GasCar(Car):
    def __init__(self, brand, model, fuel_type):
        # Call the parent class's constructor to initialize common attributes
        super().__init__(brand, model)
        self.fuel_type = fuel_type  # New attribute specific to GasCar

    def display_info(self):
        # Override the parent class's display_info method to include fuel type
        print(f"Gas Car: {self.brand} {self.model} (Fuel: {self.fuel_type})")

# Demonstrating polymorphism
vehicles = [car1, e_car, GasCar("Ford", "Mustang", "Petrol")]
for vehicle in vehicles:
    vehicle.display_info()  # Each object calls its own version of display_info

# 4. Encapsulation
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance  # Private attribute to restrict direct access

    def deposit(self, amount):
        # Add money to the account if the amount is positive
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        # Withdraw money if the amount is within the available balance
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance or invalid amount")

    @property
    def balance(self):
        # The @property decorator allows access to this method as if it were an attribute
        return self.__balance

# Creating a bank account object
account = BankAccount("Ishtiyaq", 1000)
account.deposit(500)  # Add 500 to the account
account.withdraw(200)  # Withdraw 200 from the account
print(f"Balance: {account.balance}")  # Accessing the balance using the @property method

# 5. Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    # Abstract base class to define a blueprint for shapes
    @abstractmethod
    def area(self):
        pass  # Must be implemented by subclasses

    @abstractmethod
    def perimeter(self):
        pass  # Must be implemented by subclasses

class Rectangle(Shape):
    def __init__(self, length, width):
        # Initialize the dimensions of the rectangle
        self.length = length
        self.width = width

    def area(self):
        # Calculate and return the area of the rectangle
        return self.length * self.width

    def perimeter(self):
        # Calculate and return the perimeter of the rectangle
        return 2 * (self.length + self.width)

# Instantiating a concrete class Rectangle
rect = Rectangle(10, 5)  # Create a rectangle with length 10 and width 5
print(f"Rectangle Area: {rect.area()}")  # Output: 50
print(f"Rectangle Perimeter: {rect.perimeter()}")  # Output: 30
