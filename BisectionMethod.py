def func(x):
    return x^3 - x^2 + 2

def bisection(a,b):
    if (func(a) * func(b)):
        print(' values of a and b is not assumed right')
        return
    
    c = a
    while ((b-a) >= 0.01):

        c = (a+b)/2

        if (func(c) == 0.0):
            break

        if (func(c)*func(a) < 0):
            b = c
        else:
            a = c

    print("The value of root is ",c)            