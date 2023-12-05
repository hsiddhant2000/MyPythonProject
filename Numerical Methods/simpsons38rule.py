def func(x):
    return 1 + x + x**3

def simpsons38(x0,xn,n):

    h = (xn - x0) / n

    integration = func(x0) + func(xn)

    for i in range(1,n):
        k = x0 + i*h

        if i%3 == 0:
            integration = integration + 2 * func(k)
        else:
            integration = integration + 3 * func(k)  

    integration = integration * 3 * h / 8   

    return integration   

lower_limit = float(input("Enter lower limit of integration: "))
upper_limit = float(input("Enter upper limit of integration: "))
sub_interval = int(input("Enter number of sub intervals: "))

result = simpsons38(lower_limit, upper_limit, sub_interval)
print("Integration result by Simpson's 3/8 method is: %0.6f" % (result) )


   