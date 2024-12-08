from abc import ABC, abstractmethod

class Vehicle (ABC): 
    @abstractmethod

    def start_engine(self) -> str:
     pass

class Car(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        return f"{self.make} {self.model}: Двигун запущено"

class Motorcycle(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        return f"{self.make} {self.model}: Мотор заведено"

class VehicleFactory(ABC):
    @abstractmethod

    def create_car(self, make, model) -> Car:
        pass
        
    def create_motorcycle(self) -> Motorcycle:
        pass
     
class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model) -> Car:
        return Car(make, model)
    
    def create_motorcycle(self, make, model) -> Motorcycle:
        return Motorcycle(make, model)
    
class EuropeVehicleFactory(VehicleFactory):
    def create_car(self, make, model) -> Car:
        return Car(make, model)

    def create_motorcycle(self, make, model) -> Motorcycle:
        return Motorcycle(make, model)
    
# Використання
europe_factory = EuropeVehicleFactory()
us_factory = USVehicleFactory()

europe_car = europe_factory.create_car("Volkswagen", "Golf")
print(europe_car.start_engine())

us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
print(us_motorcycle.start_engine())