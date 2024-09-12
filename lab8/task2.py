from cmath import sqrt
import re


def dist(x1,y1,x2,y2):
    d=sqrt( (x1-x2)**2 -(y1-y2**2))
    return d
def triAreaSides(a,b,c):
    s=(a+b+c)/2
    a= sqrt(s*(s-a)*(s-b)*(s-c))
    return a

def triAreaPoints(x1,y1,x2,y2,x3,y3):
    side1=dist(x1,y1,x2,y2)
    side2=dist(x2,y2,x3,y3)
    side3=dist(x3,y3,x1,y1)
    triArea=triAreaSides(side1,side2,side3)
    return triArea
    
def pentaArea(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5):
    area1=triAreaPoints(x1,y1,x2,y2,x3,y3)
    area2=triAreaPoints(x1,y1,x3,y3,x5,y5)
    area3=triAreaPoints(x5,y5,x3,y3,x4,y4)
    totalArea= area1+area2+area3
    return totalArea


x1,y1=eval(input('first points a,b  '))
x2,y2=eval(input('2nd points a,b  '))
x3,y3=eval(input('3rd points a,b  '))
x4,y4=eval(input('4th points a,b  '))
x5,y5=eval(input('5th points a,b  '))

print(f'the area of pentagone is {pentaArea(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5) } ')