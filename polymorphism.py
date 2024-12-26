# This module demonstrates polymorphism and magic methods in Python

# Example of method overriding (dynamic polymorphism)
# Base class for shapes
class Shape:
    def area(self):
        return "Area of shape"

# Circle class inherits from Shape and overrides area()
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Rectangle class also inherits from Shape and provides its own area()
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Demonstrate polymorphic behavior by calling area() on different shapes
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"Area: {shape.area()}")

# Example of polymorphism through duck typing
class Dog:
    def speak(self):
        return "Bark"

class Cat:
    def speak(self):
        return "Meow"

# Function works with any object that has a speak() method
def make_animal_speak(animal):
    print(animal.speak())

# Call function with different animal types
make_animal_speak(Dog())  # Output: Bark
make_animal_speak(Cat())  # Output: Meow

# Example of polymorphism with abstract base classes
from abc import ABC, abstractmethod

# Abstract base class that enforces speak() implementation
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete implementations must provide speak()
class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"

# Use abstract class implementations polymorphically
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())

# Examples of magic methods (dunder methods)

# Person class demonstrating __init__ and __str__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

# Vector class showing operator overloading with __add__
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Student class showing comparison magic methods
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade

# CustomList showing container magic methods
class CustomList:
    def __init__(self, elements):
        self.elements = elements

    def __getitem__(self, index):
        return self.elements[index]

    def __len__(self):
        return len(self.elements)

# Example usage of magic methods
person = Person("Alice", 30)
print(person)  # Output: Alice, 30 years old

v1 = Vector(2, 3)
v2 = Vector(4, 5)
print(v1 + v2)  # Output: Vector(6, 8)

s1 = Student("Alice", 85)
s2 = Student("Bob", 90)
print(s1 == s2)  # Output: False
print(s1 < s2)   # Output: True

lst = CustomList([1, 2, 3, 4])
print(lst[2])  # Output: 3
print(len(lst))  # Output: 4