#Finding out the eigenvalues and eigenvectors of a 4*4 matrix and finding the diagonal of eigenvalues

#All imports are declared here.
import numpy as np
InitialMatrix = np.array([[9, 7, 8, 4],[9, 8, 6, 4],[4, 3, 4, 8],[6, 1, 8, 5]])
print(" Original square array:-")
print(InitialMatrix)
#finding eigenvalues and eigenvectors 
eigenValues, eigenVectors= np.linalg.eig(InitialMatrix)
#Printing the eigenvalues
print("Eigenvalues:-",eigenValues)
#Printing the eigenvectors
print("Eigenvectors:-")
print(eigenVectors)

#Converting 1D array to 2D array
def convert_1d_to_2d(eigenValues, var):
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
