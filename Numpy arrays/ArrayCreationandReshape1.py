import numpy as np
print("Select choice:")
print("1:Preparing an array from range 0 to 25 and then reshaping into a 5*5 array")
print("2:Asking for number of variables and creating a matrix of variable n*n having value 5")
print("3:Printing numbers between 0 and 1 with interval 0.125")
print("4:Taking 2 lists as input,converting the list into array and concatenating them")
print("5:Taking elements of array as an input and splitting the array into 3 parts: ")
print("6.Printing 100 numbers between 0 and 1 with interval 0.01 and replacing the largest number with 99")
print("7.Creating a 3D array of random numbers between 0 and 1")
print("8.Finding out random integers between 1 and 10 and arranging them in a 5*5 matrix")
print("9.Creating an array of 50 numbers between 0 and 4*pi with equal interval,and another array where each member of it is a cosine of the corrosponding member of previous array.")
print("10.stacking two arrays vertically and horizontally.")
print("11.Replacing all odd numbers in an array with -1")
print("12.Extracting numbers in a given range in numpy array.")

while True:
    choice = input("Enter choice 1/2/3/4/5/6/7/8/9/10/11/12:")

    if choice == '1':
        #Preparing an array from range 0 to 25 and then reshaping into a 5*5 array
        a = np.arange(0,25).reshape(5,5)
        print(a)
        
    elif choice == '2':   
        #Asking for number of variables
        n = int(input("Enter the number of variables:"))   
        a = np.zeros((n,n))
        #Creating a matrix of variable n*n having value 5
        print("The matrix is:")
        for i in range(n):
            for j in range(n):
                a[i][j] = 5
        print(a)        

    elif choice == '3':
        # for loop for printing numbers between 0 and 1 with interval 0.125
        for i in np.arange(0,1,0.125):
            a = np.array(np.arange(0,1,0.125))
        print(a)
        
    elif choice == '4':
        #Taking the following lists as input into x and y
        x=[[1,2,3],[4,5,6]]
        y=[[6,5,4],[3,2,1]]
        #Converting the list into array
        x1 = np.array(x)
        y1 = np.array(y)
        #concatenating the two arrays
        carray = np.concatenate([x1,y1])
        print(carray)

    elif choice == '5':
        #Taking element of array as an input
        A = np.array([1,2,3,4,5,6,7,8,9])
        #Splitting the array
        Asplit = np.split(A,3)
        print(Asplit)

    elif choice == '6':  
        for i in np.arange(0,1,0.01): 
            a = np.array(np.arange(0,1,0.01))
        #printing maximum number    
        print(max(a))
        #replacing the highest number with 99 and printing the final array
        a[a == max(a)] = 99
        print(a)  

    elif choice == '7':
        n=int(input("Enter the number of variables:"))
        #creating a 3D matrix using the number of variables entered by user
        a=np.zeros((n,n,n))
        print("The matrix is:")
        #Creating a 3D array of random numbers between 0 and 1
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    a[i][j][k] = np.random.randint(0,1)
        print(a)  

    elif choice == '8':  
        n=int(input("Enter the number of variables:"))
        #creating a 2D matrix using the number of variables entered by user
        a=np.zeros((n,n))
        print("The matrix is:")
        #Finding out random integers between 1 and 10 and arranging them in a 5*5 matrix
        for i in range(n):
             for j in range(n):
                a[i][j] = np.random.randint(1,10)
        print(a) 

    elif choice == '9':
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

    elif choice == '10':
        #array of 10 elements from 0 to 9
        a=np.arange(10).reshape(2,-1)
        print(a)
        #array of 10 elements with 1 as a number
        b=np.repeat(1,10).reshape(2,-1)
        print(b)
        #stacking two arrays a and b vertically
        c=np.vstack([a,b])
        print(f'the vertical stacked array is {c}')
        #stacking two arrays a and b horizontally
        d=np.hstack([a,b])
        print(f'the horizontal stacked array is {d}')

    elif choice == '11':
        arr = np.arange(10)
        #making a copy of original array
        c = arr.copy()
        print(c)
        #replacing all odd numbers in array with -1
        m = c[c%2 == 1]=-1
        #printing the original and modified array
        print(f'original array{arr}')
        print(f'modified array{c}')

    elif choice == '12':  
        a=np.array([1,2,3,4,5,6,7,8,9])
        #Extracting numbers in a given range in numpy array
        a=a[(a>=5)&(a<=7)]
        print(a)    

    else:
        print("Invalid input") 

    








    
             










