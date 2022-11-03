import math
from msilib.schema import Binary
from shutil import SameFileError
from enum import Enum

class Circle():
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

class Result(Enum):
    Same = 1
    B_in_A = 2
    A_in_B = 3
    Intersect = 4
    Touch = 5
    No_Touch = 6
    
c1 = Circle(-10, 8, 30)    
c2 = Circle(14, -24, 10)
c3 = Circle(-10, 8, 30) 
c4 = Circle(8, 8, 8) 
c5 = Circle(4, 3, 6)
c6 = Circle(-4, 3, 6)

def circle(c1, c2):
    d = math.sqrt((c1.x - c2.x)**2 + (c1.y - c2.y)**2)
    
    #Проверка дали стойностите на двете окръжности са еднакви
    if(c1.__dict__ == c2.__dict__):
        print ("Circles are the same")
        return Result.Same.value
    elif(d <= c1.radius - c2.radius):
        print("Circle B is inside A")
        return Result.B_in_A.value
    elif(d <= c2.radius - c1.radius):
        print("Circle A is inside B")
        return Result.A_in_B.value
    elif(d < c1.radius + c2.radius):
        print("Circle intersect each other")
        return Result.Intersect.value
    elif(d == c1.radius + c2.radius):
        print("Circle touch each other")
        return Result.Touch.value
    else:
        print("Circle don't touch each other")
        return Result.No_Touch.value

circle(c1,c3)
circle(c5,c1)
circle(c1,c4)
circle(c5,c6)
circle(c1,c2)
circle(c2,c4)

def test_circles_are_same():
    assert circle(c1,c3) == Result.Same.value

def test_A_inside_B():
    assert circle(c5,c1) == Result.A_in_B.value

def test_B_inside_A():
    assert circle(c1,c4) == Result.B_in_A.value

def test_circles_intersect():
    assert circle(c5,c6) == Result.Intersect.value

def test_cicles_touch():
    assert circle(c1,c2) == Result.Touch.value

def test_circles_dont_touch():
    assert circle(c2,c4) == Result.No_Touch.value