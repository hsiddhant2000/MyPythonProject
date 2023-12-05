def f(x):
    return x**3 - x - 1

x0=int(input("Enter first guess:"))
x1=int(input("Enter second guess:")) 
e=float(input("Enter tolerable error:"))
N=int(input("Maximum step:"))

print("Secant Method")
step = 1
condition  = True

while condition:
    if f(x0) == f(x1):
        print("Divide by zero error:")
        break
    x2 = (x0*f(x1) - x1*f(x0))/(x1 - x0)

    x0 = x1
    x1 = x2
    step = step + 1

    if step > N:
        print("Not Convergent")
        break

    condition = abs(f(x2)) > e
print("Required root is ",x2)
