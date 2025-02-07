# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic sound"

# Child Class (Inherits from Animal)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor
        self.breed = breed

    def speak(self):
        return "Woof!"

# Create an instance of Dog
dog = Dog("Buddy", "Golden Retriever")

print(f"Name: {dog.name}")  # Output: Name: Buddy
print(f"Breed: {dog.breed}")  # Output: Breed: Golden Retriever
print(f"Sound: {dog.speak()}")  # Output: Sound: Woof!

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Create objects
rect = Rectangle(5, 10)
circle = Circle(7)

print("Rectangle Area:", rect.area())  # Output: 50
print("Circle Area:", circle.area())   # Output: 153.86