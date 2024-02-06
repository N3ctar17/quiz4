from abc import ABC , abstractmethod
import os

class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass
    
    @abstractmethod
    def display_info(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius
    
    def display_info(self):
        print(f"Circle with radius {self.radius}")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
    
    def display_info(self):
        print(f"Rectangle with length {self.length} and width {self.width}")
        

def main():
    circle_instance = Circle(5)
    rectangle_instance = Rectangle(4, 6)

    print(f"Area of Circle: {circle_instance.calculate_area()}")
    circle_instance.display_info()

    print(f"\nArea of Rectangle: {rectangle_instance.calculate_area()}")
    rectangle_instance.display_info()

if __name__=="__main__":
    main()