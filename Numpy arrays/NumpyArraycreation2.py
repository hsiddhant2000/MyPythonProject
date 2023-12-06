import numpy as np
#Asking for number of variables
n = int(input("Enter the number of variables:"))
#Creating a matrix of variable n*n having value 5
a = np.zeros((n,n))
print("The matrix is:")
for i in range(n):
    for j in range(n):
        a[i][j] = 5     
print(a)
