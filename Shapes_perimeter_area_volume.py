class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return self.a + self.b + self.c

    def get_area(self):
        return 1 / 4 * ((2 * self.a * self.b) ** 2 - (self.a ** 2 + self.b ** 2 - self.c ** 2) ** 2) ** 0.5


class Rectangle:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_perimeter(self):
        return 2 * (self.x + self.y)

    def get_area(self):
        return self.x * self.y


class Square(Rectangle):

    def __init__(self, x):
        super(Square, self).__init__(x, x)


class Cube(Square):

    def __init__(self, a):
        super(Cube, self).__init__(a)

    def get_volume(self):
        return self.x ** 3

    def get_area(self):
        return 6 * self.x ** 2


class Pyramid:
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def get_volume(self):
        return self.a ** 2 * self.h / 3


triangle_1 = Triangle(3, 4, 5)
print("Triangle perimeter: " + str(triangle_1.get_perimeter()))
print("Triangle area: " + str(triangle_1.get_area()))

rectangle_1 = Rectangle(6, 7)
print("Rectangle perimeter: " + str(rectangle_1.get_perimeter()))
print("Rectangle area: " + str(rectangle_1.get_area()))

square_1 = Square(5)
print("Square perimeter: " + str(square_1.get_perimeter()))
print("Square area: " + str(square_1.get_area()))

cube_1 = Cube(2)
print("Cube volume: " + str(cube_1.get_volume()))
print("Cube area: " + str(cube_1.get_area()))

#Kare tabanin 1 kenari parametre1 piramidin yuksekligi parametre2
pyramid_1 = Pyramid(3, 4)
print("Pyramid volume" + str(pyramid_1.get_volume()))
