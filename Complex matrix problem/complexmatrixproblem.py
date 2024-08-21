#Created on 21-08-2024
# INPUT:
# 7
# Tsi
# h%x
# i #
# sM 
# $a 
# #t%
# ir!

# OUTPUT:
# This is Matrix# %!

import math
import os
import random
import re
import sys
#------------------------------------------------
#STEP1:Taking input the number of elements to create a list from the user

n=int(input("Enter the no of elements:"))
#-------------------------------------------------------
#STEP2:Taking input the elements from the user and creating a list 
matrix = []
for i in range(n):
    matrix_item = input(f"Enter the contents of the matrix {i+1}: ")
    matrix.append(matrix_item)
# print(matrix)
#-----------------------------------------------
#STEP3:Selecting only the columns of the list created and adding them to a seperate list
k=3
reslist=[]
for j in range(0,k):
    res=[mat[j] for mat in matrix]
    reslist.append(res)
#print(reslist)  
#----------------------------------------------
#STEP4:Creating a new sentence finallist from the strings present in reslist
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
#----------------------------------------------
#STEP5:Replacing some characters with " " or "" in finallist
newchar=" "
finallist[4]=newchar
finallist[5]=""
finallist[8]=""

#STEP6:Joining the new finallist characters into a string sentence using join() function and printing the final sentence
sentence="".join(finallist)  
print(sentence) 









