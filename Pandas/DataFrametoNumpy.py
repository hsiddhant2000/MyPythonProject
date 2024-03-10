#To convert dataframe into Numpy array
#Created on 20-1-2024
import pandas as pd
#Converting data into dataframe
dataFrame=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], columns=['a','b','c'])
#Converting dataframe into numpy array 
converttoNumpy = dataFrame.to_numpy()
#Printing the array
print('\n Numpy Array\n-------\n',converttoNumpy)
#Converting dataframe into Numpy array from a to c
converttoNumpyac = dataFrame[['a','c']].to_numpy()
#Printing the array
print('\n Numpy Array a to c\n-------\n',converttoNumpyac)

#Creating a series of different characters
series = pd.Series(['ny','ch','ty','tr'])
#Creating a seperate data
indexW=['c1','c2','c3','c4']
#Converting the seperate data into index for the previous series
series.index = indexW
#Printing the series
print(series)

#Creating a series called seriesRange
seriesRange = pd.Series([11,21,8,18,65,18,32,10,5,32,None])
#Creating a data range starting from a particular date
indexrange=pd.date_range('2010-10-09 08:45',periods=11, freq='Y')
#Converting the seriesRange into an index
seriesRange.index=indexrange
#Printing the seriesRange
print(seriesRange)