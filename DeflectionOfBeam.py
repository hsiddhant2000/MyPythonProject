#Defelection of a simply supported beam at a particular point provided by the user
#Created on 29 September,2023
#Last modified on 6 December,2023
import math
from sympy import*

BeamHeight = float(input("Enter the length of beam in metres:"))
BendingMoment = float(input("Enter the Bending moment applied on beam in N.m :"))
YoungModulus = float(input("Enter the Youngs modulus of beam in N/m2:"))
MomentofInertia = float(input("Enter the Moment of Inertia in kgm^2:"))
Deflectiondistance = float(input("Enter the distance where deflection is going to happen in metres:")) 
pi = 3.14
#A is a constant
A = (-4*BendingMoment*BeamHeight**2)/(YoungModulus*MomentofInertia*pi**3)

Deflection = A * math.sin((pi*Deflectiondistance)/BeamHeight)

print("The deflection of beam at " ,Deflectiondistance, "distance is:",Deflection)





