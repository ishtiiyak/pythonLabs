"""
Object Oriented Programming (OOP) and Data Encapsulation
=======================================================

1. Object Oriented Programming (OOP)
-----------------------------------
OOP is a programming paradigm based on the concept of "objects" which can contain:
- Data (attributes/properties)
- Code (methods/functions)

Key OOP Concepts:
a) Encapsulation: Bundling data and methods that operate on that data within a single unit
b) Inheritance: Creating new classes that are built upon existing classes
c) Polymorphism: Ability of objects to take multiple forms
d) Abstraction: Hiding complex implementation details and showing only necessary features

2. Data Encapsulation
---------------------
Data encapsulation is a fundamental concept in OOP that:
- Bundles related data and methods together into a single unit (class)
- Restricts direct access to some object's components
- Prevents unintended interference and misuse of data

Access Modifiers in Python:
- Public: name      (no underscore)
- Protected: _name  (single underscore)
- Private: __name   (double underscore)

Example of Data Encapsulation:
"""

class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private attribute
        self._account_type = "Savings"  # Protected attribute
        self.bank_name = "MyBank"  # Public attribute
    
    # Getter method for balance
    def get_balance(self):
        return self.__balance
    
    # Setter method for balance
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            raise ValueError("Balance cannot be negative")

"""
3. Getter and Setter Methods
---------------------------
Getters and setters are methods that:
- Allow controlled access to class attributes
- Implement encapsulation by providing indirect access to private attributes
- Enable validation of data before setting values
- Help maintain data integrity

Benefits of using getters and setters:
1. Data Validation
2. Read-only or Write-only access
3. Flexibility to change implementation
4. Maintaining encapsulation

Different ways to implement getters and setters in Python:
"""

# 1. Traditional Method
class Student:
    def __init__(self):
        self.__name = ""
        
    def get_name(self):
        return self.__name
        
    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise TypeError("Name must be a string")

# 2. Using @property decorator
class Employee:
    def __init__(self):
        self.__salary = 0
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value
        else:
            raise ValueError("Salary must be positive")

"""
Best Practices for Data Encapsulation:
1. Always make instance variables private unless required otherwise
2. Provide public methods to access and modify private variables
3. Implement validation in setter methods
4. Use meaningful names for getter and setter methods
5. Consider using @property decorator for cleaner syntax

Summary:
--------
- OOP helps organize code into reusable and maintainable objects
- Data encapsulation protects data integrity and implements information hiding
- Getter and setter methods provide controlled access to class attributes
- Python offers multiple ways to implement encapsulation and access control
- Following best practices ensures better code organization and maintenance
"""












"""
Polymorphism and Magic Methods in Python
======================================

Polymorphism allows objects of different classes to be treated as objects of a common base class.
Magic methods (dunder methods) enable operator overloading and customizing object behavior.
"""

# 1. Method Overriding (Polymorphism)
class Animal:
    def make_sound(self):
        return "Some sound"


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


# 2. Magic Methods Example
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# 3. Duck Typing
class Duck:
    def swim(self):
        return "Swimming like a duck"
    
    def fly(self):
        return "Flying like a duck"


class Swan:
    def swim(self):
        return "Swimming like a swan"
    
    def fly(self):
        return "Flying like a swan"


def make_bird_swim(bird):
    return bird.swim()  # Works for any object with swim() method


"""
Best Practices for Polymorphism and Magic Methods:

1. Use method overriding to customize behavior in derived classes
2. Implement magic methods to make objects behave like built-in types
3. Follow the Liskov Substitution Principle
4. Use duck typing when appropriate
5. Keep magic method implementations consistent with Python conventions

Summary:
--------
- Polymorphism enables code reuse and flexibility
- Method overriding allows customizing behavior in derived classes
- Magic methods provide a way to integrate custom objects with Python's built-in operations
- Duck typing focuses on object capabilities rather than specific types
- Proper use of polymorphism and magic methods leads to more elegant and maintainable code
"""

