import numpy as np
#Creating a random vector of size 20
x=np.random.random(20)
print("Resultant array:")
#Printing a resultant array
print(x)
print(max(x))
#Finding the maximum number in the array and replacing it with zero.
x[x == max(x)] = 0
print(x)