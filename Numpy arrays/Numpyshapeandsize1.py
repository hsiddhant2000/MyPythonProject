import numpy as np
a = np.arange(6)
#newaxis is used for increasing the dimensions of an array
a2 = a[np.newaxis, :]
a3 = a[:, np.newaxis]
a4 = a[:, np.newaxis,np.newaxis]
a5 = a[np.newaxis,:, np.newaxis]
#shape method returns the shape of an array as a tuple
a2.shape
print("a is",a)
print("shape of a is",a.shape)
print("a2 is",a2)
print("shape of a2 is",a2.shape)
print("a3 is",a3)
print("shape of a3 is",a3.shape)
print("shape of a4 is",a4.shape)
print("shape of a5 is",a5.shape)