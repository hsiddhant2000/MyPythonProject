def func(x):
    return x * x * x - x * x + 2
def derivefunc(x):
    return 3 * x * x - 2 * x
x = int(input("Enter a number:"))
h = func(x)/derivefunc(x)
x = x - h

print("The new root is",x)      



