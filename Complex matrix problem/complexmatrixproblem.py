import math
import os
import random
import re
import sys
#------------------------------------------------
#STEP1
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
#-------------------------------------------------------
#STEP2
matrix = []
for i in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
# print(matrix)
#-----------------------------------------------
#STEP3
k=3
reslist=[]
for j in range(0,k):
    res=[mat[j] for mat in matrix]
    reslist.append(res)
#print(reslist)  
#----------------------------------------------
#STEP4
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

newchar=" "
finallist[4]=newchar
finallist[5]=""
finallist[8]=""

presentence="".join(finallist)  
print(presentence) 









# import re
# str1 = "Welcome #@ !! to Tutorialspoint123"

# print("The given string is")
# print(str1)

# print("Removing special characters and white spaces")
# print(re.sub('[^A-Za-z0-9]+', '', str1))




# special_string="spe@#$ci87al*&"
# print("String before conversion: ",special_string)
# # Create a list with normal characters using the isalnum() method
# # use the join() function to convert the list to string
# normal_string="".join(ch for ch in special_string if ch.isalnum())
# # print the normal string 
# print("string after conversion:",normal_string)