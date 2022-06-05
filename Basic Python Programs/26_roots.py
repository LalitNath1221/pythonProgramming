from math import sqrt
import math


a = int(input("Enter the cofficient of x^2 : "))
b = int(input("Enter the cofficient of x : "))
c = int(input("Enter the constant : "))
d = (b*b)-(4*a*c)

if(d<0):
    print(f'rootes are : {-b/(2*a)} + i{math.sqrt(-d)/(2*a)}, {-b/(2*a)} - i{math.sqrt(-d)/(2*a)}')
elif d>0:
    root1 = (-b + math.sqrt(d))/(2*a)
    root2 = (-b - math.sqrt(d))/(2*a)
    print(f'rootes are : {root1}, {root2}')

else:
    print(f'rootes are : {-b/(2*a)}')


