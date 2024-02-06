from typing import Protocol
import os

class Shape(Protocol):
    def calculate_area(self) -> float:
        ...

    def display_info(self) -> None:
        ...

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        return 3.14 * self.radius * self.radius
    
    def display_info(self) -> None:
        print(f"Circle with radius {self.radius}")

class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width
    
    def calculate_area(self) -> float:
        return self.length * self.width
    
    def display_info(self) -> None:
        print(f"Rectangle with length {self.length} and width {self.width}")

def main():
    circle_instance = Circle(5)
    rectangle_instance = Rectangle(4, 6)

    print(f"Area of Circle: {circle_instance.calculate_area()}")
    circle_instance.display_info()

    print(f"\nArea of Rectangle: {rectangle_instance.calculate_area()}")
    rectangle_instance.display_info()

if __name__ == "__main__":
    main()