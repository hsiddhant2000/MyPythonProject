import numpy as np
#Creating various arrays and finding out their shape,size,dimension
#Created on 8.12.2023
print("Select choice.")
print("1.Finding out the shape of arrays.")
print("2.Finding out the size,dimension and shape of an array.")
#Performing array operations
while True:
    choice=input("Enter choice 1/2:")

    if choice == '1': 
        #Finding out the shape and orientation of arrays
        a = np.arange(6)
        #newaxis is used for ig 
        a2 = a[np.newaxis, :]
        a3 = a[:, np.newaxis]
        a4 = a[:, np.newaxis,np.newaxis]
        a5 = a[np.newaxis,:, np.newaxis]
        #shape method returns the shape of an array as a tuple
        a2.shape
        print("a is",a)
        print("shape of a is",a.shape)
        print("a2 is",a2)
        print("shape of a2 is",a2.shape)
        print("a3 is",a3)
        print("shape of a3 is",a3.shape)
        print("shape of a4 is",a4.shape)
        print("shape of a5 is",a5.shape)

    elif choice == '2':
        #Finding the dimension,size and shape of an array
        arr = np.array([[[1,2,3,4,6],[5,6,7,8,0],[9,10,11,12,9]]])
        #ndim is used to denote the number of dimensions of an array
        print(arr.ndim)
        #size is used to denote the number of elements of an array
        print(arr.size)
        #shape returns the shape of an array as a tuple 
        print(arr.shape)  

    else:
        print("Invalid Input")      