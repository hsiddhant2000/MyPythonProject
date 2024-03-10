#Creating a program to import  an excel sheet and printing its
#different data
#created on  21-12-2023
import pandas as pd

#Importing data from an Excel file 
#r is a raw string literal
studentData=pd.read_excel(r"C:\Users\KIIT\Desktop\Pandas\studentdatanew.xlsx")
#Printing all the data in excel file
print("1.Student Data from studentdatanew file:")
print(studentData)
print("--------------------------------------------------------")
print("2.Upper part of student data:")
print(studentData.head(3))
print("--------------------------------------------------------")
print("3.Lower part of student data:")
print(studentData.tail(3))
print("--------------------------------------------------------")
print("4.Description of student data:")
print(studentData.describe())
print("--------------------------------------------------------")

#Extracting roll numbers from studentdatanew fileand printing them.
Rollnumber=pd.Series(studentData['Roll Number'])
print("5.Roll No of Students:")
print(Rollnumber)
print("--------------------------------------------------------")

#Collecting phone numbers from studentdatanew file.
Phonenumber=pd.Series(studentData['Mobile Number'])
#Extracting phone number upto student number 4
phoneNoUpto4=Phonenumber.head(5)
#printing the phone numbers
print("6.Phone no upto student no 4:")
print(phoneNoUpto4)
print("--------------------------------------------------------")

#Collecting personal email id from studentdatanew file.
Emailid=pd.Series(studentData['Personal Email Id'])
#Extracting personal email id from student number 3 to student number 6 
emailId3to6=Emailid.iloc[3:6]
#printing the personal email ids
print("7.Personal Email ids from Student 3 to student 6:")
print(emailId3to6)
print("--------------------------------------------------------")

studentDataIndex=pd.read_excel(r"C:\Users\KIIT\Desktop\Pandas\studentdatanew.xlsx",index_col="Name")
print("8.The entire excel data with the names as index column:")
print(studentDataIndex)
sounav=studentDataIndex.loc["Sounav Banerjee"]
siddhant=studentDataIndex.loc["Siddhant Hore"]
print("9.DATA OF INDIVIDUAL NAMES ARE:")
print(sounav, "\n\n\n", siddhant)
print("--------------------------------------------------------")

#Slicing only rows
print("10.Slicing data till student 4:")
slicing_student_data_Rows=studentData.iloc[:4, ]
print(slicing_student_data_Rows)
print("--------------------------------------------------------")

#Slicing both rows and columns
print("11.Slicing rows till index 4 and columns from 1-4")
slicing_student_data_RowsandColumns=studentData.iloc[:4, 1:4]
print(slicing_student_data_RowsandColumns)
print("--------------------------------------------------------")

print("12.The names of individual students in the list are:")
for i,j in studentData.iterrows():
    print(i, j)
print("------------------------------------------------------")

print("12.A")
column = studentData.head(7)

ListColumn = list(column)
for i in ListColumn:
    print(column[i][5])
print("------------------------------------------------------")

studentDataNew=pd.read_excel(r"C:\Users\KIIT\Desktop\Pandas\studentdatanew.xlsx",skiprows=[1,5], header=0)
print("13.Dataset after skipping rows:")
print(studentDataNew)
print("------------------------------------------------------")

studentData_skip_rows=pd.read_excel(r"C:\Users\KIIT\Desktop\Pandas\studentdatanew.xlsx", skiprows=2)
print("14.Dataset after skipping starting rows:")
print(studentData_skip_rows)

studentData["Name of examination"]=studentData["Name of examination"].str.replace("MT132", "WER",case=False)
print(studentData)