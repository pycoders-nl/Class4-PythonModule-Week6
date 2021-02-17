

# Create a class named Triangle and Rectangle.
# 
# Create a subclass named Square inherited from Rectangle.
# 
# Create a subclass named Cube inherited from Square.
# 
# Create a subclass named Pyramid multiple inherited both from Triangle and Square.
# 
# Two dimensional classes (Triangle, Rectangle and Square) should have:
# 
# its dimensions as attributes.(can be inherited from a superclass)
# methods which calculate its area and perimeter separately. Three dimensional classes (Cube and Pyramid) should have:
# its dimensions as attributes which are inherited from a superclass
# its extra dimensions if there is. (hint: maybe for Pyramid)
# methods which calculate its volume and surface area separately. (surface area is optional, you may not do this)

# In[17]:


# Çeşitkenar Üçgenin Alanı Nasıl Hesaplanır? 
# a, b ve c üçgenin kenar uzunlukları ve s üçgenin çevre uzunluğunun yarısı olmak üzere;
# Alan = √(s(s-a)(s-b)(s-c))


def star_triangle(n):
    for i in range(n):
        print(" "*(n-1-i), end="")
        print("*"*((i*2)+1))
star_triangle(28)


class Triangle():
    
    def __init__(self,a,b,c):
        self.a=int(a)
        self.b=int(b)
        self.c=int(c)
        
    def area(self):
        s=(self.a+self.b+self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**(0.5)
    
    def perimeter(self):
        return (self.a+self.b+self.c)

    
class Rectangle():
    def __init__(self,d,e):
        self.d=d
        self.e=e
        
    def perimeter(self):
        return 2*(self.d+self.e)
    
    def area(self):
        return self.d*self.e
    
    
class Square(Rectangle):
    
    def __init__(self,d):
        super().__init__(d,d)
        self.d=d
        
    def perimeter(self):
        return 4*(self.d)
    
    def area(self):
        return (self.d)**2
    
    
class Cube (Square):
    
    def __init__(self,d):
        super().__init__(d)
        
    def cube_area(self):
        return 6*(self.d**2)
    
    def volume(self):
        return (self.d)**3
    

class Pyramid(Triangle, Square):
    def __init__(self,d,a,c):
        super().__init__(d,a,c)
        self.d=d
        self.a=a    
    
    def volume(self):
        return ((1/3)*(self.d**2)*( (self.a**2-(self.d**2)/2)**0.5 ))
    
    
triangle1 = Triangle(6,8,10)
print('\n\t The area of the triangle is: {}' .format(triangle1.area()))
print('\t The perimeter of the triangle is: {}' .format(triangle1.perimeter()))

rectangle1 = Rectangle(5,10)
print('\n\t The perimeter of the rectangle is: {}' .format(rectangle1.perimeter()))
print('\t The area of the rectangle is: {}' .format(rectangle1.area()))

square1 = Square(rectangle1.d)
print('\n\t The area of the square is: {}' .format(square1.area()))
print('\t The perimeter of the square is: {}' .format(square1.perimeter()))
      
cube1 = Cube(square1.d)
print('\n\t The area of the cube is: {}' .format(cube1.cube_area()))
print('\t The volume of the cube is: {}' .format(cube1.volume()))

pyramid1 = Pyramid(square1.d, triangle1.a, triangle1.c)
print('\n\t The volume of the pyramid is: {}' .format(int(pyramid1.volume())))
