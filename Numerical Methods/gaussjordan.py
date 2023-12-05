def gaussjordan():
    import numpy
    n=int(input("Enter no of variables"))
    a=numpy.zeros((n,n+1))
    x=numpy.zeros(n)
    print("Enter the coefficients of augmented matrix")
    for i in range(n):
        for j in range(n+1):
            a[i][j] = float(input('a['+str(i)+']['+str(j)+']='))
    print(a)
    for i in range(n):
        if a[i][i]==0.0:
            print("Divide by zero detected")
            break
        for j in range(n):
            if i!=j:
                r=a[j][i]/a[i][i]
                for k in range(n+1):
                    a[j][k]=a[j][k]-r*a[i][k]
    print("The diagonal matrix is:")
    print(a) 
    print("\nThe values of variable are: ")
    for i in range(n):
        x[i]=a[i][n]/a[i][i]
    for i in range(n): 
        print('x%d=%0.2f' %(i, x[i]), end='\n' )

gaussjordan() 