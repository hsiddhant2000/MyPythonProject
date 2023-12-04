import numpy as np
#boolean array
arr=np.array([0,1,1,0,0,1])
print(f'original array:{arr}')
#converting the original array into boolean array
boolarr = np.array(arr, dtype='bool')
print(f'boolean array:{boolarr}')