class Vehicle:
    def __init__(self,model,brand,enginetype,hoursepower):
        self.__model=model
        self.__brand=brand
        self.__enginetype=enginetype
        self.__hoursepower=hoursepower
    def move(self):
        print("vehicle is moving")
    
    @property
    def model(self):
        return self.__model
    @property
    def brand(self):
        return self.__brand
    @property
    def enginetype(self):
        return self.__enginetype
    @property
    def hoursepower(self):
        return self.__hoursepower
class Car(Vehicle):
    def move(self):
        print("vehicle is moving")
class Bus(Vehicle):
    def move(self):
        print("Bus is moving")
class Truck(Vehicle):
    def move(self):
        print("vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("vehicle is moving")


class Bus(Vehicle):

    def move(self):
        print("Bus is moving")

class Truck(Vehicle):   

    def move(self):
        print("vehicle is moving")

class Bike(Vehicle):

    def move(self):
        print("Bike is moving")

bike1 = Bike("2023","honda","cc","23")
car1 = Car("2023","honda","cc","23")
Bus1 = Bus("209","uet","nonc","203")
Truck1 = Truck("223","bmw","classy","50")
print(bike1.model)
print(bike1.brand)
print(bike1.enginetype)
print(bike1.hoursepower)
print(f'the vehicle is a {bike1.model} brand is {bike1.brand} engine type: {bike1.enginetype} and has {bike1.hoursepower} hp engine ')

print('-*-*-*-*-*-*-*-*-*')


print(f'the vehicle is a {car1.model} brand is {car1.brand} engine type: {car1.enginetype} and has {car1.hoursepower} hp engine ')

print('-*-*-*-*-*-*-*-*-*')

print(f'the vehicle is a {Bus1.model} brand is {Bus1.brand} engine type: {Bus1.enginetype} and has {Bus1.hoursepower} hp engine ')

print('-*-*-*-*-*-*-*-*-*')

print(Truck1.model)
print(Truck1.brand)
print(Truck1.enginetype)
print(Truck1.hoursepower)

print('-*-*-*-*-*-*-*-*-*')




bike1.move()
car1.move()
Bus1.move()
Truck1.move()







        
   
    
    
    














