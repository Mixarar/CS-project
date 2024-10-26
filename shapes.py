from math import pi, sqrt

class Shape():
    def __init__(self):
        self.area_value = 0

    def calculate_area(self):
        self.area_value = self.area()
        return self.area_value
    
    def area(self):
        raise NotImplementedError("Not implemented!")
    
class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self):
        return round(self.side ** 2, 1)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return round(pi * self.radius ** 2, 1)

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def area(self):
        return round(0.5 * self.base * self.height, 1)

class Hexagon(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self):
        return round((3 * sqrt(3) * self.side ** 2) / 2, 1)

shapes = [
    Square(4),
    Circle(3),
    Triangle(4, 5),
    Hexagon(2)
]

for shape in shapes:
    print(f"The area of the {shape.__class__.__name__} is {shape.calculate_area()}")