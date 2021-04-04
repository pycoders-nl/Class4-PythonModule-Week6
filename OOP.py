from math import sqrt


class Triangle:
    def __init__(self, height, base, side2, side3):
        self.height = height
        self.base = base
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return self.height * self.base * 0.5

    def perimeter(self):
        return self.base + self.side2 + self.side3


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return self.width + self.length


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(width=length, length=length)


# square = Square(5)
# print(square.area())
# print(square.perimeter())


class Cube(Square):
    def surface_area(self):
        return self.area() * 6

    def volume(self):
        return self.length ** 3


cube = Cube(5)
print(cube.surface_area())


class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

    def volume(self):
        base_area = super().area()
        height = sqrt(self.slant_height ** 2 - (self.base / 2) ** 2)
        return (base_area * height) / 3


pyramid = RightPyramid(2, 4)

print(pyramid.area())
print(pyramid.volume())
