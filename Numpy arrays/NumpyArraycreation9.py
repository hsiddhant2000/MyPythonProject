import numpy as np
n=int(input("Enter the number of variables:"))
#creating a 2D matrix using the number of variables entered by user
a=np.zeros((n,n,n))
print("The matrix is:")
#Finding out random integers between 1 and 10 and arranging them in a 5*5 matrix
for i in range(n):
    for j in range(n):
        for k in range(n):
            a[i][j][k] = np.random.randint(1,10)
print(a)    
