class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

# Create an object
my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()  # Output: Car: 2020 Toyota Corolla

class Vehicle:
    def drive(self):
        return "Generic vehicle driving."

class Car(Vehicle):
    def drive(self):
        return "Car is driving on the road."

class Bike(Vehicle):
    def drive(self):
        return "Bike is cycling on the path."

# Function demonstrating polymorphism
def start_driving(vehicle):
    print(vehicle.drive())

# Create objects
my_car = Car()
my_bike = Bike()

# Call the function with different objects
start_driving(my_car)   # Output: Car is driving on the road.
start_driving(my_bike)  # Output: Bike is cycling on the path.