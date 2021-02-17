class Triangle:
    def __init__(self, x ,y ,z):
        self.x = x
        self.y = y
        self.z = z
    
    def calc_area(self):
        #   heron
        s = (self.calc_perimeter)/2
        area = (s*(s-self.x)*(s-self.y)*(s-self.z)) ** 0.5
        return area

    def calc_perimeter(self):
        return self.x + self.y + self.z

################################################

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc_area(self):
        return self.x * self.y

    def calc_perimeter(self):
        return self.x * 2 + self.y * 2 

#################################################

class Square(Rectangle):
    def __init__(self, x):
        super().__init__(x, x)
        
#################################################

class Cube(Square):
    def __init__(self, x):
        super().__init__(x)

    def calc_volume(self):
        return super().calc_area() * self.x

    def calc_surface(self):
        return super().calc_area() * 6
    
#################################################

class Pyramid(Triangle,Square):
    def __init__(self, x, y, z, h):
        #   heron yapmaya usendim
        self.h = h
        Triangle.__init__(self, x, y, z)
        Square.__init__(self, x)

    def calc_volume(self):
        return Square.calc_area(self) * self.h * 1/3

    def calc_surface(self):
        return Triangle.calc_area(self) * 4 + Square.calc_area()
    
#################################################

a = Pyramid(5, 10 ,10 ,5)
print(a.calc_volume())