import sys !{sys.executable} -m pip install pulp
import pulp as p
LPprob = p.LPproblem('Problem', p.LPmaximize)

x = p.LPvariable("x", lowBound = 0)
y = p.LPvariable("y", lowBound = 0)

LPprob += x + y - 50

LPprob += 50 * x + 24 * y <= 2400
LPprob += 30 * x + 33 * y <= 2100
LPprob += x >= 45
LPprob += y >= 5

print(LPprob)

status = LPprob.solve()
print(p.LPstatus[status])

print(p.value(x), p.value(y),  p.value(LPprob.objective))