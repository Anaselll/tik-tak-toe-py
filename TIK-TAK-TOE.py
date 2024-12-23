from abc import *

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,r,pi=3.14):
        self.r = r
        self.pi = pi
    def area(self):
        S = self.r * self.r * self.pi 
        return S
class Rectangle(Shape):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def area(self):
        S = self.a * self.b
        return S
class Triangle(Shape):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def area(self):
        S = 0.5 * self.a * self.b
        return S
    
circle = Circle(2)
print(circle.area())

rectangle = Rectangle(3,4)
print(rectangle.area())

triangle = Triangle(6,2)
print(triangle.area())