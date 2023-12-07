import numpy as np
print("Select choice:")
print("1:Preparing an array from range 0 to 25 and then reshaping into a 5*5 array")
print("2:Asking for number of variables and creating a matrix of variable n*n having value 5")
print("3:Printing numbers between 0 and 1 with interval 0.125")
print("4:Taking 2 lists as input,converting the list into array and concatenating them")
print("5:Taking elements of array as an input and splitting the array into 3 parts: ")
print("6.Printing 100 numbers between 0 and 1 with interval 0.01 and replacing the largest number with 99")
print("7.")

while True:
    choice = input("Enter choice 1/2/3/4/5/6/7:")

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
        #creating a 2D matrix using the number of variables entered by user
        a=np.zeros((n,n,n))
        print("The matrix is:")
        #Finding out random integers between 1 and 10 and arranging them in a 5*5 matrix
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    a[i][j][k] = np.random.randint(0,1)
        print(a)  

    else:
        print("Invalid input") 

    








    
             











