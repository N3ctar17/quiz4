class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    
    @property
    def diameter(self):
        return self._radius * 2
    
    @property
    def area(self):
        return 3.14 * self._radius**2
    
def main():
    my_circle = Circle(radius=5)

    print(f"Radius: {my_circle.radius}")
    print(f"Diameter: {my_circle.diameter}")
    print(f"Area: {my_circle.area:.2f}")

if __name__ == "__main__":
    main()