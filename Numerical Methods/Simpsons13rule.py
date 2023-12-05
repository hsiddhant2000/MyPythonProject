# definition of function
def func(x):
    return 1+x**2

# definition of integral

def integrand(x0,xn,n):

    h = (xn - x0) / n

    integration = func(x0) + func(xn)

    for i in range(1,n):
        k = x0 + i*h

        if i%2 == 0:
            integration = integration + 2 * func(k)
        else:
            integration = integration + 4 * func(k)  

    integration = integration * h/3 

    return integration

lowerlimit = int(input("Enter lower limit of integration:"))         
upperlimit = int(input("Enter upper limit of integration:"))
subinterval = int(input("Enter no of subintervals:"))

result = simpsons13(lowerlimit, upperlimit, subinterval)
print("The result by integration method is",result)



      