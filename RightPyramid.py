
"""Create a class named Triangle and Rectangle.
Create a subclass named Square inherited from Rectangle.
Create a subclass named Cube inherited from Square.
Create a subclass named Pyramid multiple inherited both from Triangle and Square.
Two dimensional classes (Triangle, Rectangle and Square) should have:
its dimensions as attributes.(can be inherited from a superclass)
methods which calculate its area and perimeter separately.
Three dimensional classes (Cube and Pyramid) should have:
its dimensions as attributes which are inherited from a superclass
its extra dimensions if there is. (hint: maybe for Pyramid)
methods which calculate its volume and surface area separately.
(surface area is optional, you may not do this)"""

# Mostly inspired from the example in the Gitbook additional reading, it is a hint as well,

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

rectangle = Rectangle(4,6)
print ("dikdortgen alan :", rectangle.area())
print ("dikdortgen cevre :",rectangle.perimeter())

class Square(Rectangle):   # kare dikdortgenin alt sinifi, ozellikleri ondan aliyor
    def __init__(self, length):
        super().__init__(length, length) # kare kenar uzunluklari ayni oldugu icin, ust sinifta olan width, length olarak degistiyoruz
                                         # boylece kara icin 2 ayri kenar bilgisi gerek kalmadi
    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length

square = Square(6)
print ("kare alan :", square.area())
print ("kare cevre :", square.perimeter())

class Cube(Square):  # kup'te karenin alt sinifi oluyor

    def __init__(self, length):   #bunu hic yazmasak da olur,
        super().__init__(length)

    def surface_area(self):
        face_area = self.length * self.length
        return face_area * 6

    def volume(self):
        return  self.length * self.length * self.length

cube1 = Cube(5)
print ("kup alan :", cube1.surface_area())
print ("kup hacim :", cube1.volume())


class Triangle:   #eskenar ucgen olarak versaydim, cevre hesaplamasi kolay olsun diye
    def __init__(self, base, tri_height):
        self.base = base
        self.tri_height = tri_height

    def tri_area(self):
        return 0.5 * self.base * self.tri_height

    def perimeter(self):
        return 3 * self.base

triangle1 = Triangle(4,5)
print ("ucgen alan :", triangle1.tri_area())
print ("ucgen cevre :", triangle1.perimeter())

class RightPyramid(Square, Triangle):   #karepiramit,   # boylece base, hem karenin kenar verisi oldu, hem de ucgenin tabani
    def __init__(self, base, tri_height, height):  #tri_height yan alandaki ucgen yuksekligi, slant_height diye bilinir
        super().__init__(length=base)  #kare sinifindaki length verisi icin base verisini kullanmasini istiyorum, onun yerine geciyor,
                                        # boylece base, hem karenin kenar verisi oldu, hem de ucgenin tabani
        self.base = base               # yoksa hem ucgen hem de kare icin kenar verileri icin ayri ayri veri girmemiz gerekiyor
        self.tri_height = tri_height   #tri_height, piramitin yuksekligi degil, yan yuzey ucgen yuksekligi
        self.height= height            #height, piramitin dikey yuksekligi, hacim hesaplama icin gerekli

    def area(self):
        base_area = super().area()              #taban alani hesaplamayi kare ust sinifindan aliyor
        triangle_area = super().tri_area()      #  yan alan hesaplamayi ucgen ust sinifindan aliyor
        return (triangle_area * 4 + base_area)  # tum alan

    def volume(self):
        base_area = super().area()     
        return base_area*self.height*(1/3)  # taban alani * yukseklik* 1/3

pyramid1 = RightPyramid(6, 4, 5)  #taban kenar 6, yan ucgen yukseklik 5, piramit yukseklik 5
print ("piramit alan :", pyramid1.area())
print ("piramit hacim :", pyramid1.volume())