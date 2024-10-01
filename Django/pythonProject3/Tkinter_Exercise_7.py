# create a class object and insert polymorphism ,abstraction concepts with using advance concepts

class Area:
    def area(self):
        pass


class Rectangle(Area):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Area):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Circle(Area):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


rectangle = Rectangle(4, 6)
triangle = Triangle(9, 3)
circle = Circle(4)

print("Area of Rectangle = ", rectangle.area())
print("Area of Triangle = ", triangle.area())
print("Area of Circle = ", circle.area())
