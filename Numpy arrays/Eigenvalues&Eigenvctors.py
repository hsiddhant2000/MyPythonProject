#
import numpy as np
m = np.array([[9, 7, 8, 4],[9, 8, 6, 4],[4, 3, 4, 8],[6, 1, 8, 5]])
print(" Original square array:-",m)
#finding eigenvalues and eigenvectors 
w, v = np.linalg.eig(m)
#Printing the eigenvalues
print("Eigenvalues:-",w)
#Printing the eigenvectors
print("Eigenvectors:-",v)

#
def convert_1d_to_2d(w, var):
    #Convert the list to a numpy array
    arr = np.array(w)
    #Calculating the cumulative sum of the variable lengths list
    cumsum = np.cumsum(var)
    #split the array at the indices obtained from the cumulative sum
    result = np.split(arr, cumsum)
    #Converting the resulting array back to a list
    res = [list(subarr) for subarr in result][:-1]
    return res
var = [2,2]
l=convert_1d_to_2d(w, var)
#converting 1d array of eigenvalues into a 2d array
eigen = np.array(l)
#printing eigenvalues in 2D matrix
print("The 2D matrix of eigenvalues are",eigen)
#printing the diagonal elements of the 2D matrix
print("The diagonals of eigenvalue are ",np.diag(eigen))
