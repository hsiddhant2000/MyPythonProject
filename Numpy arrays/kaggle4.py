import numpy as np
arr = np.arange(10)
#making a copy of original array
c = arr.copy()
print(c)
#replacing all odd numbers in array with -1
m = c[c%2 == 1]=-1
#printing the original and modified array
print(f'original array{arr}')
print(f'modified array{c}')