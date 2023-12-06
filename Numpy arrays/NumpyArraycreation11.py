#Creating an array of 50 numbers between 0 and 4*pi with equal interval,and another array where each member of it is a cosine of the corrosponding member of previous array.
import numpy as np
#linespace function is used for producing an evenly spaced sequence between specific intervals
p = np.linspace(0,4*np.pi)
#converting the sequence into an array
arr = np.array(p)
#printing the array
print(arr)
#creating a new array by getting the cosine of all elements of arr.
resultarray=np.cos(arr)
#printing the new array
print("The resultant array is",resultarray)
