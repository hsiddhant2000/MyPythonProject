#Finding out the eigenvalues and eigenvectors of a 4*4 matrix and finding the diagonal of eigenvalues
#Created on 10.12.23
#Modified on 11.12.23
#All imports are declared here.
import numpy as np

#Initial input matrix
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
def convert_1d_to_2d(eigenValues, variableLength):
    #Convert the list to a numpy array
    eigenvalueArray = np.array(eigenValues)
    #Calculating the cumulative sum of the variable lengths list
    cumulativeSum = np.cumsum(variableLength)
    #split the array at the indices obtained from the cumulative sum
    result = np.split(eigenvalueArray, cumulativeSum)
    #Converting the resulting array back to a list
    res = [list(subarr) for subarr in result][:-1]
    return res

#Driver code start here
variableLength = [2,2]
eigenvalueList=convert_1d_to_2d(eigenValues, variableLength)

#converting 1d array of eigenvalues into a 2d array
eigenValue2D = np.array(eigenvalueList)

#printing eigenvalues in 2D matrix
print("The 2D matrix of eigenvalues are")
print(eigenValue2D)

#printing the diagonal elements of the 2D matrix
print("The diagonals of eigenvalue are ")
print(np.diag(eigenValue2D))
