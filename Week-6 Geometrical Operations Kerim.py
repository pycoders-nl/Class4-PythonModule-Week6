# At the Square class you can check if the edges same or not

class Triangle:
    def __init__(self, edge_1 = 1, edge_2 = 1 , edge_3 = 1):
        self.edge_1 = float(edge_1)
        self.edge_2 = float(edge_2)
        self.edge_3 = float(edge_3)

    def Tri_Area(self):
        semi_perimeter = (self.edge_1 + self.edge_2 + self.edge_3) / 2
        area_triangle = (semi_perimeter*(semi_perimeter - self.edge_1)*(semi_perimeter - self.edge_2)*(semi_perimeter - self.edge_3)) ** 0.5
        return area_triangle

    def Perimeter(self):
        return self.edge_1 + self.edge_2 + self.edge_3

    def __str__(self):
        return f"The Area of this Triangle is: {self.Tri_Area()}  The Perimeter of this Triangle is: {self.Perimeter()}"

class Rectangle:
    def __init__(self, edge_1, edge_2):
        self.edge_1 = float(edge_1)
        self.edge_2 = float(edge_2)
    
    def Area(self):
        return self.edge_1 * self.edge_2

    def Perimeter(self):
        return 2 * (self.edge_1 + self.edge_2)

    def __str__(self):
        return f"The Area of this Rectangle is: {self.Area()}  The Perimeter of this Rectangle is: {self.Perimeter()}"

class Square(Rectangle):

    def __init__(self, edge_1):
        super().__init__(edge_1, edge_2 = edge_1)

    def Area(self):
        return super().Area()
    
    def Perimeter(self):
        return super().Perimeter()

    def __str__(self):
        return f"The Area of this Square is: {super().Area()}  The Perimeter of this Square is: {super().Perimeter()}"


class Cube(Square):

    def Volume(self):
        return self.edge_1 ** 3

    def Surface(self):
        return 6 * super().Area()

    def __str__(self):
        return f"The Volume of this Cube is: {self.Volume()}  The Surface of this Cube is: {self.Surface()}"


class Pyramid(Square, Triangle):
    def __init__(self, edge_base,triangle_height, pyramid_height):        
        super().__init__(edge_1=edge_base)
        self.triangle_height = triangle_height
        self.pyramid_height = pyramid_height

    def Volume(self):
        return (super().Area()*self.pyramid_height)/3

    # def Surface(self):
    #     return super().Area() + 4*super().Tri_Area()

    def __str__(self):
        return f"The Volume of this Pyramid is: {self.Volume()}"



triangle_1 = Triangle(3,4,5)
print(triangle_1)

rec1 = Rectangle(5,10)
print(rec1)

square1 = Square(8)
print(square1)

cube1 = Cube(8)
print(cube1)

pyramid1 = Pyramid(5,10,10)
print(pyramid1)



