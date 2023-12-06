import numpy as np
#Taking the following lists as input into x and y
x=[[1,2,3],[4,5,6]]
y=[[6,5,4],[3,2,1]]
#Converting the list into array
x1 = np.array(x)
y1 = np.array(y)
#concatenating the two arrays
carray = np.concatenate([x1,y1])
print(carray)
