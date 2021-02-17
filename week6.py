# Create a class named Triangle and Rectangle.

# Create a subclass named Square inherited from Rectangle.

# Create a subclass named Cube inherited from Square.

# Create a subclass named Pyramid multiple inherited both from Triangle and Square.

# Two dimensional classes (Triangle, Rectangle and Square) should have:
# its dimensions as attributes.(can be inherited from a superclass)
# methods which calculate its area and perimeter separately.

# Three dimensional classes (Cube and Pyramid) should have:
# its dimensions as attributes which are inherited from a superclass
# its extra dimensions if there is. (hint: maybe for Pyramid)
# methods which calculate its volume and surface area separately. (surface area is optional, you may not do this)

class Triangle:
    def __init__(self, a, b):
        self.yukseklik = a
        self.taban = b

    def alanHesaplama(self):
        alan = (self.yukseklik*self.taban) / 2
        return alan

    def cevreHesaplama(self):
        uzunKenar = (self.yukseklik**2 + self.taban**2)**(1/2)
        cevre = self.yukseklik + self.taban + uzunKenar
        return cevre


class Rectangle:
    def __init__(self, a, b):
        self.uzunKenar = a
        self.kisaKenar = b

    def alanHesaplama(self):
        alan = self.uzunKenar * self.kisaKenar
        return alan

    def cevreHesaplama(self):
        cevre = (self.uzunKenar + self.kisaKenar)*2
        return cevre


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


class Cube(Square):
    def __init__(self, a):
        super().__init__(a)

    def kupAlanHesaplama(self):
        alan = super().alanHesaplama()
        return alan * 6

    def kupHacimHesaplama(self):
        hacim = super().alanHesaplama() * self.uzunKenar
        return hacim


class Pyramid (Square, Triangle):
    def __init__(self, a, h):
        self.piramitYukseklik = h
        ucgenYukseklik = (h**2 + ((a/2)**2))**1/2
        Square.__init__(self, a)
        Triangle.__init__(self, ucgenYukseklik, a)

    def piramitAlanHesaplama(self):
        tabanAlani = Square.alanHesaplama(self)
        ucgenAlani = Triangle.alanHesaplama(self)
        toplamAlan = tabanAlani + (ucgenAlani * 4)
        return toplamAlan

    def piramitHacimHesaplama(self):
        piramitHacim = Square.alanHesaplama(self) * \
            self.piramitYukseklik / 3
        return piramitHacim


ucgen = Triangle(5, 8)
ucgenAlan = ucgen.alanHesaplama()
ucgenCevre = ucgen.cevreHesaplama()
print(ucgenAlan, ucgenCevre)

dikdortgen = Rectangle(10, 20)
dikdortgenAlan = dikdortgen.alanHesaplama()
dikdortgenCevre = dikdortgen.cevreHesaplama()
print(dikdortgenAlan, dikdortgenCevre)

kare = Square(15)
kareAlan = kare.alanHesaplama()
kareCevre = kare.cevreHesaplama()
print(kareAlan, kareCevre)

kup = Cube(20)
kupAlan = kup.kupAlanHesaplama()
kupHacim = kup.kupHacimHesaplama()
print(kupAlan, kupHacim)

piramit = Pyramid(10, 15)
piramitAlan = piramit.piramitAlanHesaplama()
piramitHacim = piramit.piramitHacimHesaplama()
print(piramitAlan, piramitHacim)
