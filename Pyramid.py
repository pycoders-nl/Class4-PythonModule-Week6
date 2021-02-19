'''
Create a class named Triangle and Rectangle.
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

Author= Bulent Caliskan  Date= 15/02/2021
'''
print("-"*80)
print("-"*80)
print(str("-") *30 +"GEOMETRIC CALCULATIONS "+ str("-")*27)
print("-"*80)
print("-"*80)
#Triangle class ini olusturup 3 kenar uzunlugunu userdan istiyoruz.ve bunu hata ayiklamaya 
# (try-except) sokuyoruz.
class Triangle():
    def __init__(self,side_1=0,side_2=0,side_3=0):
        while True:
            try:
                self.side_1 = float(input("Please enter the length of the first side in meters? "))
                self.side_2 = float(input("Please enter the length of the second side in meters? "))
                self.side_3 = float(input("Please enter the length of the third side in meters? "))
                break           
            except ValueError:
                print("Your entry was wrong!")
                continue
    #Triangle nin area sini hesaplayip return eden functionu yaziyoruz.
    def area(self):
        s=(self.side_1+self.side_2+self.side_3)/2
        return (s*(s-self.side_1)*(s-self.side_2)*(s-self.side_3)) ** 0.5     
    
    #Triangle nin aperimeter ini hesaplayip return eden functionu yaziyoruz.
    def perimeter(self):
        return  self.side_1+self.side_2+self.side_3

    # ekrana print yapacak str functionunu yaziyoruz.
    def __str__(self):
        print (f"""
        Area of the triangle = {self.area():.8} m²
        Perimeter of the triangle = {self.perimeter():.8} m
        """)    


#Rectangle class ini olusturup 2 kenar uzunlugunu userdan istiyoruz.ve bunu hata ayiklamaya
#  (try-except) sokuyoruz.
class Rectangle:
    def __init__(self,side1=0,side2=0):
        while True:
            try:
                self.side1 = float(input("Please enter the length of the first side in meters? "))
                self.side2 = float(input("Please enter the length of the second side in meters? "))
                break           
            except ValueError:
                print("Your entry was wrong!")
                continue
    #Rectangle nin area sini hesaplayip return eden functionu yaziyoruz.
    def area(self):
        return self.side1 * self.side2
    
    #Rectangle nin aperimeter ini hesaplayip return eden functionu yaziyoruz.
    def perimeter(self):
        return 2 * (self.side1 + self.side2)
    
    # ekrana print yapacak str functionunu yaziyoruz.
    def __str__(self):
        print (f"""
        Area of the Rectangle = {self.area():.8} m²
        Perimeter of the Rectangle = {self.perimeter():.8} m
        """)    
    
#Square class ini Rectangle inherid ederek olusturuyoruz.
class Square(Rectangle):

    def __init__(self,side1=0):
        super().__init__(side1,side1)

    # Rectangle class indan inherid ettigimiz icin ordaki function lari kullaniyoruz.
    def __str__(self):
        print (f"""
        Area of the Square = {self.area():.8} m²
        Perimeter of the Square = {self.perimeter():.8} m
        """)        

#Cube class ini Square inherid ederek olusturuyoruz.
class Cube(Square):
    def __init__(self,side1=0):
        super().__init__(side1)
    
    #Cube hacmini hesaplayip donen volume functionunu hesapliyoruz.
    def volume(self):
        return self.side1**3   
    
    #Square class indan inherid ettigimiz icin ordaki function lari kullaniyoruz.
    def __str__(self):
        print (f"""
        Area of the Cube = {6 * self.area():.8} m²
        Perimeter of the Cube = {3 * self.perimeter():.8} m
        Volume of the Cube = {self.volume():.8} m³
        """)

 #Pyramid class ini Square ve Triangle inherid ederek olusturuyoruz ve bunu hata ayiklamaya
#  (try-except) sokuyoruz.   
class Pyramid (Square,Triangle):
    def __init__(self,base_lenght=0,triangle_hight=0,pyramid_height=0):
        while True:
            try:
                self.base_lenght = float(input("Please enter the length of the base in meters? "))
                self.triangle_hight = float(input("Please enter the hight of the triangle in meters? "))
                self.pyramid_height = float(input("Please enter the hieght of the pyramid in meters? "))
                break           
            except ValueError:
                print("Your entry was wrong!")
                continue
        super().__init__(self.base_lenght)
        
    # ekrana print yapacak str functionunu yaziyoruz.
    def __str__(self):
        print (f"""
        Area of the Pyramid = {0.5*super().perimeter()*self.triangle_hight+super().area():.8} m²
        Volume of the Pyramid = {((self.base_lenght*self.triangle_hight)/2)*self.pyramid_height:.8} m³
        """)      
#Ask adinda class olusturup user a secenekleri sorup ne hesaplamasini istedigini soruyoruz.
# Ve cevaba gore ilgili class a if elif kullanarak yonlendiriyoruz.
class Ask:
    def __init__(self,questions=""):
        self.questions = input('''
        What do you want to calculate ? Enter number between 1 and 5 
        
        1-Area and perimeter of the Triangle
        2-Area and perimeter of the Rectangle
        3-Area and perimeter of the Square
        4-Area ,perimeterand and volume of the Cube
        5-Area and volume of the Pyramid
        Enter your choose---------------->''')
        print()
    def run(self):
        if self.questions=="1":
            obj = Triangle()
            obj.__str__()
        elif self.questions=="2":
            obj = Rectangle()
            obj.__str__()
        elif self.questions=="3":
            obj = Square()
            obj.__str__()
        elif self.questions=="4":
            obj = Cube()
            obj.__str__()
        elif self.questions=="5":       
            obj = Pyramid()
            obj.__str__()
        else :
            self.questions = input("Your entry was wrong! Enter number between 1 and 5 \n")
            self.run()
#objemizi olusturup run() functionunu cagiriyoruz
obj = Ask()
obj.run()



