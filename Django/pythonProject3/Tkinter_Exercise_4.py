# In object-oriented-based Python programming, CC means the same function name is being used for different
# types. Each function is differentiated based on its data type and number of arguments. So, each function has a
# different signature. In simple words, we can define polymorphism as the ability of a message to be displayed in
# more than one form. Real life example of polymorphism, a person at the same time can have different characteristic.
# Like a man at the same time is a father, a husband, an employee. Polymorphism is used in OOP to allow developers to
# write more efficient code and redefine methods for derived classes; however, it could raise real-time performance
# issues.

# Polymorphism with an Example

class Shape:
    def Area(self):
        pass


class Rectangle(Shape):
    def __init__(self, Width, Height):
        self.Width = Width
        self.Height = Height

    def Area(self):
        return self.Width * self.Height


class Triangle(Shape):
    def __init__(self, Base, Height):
        self.Base = Base
        self.Height = Height

    def Area(self):
        return 0.5 * self.Base * self.Height


rectangle = Rectangle(10, 5)
triangle = Triangle(6, 4)

print("Area of Rectangle = ", rectangle.Area())
print("Area of Triangle = ", triangle.Area())
