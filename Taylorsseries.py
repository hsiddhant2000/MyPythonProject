from sympy import diff, symbols, factorial, exp, pretty_print

x = symbols("x")

func = x**3 + x**2 + 1
n = 10
x0 = 0
result = func.subs(x, x0)


for i in range(1, n):
    result += diff(func, x, i)*(x - x0)**i / factorial(i)

pretty_print(result)    