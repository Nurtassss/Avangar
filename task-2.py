from math import pi

class Circle:
    def __init__(self, radius): self.radius = radius

    def area(self):
        return pi *self.raduis ** 2

    def perimeter(self):
        return 2 *pi* self.radius

def print_shape_info(shape):
    print("Area={},perimetr = {}.".format(shape.area()))

square = Square(10)
#Area = 100, perimetr=40
print_shape_info(square)circle
Circle(10)
#Area = 314.1592653589793,perimetr=62.83185307179586
print_shape_info(circle)