import math
from sympy import*

H = float(input("Enter the length of beam:"))
M = float(input("Enter the Bending moment applied on beam:"))
E = float(input("Enter the Youngs modulus of beam:"))
I = float(input("Enter the Moment of Inertia:"))
x = float(input("Enter the distance where deflection is going to happen:")) 

A = (-4*M*H*H)/(E*I*3.14*3.14*3.14)

y = A * math.sin((3.14*x)/H)

print("The deflection of beam at " ,x, "distance is:",y)





