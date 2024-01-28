#To create an excel sheet using pandas library
#Created on 28-01-2024
#importing pandas and openpxyl
import pandas as pd 
import openpyxl

#Converting data into a  dataframe named df
df = pd.DataFrame([['Hi', 'Hello', 'Hey'], ['Person1', 'Person2', 'Person3'], ['Person4','Person5', 'Person6']], index=['one', 'two', 'three'], columns=['a', 'b', 'c'])
#Converting another set of data into a second dataframe named df2
df2=pd.DataFrame([['we','do','not'],['want','to','come'],['here','for','dinner']],index=[1,2,3],columns=['a','b','c'])
#Creating a new excel file with the help of excelwriter and 
#printing first set of data in a sheet named Sheet1
#and second set of data in a sheet named Sheet2
with pd.ExcelWriter('New_excel_Multisheet.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sheet1')
    df2.to_excel(writer, sheet_name='Sheet2')