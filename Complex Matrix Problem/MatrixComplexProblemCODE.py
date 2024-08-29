#Created on 21-08-2024
#Modified on 29-08-2024
# User has to enter the rows and columns and the elements of rows and columns(Please Note:The no of elements should be 
# more than 17 otherwise the code will not work )

#The No of rows and columns should be in the format 5 * 4  or 4 * 5 or 3 * 7 or 7 * 3

#The elements will be converted into a matrix and will be subsequently printed as a string.
#Sample Input:
# 7 3
# T
# s
# i
# h
# %
# x
# i
#  
# #
# s
# M
#  
# $
# a
#  
# #
# t
# %
# i
# r
# !
# Sample Output:
# This is Matrix# %!

#-------------------------------------------------------
#STEP1:Taking input the number of Rows and columns to create a list from the user
Row=int(input("Enter the number of rows: "))
Column=int(input("Enter the no of column: "))

#-------------------------------------------------------
#STEP2:Taking input the elements from the user and creating a list
#Inilializing a matrix to create a list
matrix=[]
#Initializing a variable to count the no of elements entered
i=0
for row in range(Row):
    a=[]  
    for column in range(Column):
        i+=1
        a.append(input(f"Enter the entries rowwise {i}: "))
    matrix.append(a)
# print(matrix)  


#-----------------------------------------------
#STEP3:Selecting only the columns of the list created and adding them to a seperate list
k=Column
reslist=[]
for i in range(0, k):
    res=[mat[i] for mat in matrix]
    reslist.append(res)
# print(reslist)

#----------------------------------------------
#STEP4:Creating a new list named finallist from the strings present in reslist
def flat(reslist):
    flatlist=[]
    for element in reslist:
        if type(element) is list:
            for item in element:
                flatlist.append(item)
        else:
            flatlist.append(element)
    return flatlist
finallist=(flat(reslist))
# print(finallist)  
print("The length of the list is: ",len(finallist))


#----------------------------------------------
#STEP5:Replacing some characters with " " or "" in finallist
finallist[4]=" "
finallist[5]=""
finallist[8]=" "
finallist[17]=" "

#----------------------------------------------------
#STEP6:Joining the new finallist characters into a string sentence using join() function and printing the final sentence
finalsentence="".join(finallist)
print("The final sentence created is:")
print(finalsentence)







# mat=[]      
# for row in range(Row):
#     for column in range(Column):   
#         matrix[row][column]           
#         # print(matrix[row][column], end= "")    
#     print()            
# print(mat)

# sentence="".join(mat)
# print(sentence)



# Row=int(input("Enter the number of rows: "))
# Column=int(input("Enter the no of column: "))

# matrix=[]

# for row in range(Row):
#     a=[]  
#     for column in range(Column):
#         a.append(input("Enter the entries rowwise: "))    
#     matrix.append(a)

     
# for row in range(Row):
#     for column in range(Column):                
#         print(matrix[row][column], end= "")    
#     print()       
    
