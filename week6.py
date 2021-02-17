class Triangle():
    def __init__(self,a,b,c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)

    def perimeter(self):
        return (self.a+self.b+self.c)   # Cevre = a+b+c

    def area(self):
        s = (self.a + self.b + self.c)/2    # Cevrenin yarisi = s 
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5    # Alan = karekok icinde s*(s-a)*(s-b)*(s-c)
    

class Rectangle():
    def __init__(self,d,e):
        self.d = d
        self.e = e
    
    def perimeter(self):
        return 2*(self.d + self.e)      #Dikdortgen cevresi = 2*(d+e)

    def area(self):
        return self.d * self.e          #Dikdortgen alani = d * e


class Square(Rectangle):
    def __init__(self,d):
        super().__init__(d,d)
        self.d = d

    def perimeter(self):
        return 4*(self.d)           # Karenin cevresi = 4 * d

    def area(self):
        return (self.d)**2          # Karenin alani = d ** 2

class Cube(Square):
    def __init__(self, d):
        super().__init__(d)
    
    def cube_area(self):
        return 6*(self.d ** 2)      # Kupun yuzey alani = 6 *(d **2)

    def volume(self):
        return (self.d)**3          # Kupun hacmi = d * d * d

class Pyramid(Triangle, Square):
    def __init__(self, d, a, c):
        super().__init__(d, a, c)    
        self.d = d
        self.a = a
    
    def volume(self):
        return ((self.d**2)*((self.a**2-(self.d**2)/2)**0.5)*(1/3))

triangle1 = Triangle(3,4,5)
print(f'The area of the triangle is: {triangle1.area()}')
print(f'The perimeter of the triangle is : {triangle1.perimeter()}')

rectangle1 = Rectangle(4,8)
print(f'The area of the rectangle is: {rectangle1.area()}')
print(f'The perimeter of the rectangle is : {rectangle1.perimeter()}')

square1 = Square(rectangle1.d)
print(f'The area of the square is: {square1.area()}')
print(f'The perimeter of the square is : {square1.perimeter()}')

cube1 = Cube(square1.d)
print(f'The area of the square is: {cube1.cube_area()}')
print(f'The volume of the square is : {cube1.volume()}')

pyramid1 = Pyramid(square1.d, triangle1.a, triangle1.c)
print(f'The volume of the pyramid is: {int(pyramid1.volume())}')