import numpy as np
#array of 10 elements from 0 to 9
a=np.arange(10).reshape(2,-1)
print(a)
#array of 10 elements with 1 as a number
b=np.repeat(1,10).reshape(2,-1)
print(b)
#stacking two arrays a and b vertically
c=np.vstack([a,b])
print(f'the vertical stacked array is {c}')
#stacking two arrays a and b horizontally
d=np.hstack([a,b])
print(f'the horizontal stacked array is {d}')