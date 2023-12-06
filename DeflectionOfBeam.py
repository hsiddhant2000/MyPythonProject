#Defelection of a simply supported beam at a particular point provided by the user
#Created on 29 September,2023
#Last modified on 6 December,2023
import math
from sympy import*

BeamHeight = float(input("Enter the length of beam:"))
BM = float(input("Enter the Bending moment applied on beam:"))
E = float(input("Enter the Youngs modulus of beam:"))
I = float(input("Enter the Moment of Inertia:"))
x = float(input("Enter the distance where deflection is going to happen:")) 
pi = 3.14

A = (-4*BM*BeamHeight**2)/(E*I*pi**3)

Deflectiondistance = A * math.sin((pi*x)/BeamHeight)

print("The deflection of beam at " ,x, "distance is:",Deflectiondistance)





