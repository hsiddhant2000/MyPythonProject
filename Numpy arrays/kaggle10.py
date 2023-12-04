import numpy as np
a=np.array([1,2,3])
m=np.hstack((np.repeat(a,3)), np.tile(a,3))
print(m)