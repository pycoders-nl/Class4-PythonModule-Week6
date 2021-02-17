class Triangle:
    def __init__(self,x,y,h):
        self.x=x
        self.y=y
        self.h=h

    def ucgenin_cevresi(self):
        return self.x+self.y+self.h
    def ucgenin_alani(self):
        return self.x*self.h*0.5

Triangle_New=Triangle(3,4,5)
print ("Ucgenin_Cevresi :", Triangle_New.ucgenin_cevresi())
print ("Ucgenin_Alani   :", Triangle_New.ucgenin_alani())

class Rectangle:
    def __init__(self,k_a,u_b):
        self.k_a=k_a
        self.u_b=u_b

    def dikdortgenin_cevresi(self):
        return 2*(self.k_a+self.u_b)

    def dikdortgenin_alani(self):
        return self.k_a*self.u_b

Rectangle_New=Rectangle(3,4)
print ("Dikdortgenin_Cevresi :", Rectangle_New.dikdortgenin_cevresi())
print ("Dikdortgenin_Alani   :", Rectangle_New.dikdortgenin_alani())


class Square(Rectangle):
    def __init__(self,k_a):
        super().__init__(k_a,k_a)

    def karenin_cevresi(self):
        return 4*self.k_a

    def karenin_alani(self):
        return self.k_a*self.k_a

Square_New=Square(3)
print ("Karenin_Cevresi :", Square_New.karenin_cevresi())
print ("Karenin_Alani   :", Square_New.karenin_alani())

class Cube(Square):
    def __init__(self,k_a):
        super().__init__(k_a)

    def kupun_alani(self):
        return 6*(self.k_a**2)

    def kupun_hacmi(self):
        return self.k_a*self.k_a*self.k_a

Cube_New=Cube(4)
print ("Kupun Hacmi   :", Cube_New.kupun_hacmi())
print ("Kupun Alani   :", Cube_New.kupun_alani())

class Pyramid(Square,Triangle):
    def __init__(self,k_a,h):
        self.k_a=k_a
        self.h=h

    def Pyramidin_Hacmi(self):
        return (self.k_a**2)*self.h*1/3
Pyramid_New=Pyramid(3,4)

print("Pyramidin_Hacmi:",Pyramid_New.Pyramidin_Hacmi())















