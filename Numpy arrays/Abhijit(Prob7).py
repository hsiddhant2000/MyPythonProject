import numpy as np
# for loop for printing 100 numbers between 0 and 1 and arranging them in an array
for i in np.arange(0,1,0.01):
    a = np.array(np.arange(0,1,0.01))
#printing maximum number    
print(max(a))
#replacing the highest number with 99 and printing the final array
a[a == max(a)] = 99
print(a)