def f(x):
    return x**3 - x - 1

def bisection(x0,x1,e):

    condition = True
    while condition:
        xavg = (x0+x1)/2
        print(' xavg = %0.6f and f(xavg) = %0.6f' % (xavg, f(xavg)))

        if f(x0) * f(xavg) < 0:
            x1 = xavg
        else:
            x0 = xavg  

        condition = abs(f(xavg))>e

    print("Required root is:",xavg)    

x0=float(input("First guess?"))
x1=float(input("Second guess?"))
e=float(input("Tolerable error?"))

if f(x0) * f(x1) > 0.0:
    print("Guess values not correct.Try with different guess values")
else:
    bisection(x0,x1,e)    

    
       



    
