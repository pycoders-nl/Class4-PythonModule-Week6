# Create a class named Triangle and Rectangle.
# Create a subclass named Square inherited from Rectangle.
# Create a subclass named Cube inherited from Square.
# Create a subclass named Pyramid multiple inherited both from Triangle and Square.
#
# Two dimensional classes (Triangle, Rectangle and Square) should have:
#     its dimensions as attributes.(can be inherited from a superclass)
#     methods which calculate its area and perimeter separately.
#     Three dimensional classes (Cube and Pyramid) should have:
#     its dimensions as attributes which are inherited from a superclass
#     its extra dimensions if there is. (hint: maybe for Pyramid)
#     methods which calculate its volume and surface area separately.


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def tri_perimeter(self):            # considered as equilateral triangle
        return self.base * 3

    def tri_area(self):
        return (self.base * self.height) / 2



a = int(input("Enter the base of equilateral triangle: "))
b = int(input("Enter the height of equilateral triangle: "))

tri1 = Triangle(a, b)
print("--- Equilateral Triangle ---")
print("Perimeter is: ", tri1.tri_perimeter())
print("Area is: ", tri1.tri_area())


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rec_area(self):
        return self.length * self.width

    def rec_perimeter(self):
        return (self.length + self.width) * 2


a = int(input("\nEnter the length of Rectangular: "))
b = int(input("Enter the width of Rectangular: "))
rect1 = Rectangle(a, b)

print("\n--- Rectangular ---")
print("Perimeter is: ", rect1.rec_perimeter())
print("Area is: ", rect1.rec_area())


class Square(Rectangle):

    def __init__(self, length):
        super().__init__(length, length)

    def perimeter(self):
        return self.length * 4

    def sq_area(self):
        return self.length ** 2


side = int(input("\nEnter the one side of Square: "))
squ1 = Square(side)

print("\n--- Square ---")
print("Perimeter is: ", squ1.perimeter())
print("Area is: ", squ1.sq_area())


class Cube(Square):

    def __init__(self, length):
        super().__init__(length)


a = int(input("\nEnter the length of one side of Cube: "))
cube1 = Cube(side)

print("\n--- Cube ---")
print("Cube Area:", cube1.sq_area() * 6)
print("Cube Volume :", cube1.sq_area() * a)


class Pyramid(Square, Triangle):
    def __init__(self, base, tri_height, height):
        self.base = base
        self.tri_height = tri_height
        self.height = height
        super().__init__(self.base)

    def area(self):
        base_area = super().sq_area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area

    def volume(self):
        base_area = super().sq_area()
        return (base_area * self.height) / 3


a = int(input("\nEnter the length of base of square Pyramid: "))
b = int(input("Enter the height of triangles: "))
c = int(input("Enter the height of square Pyramid: "))

pyr1 = Pyramid(a, b, c)
print("--- Square base Pyramid ---")
print("Pyramid Area: ", pyr1.area())
print("Pyramid Volume: ", pyr1.volume())

