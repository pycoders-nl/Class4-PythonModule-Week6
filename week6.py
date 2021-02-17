class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        Perimeter = a + b + c
        s = (a + b + c) / 2
        Area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

        print("\n The Perimeter of Traiangle = %.2f" % Perimeter);
        print(" The Area of a Triangle is %0.2f" % Area)




class Rectangle:
    def __init__(self,s,height ):

        self.width=s
        self.height=height
        Area2 = s * height
        Perimeter = 2 * (s + height)

        print("\n Area of a Rectangle is: %.2f" % Area2)
        print(" Perimeter of Rectangle is: %.2f" % Perimeter)

        super().__init__()


class Square(Rectangle):
      def __init__(self,s):
        super().__init__(s,s)

        area = s * s
        perimeter = 4 * s

        print("Area of Square : ", area)
        print("Perimeter of Square : ", perimeter)




class Cube(Square):
    def __init__(self,s):
        super().__init__(s)

        sa = 6 * (s * s)
        Volume = s * s * s
        LSA = 4 * (s * s)

        print("\n Surface Area of Cube = %.2f" % sa)
        print(" Volume of cube = %.2f" % Volume)
        print(" Lateral Surface Area of Cube = %.2f" % LSA)

class Pyramid(Triangle, Square):
    def __init__(self,b,c):
        super().__init__(b,b,c)
        volume = (0.33) * b * b * c
        area=2 * b * c + pow(b, 2)
        print(" Volume of pyramid = %.2f" % volume)
        print(" Area of pyramid = %.2f" % area)


"""print(Triangle(5,6,7))"""
"""print(Rectangle(6,7))"""
"""print(Square())"""
print(Cube(5))
print(Pyramid(6,4))
