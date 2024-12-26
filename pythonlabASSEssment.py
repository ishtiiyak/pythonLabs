
class Vehicle:
    def __init__(self, model, brand, engine_type, horsepower):
        self.__model = model
        self.__brand = brand
        self.__engine_type = engine_type
        self.__horsepower = horsepower

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_engine_type(self):
        return self.__engine_type

    def set_engine_type(self, engine_type):
        self.__engine_type = engine_type

    def get_horsepower(self):
        return self.__horsepower

    def set_horsepower(self, horsepower):
        self.__horsepower = horsepower

    def move(self):
        print(f"{type(self).__name__} {self.__brand} {self.__model} is moving")



class Bike(Vehicle):
    pass

class Bus(Vehicle):
    pass

class Truck(Vehicle):
    pass

class Car(Vehicle):
    pass


bike = Bike("2023", "Honda", "Petrol", 150)
bus = Bus("Volvo 9700", "Volvo", "Diesel", 420)
truck = Truck("Actros", "Mercedes-Benz", "Diesel", 480)
car = Car("Civic", "Honda", "Petrol", 180)


bike.move()
bus.move()
truck.move()
car.move()
