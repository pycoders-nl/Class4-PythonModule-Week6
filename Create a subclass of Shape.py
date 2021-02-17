"""
Create a class named Triangle and Rectangle.
Create a subclass named Square inherited from Rectangle.
Create a subclass named Cube inherited from Square.
Create a subclass named Pyramid multiple inherited both from Triangle and Square.

Two dimensional classes (Triangle, Rectangle and Square) should have:
* its dimensions as attributes.(can be inherited from a superclass)
* methods which calculate its area and perimeter separately.

Three dimensional classes (Cube and Pyramid) should have:
* its dimensions as attributes which are inherited from a superclass
* its extra dimensions if there is. (hint: maybe for Pyramid)
methods which calculate its volume and surface area separately. (surface area is optional, you may not do this)
"""

'''
class Shape():
    def _init_(self,a,b,c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
a= input("a=")
b= input("b=")
c= input("c=")'''


class Triangle():
    def __init__(self, a=0, b=0, c=0):
        self.a = float(input("ucgenin a kenar uzunlugunu giriniz="))
        self.b = float(input("ucgenin b kenar uzunlugunu giriniz="))
        self.c = float(input("ucgenin c kenar uzunlugunu giriniz="))

    def get_area(self):
        # ucgen alanini hesaplar
        s = (self.a + self.b + self.c) / 2
        return (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5

    def get_perimeter(self):
        # ucgen cevresini hesaplar
        return self.a + self.b + self.c

    def __str__(self):
        print(  "ucgenin alani   : {} m2 \n"
                "ucgenin cevresi : {} m"
                .format(self.get_area(), self.get_perimeter()))


class Rectangle():
    def __init__(self, a=0, b=0):
        self.a = float(input("dikdortgenin a kenar uzunlugunu giriniz="))
        self.b = float(input("dikdortgenin b kenar uzunlugunu giriniz="))

    def get_area(self):
        # dikdortgenin alanini hesaplar
        return self.a*self.b

    def get_perimeter(self):
        # dikdortgenin cevresini hesaplar
        return (self.a + self.b)*2

    def __str__(self):
        print(  "dikdortgenin alani   : {} m2 \n"
                "dikdortgenin cevresi : {} m"
                .format(self.get_area(), self.get_perimeter()))


class Square(Rectangle):

    def __init__(self,a=0):
        self.a = float(input("karenin kenar uzunlugunu giriniz="))
        self.b = self.a

    def __str__(self):
        print("karenin alani   : {} m2 \n"
              "karenin cevresi : {} m"
              .format(self.get_area(), self.get_perimeter()))


class Cube(Square):
    def __init__(self,a=0):
        self.a = float(input("kupun kenar uzunlugunu giriniz="))
        self.b = self.a

    def get_volume(self):
        # kupun hacmini hesaplar
        return self.a**3

    def __str__(self):
        print("kupun hacmi   : {} m3 \n"
              "kupun alani   : {} m2 \n"
              "kupun cevresi : {} m"
              .format(self.get_volume(), 6*self.get_area(), 3*self.get_perimeter()))


class Pyramid (Square,Triangle):
    def __init__(self,a=0,pyramid_height=0):
        self.a = float(input("Kere Piramidin kenar uzunlugunu giriniz="))
        self.pyramid_height = float(input("Kare Piramidin yuksekligini giriniz="))
        self.b = self.a
        self.c = self.a

    def get_volume(self):
        # Piramidin hacmini hesaplar
        return self.a**2*self.pyramid_height/3

    def __str__(self):
        print("Piramidin hacmi   : {} m3 \n"
              "Piramidin alani   : {} m2 \n"
              "Piramidin cevresi : {} m"
              .format(self.get_volume(), self.get_area(), self.get_perimeter()))


#t = Triangle()
#t.__str__()
#d = Rectangle()
#d.__str__()
#k = Square()
#k.__str__()
#kk = Cube()
#kk.__str__()
p = Pyramid()
p.__str__()