#Performing iteration over rows using different methods in pandas DataFrame
#Created on 16-12-2023
#Modified on 18-12-2023
import pandas as pd

print("Select choice:")
print("1.Iterating over rows using index attribute of the DataFrame")
print("2.Iterating over rows using loc() and iloc() function of the DataFrame")
print("3.Iterating over rows using iterrows() method of the DataFrame")
print("4.Iterating over rows using itertuples() method of the DataFrame")
print("5.Iterating over rows using apply() method of the DataFrame")

#Performing iterations using different methods
while True:
    choice=input("Enter choice 1/2/3/4/5:")

    if choice == '1':
        #USING index ATTRIBUTE OF DataFrame TO ITERATE OVER ROWS
        #Defining a dictionary containing student data
        data = {'name':['sid','amit','dhawan'],'age':[12,13,14],'stream':['Math','Chem','Bio'],'Percentage':[67,78,89]}
        #Converting dictionary into DataFrame
        dataFrameDictionary = pd.DataFrame(data, columns=['name','age','stream','Percentage'])
        print("Given dataframe :\n",dataFrameDictionary)
        #iterate through each row and column and select
        #'Name' and 'stream'column respectively
        for ind in dataFrameDictionary.index:
            print(dataFrameDictionary['name'][ind], dataFrameDictionary['stream'][ind])
    
    elif choice == '2':
        #USING loc() and iloc() function OF DataFrame TO ITERATE OVER ROWS
        #Defining a dictionary containing student data
        dataloc = {'name':['sid','amit','dhawan'],'age':[12,13,14],'stream':['Math','Chem','Bio'],'Percentage':[67,78,89]}
        #Converting dictionary into DataFrame
        dataFrameloc = pd.DataFrame(dataloc, columns=['name','age','stream','Percentage'])
        print("Given dataframe :\n",dataFrameloc)

        print("\nIterating over rows using loc() function:\n")
        #iterate through each row and column and select
        #'Name' and 'stream'column respectively
        for i in range (len(dataFrameloc)):
            print(dataFrameloc.loc[i, "name"], dataFrameloc.loc[i, "stream"])
        
        print("\nIterating over rows using iloc() function:\n")
        for i in range (len(dataFrameloc)):
            print(dataFrameloc.iloc[i, 0], dataFrameloc.iloc[i, 1])    

    elif choice == '3':
        #USING iterrows() function OF DataFrame TO ITERATE OVER ROWS
        #Defining a dictionary containing student data
        dataiterrows = {'name':['sid','amit','dhawan'],'age':[12,13,14],'stream':['Math','Chem','Bio'],'Percentage':[67,78,89]}
        #Converting dictionary into DataFrame
        dataFrameiterrows = pd.DataFrame(dataiterrows, columns=['name','age','stream','Percentage'])
        print("Given dataframe :\n",dataFrameiterrows)

        print("\nIterating over rows using iterrows method:\n")
        #iterate through each row and column and select
        #'Name' and 'stream'column respectively
        for index, row in dataFrameiterrows.iterrows():
            print(row["name"], row["stream"])
    

    elif choice == '4':
        #USING itertuples() function OF DataFrame TO ITERATE OVER ROWS
        #Defining a dictionary containing student data
        dataitertuples = {'name':['sid','amit','dhawan'],'age':[12,13,14],'stream':['Math','Chem','Bio'],'percentage':[67,78,89]}
        #Converting dictionary into DataFrame
        dataFrameitertuples = pd.DataFrame(dataitertuples, columns=['name','age','stream','percentage'])
        print("Given dataframe :\n",dataFrameitertuples)

        print("\nIterating over rows using itertuples method:\n")
         #iterate through each row and column and select
        #'name' and 'percentage'column respectively
        for row in dataFrameitertuples.itertuples(index=True, name= 'Pandas'):
            print(getattr(row,"name"), getattr(row,"percentage"))

    elif choice == '5':  
        #USING apply() function OF DataFrame TO ITERATE OVER ROWS
        #Defining a dictionary containing student data
        dataApply = {'name':['sid','amit','dhawan'],'age':[12,13,14],'stream':['Math','Chem','Bio'],'percentage':[67,78,89]}
        #Converting dictionary into DataFrame
        dataFrameApply = pd.DataFrame(dataApply, columns=['name','age','stream','percentage'])
        print("Given dataframe :\n",dataFrameApply)

        print("\nIterating over rows using apply method:\n")
         #iterate through each row and column and select
        #'name' and 'percentage'column respectively
        print(dataFrameApply.apply(lambda row:row["name"] + " " + str(row["percentage"]),axis=1))
    else:
        print("Wrong choice")
    