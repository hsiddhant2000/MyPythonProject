import numpy as np
#creating a 1st 2D 4*5 matrix
a=np.zeros((4,5))
print("The matrix is:")
#Finding out random integers between 1 and 10 and arranging them in a 4*5 matrix
for i in range(4):
    for j in range(5):
        a[i][j] = np.random.randint(1,10)
print(a) 
#creating a 2nd 2D 4*5 matrix
b=np.zeros((4,5))
#Finding out random integers between 0 and 1 and arranging them in a 4*5 matrix
for k in range(4):
    for l in range(5):
        b[k][l] = np.random.randint(0,1)
print(b) 
#Adding the two matrices
c = a + b
print(c)  
