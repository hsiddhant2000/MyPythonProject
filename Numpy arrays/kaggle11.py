import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
#Extracting numbers in a given range in numpy array
a=a[(a>=5)&(a<=7)]
print(a)