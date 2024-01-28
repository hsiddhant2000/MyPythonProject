#Creating various pandas programs using DataFrame
#Created on 15-12-2023
import pandas as pd
#Dataframe is a 2D labelled datastructure 
#with columns of potentially different types
while True:
    choice = input("Enter choice 1/2/3/4/5/6/7/8/9:")

    if choice == '1':
        x=[10, 20, 30, 40]
        m = pd.DataFrame(x)
        print(m)

    elif choice == '2':
        y=[[10, 20, 30, 40],[50,60,70,80]]
        n=pd.DataFrame(y)
        print(n)
        rowIndex=['a', 'b']
        colIndex=['A', 'B', 'C', 'D']
        d=pd.DataFrame(y, rowIndex, colIndex)
        print(d)

    elif choice == '3':    
        list = [['I', 1],['am', 2],['coming', 3],['home', 4]]
        df=pd.DataFrame(list, columns =['Tag', 'number'])
        print(df)

    elif choice == '4':
        data = [['Sid', 1, 'Analyst'], ['amd', 2, 'Writer'], ['zax', 3, 'Editor']]
        columns=['Name', 'Age', 'Occupation']
        #from_records convert structured or record ndarray to DataFrame
        table = pd.DataFrame.from_records(data, columns=columns)
        print(table)

    elif choice == '5':    
        dataarray = [['Sid', 1, 'Analyst'], ['amd', 2, 'Writer'], ['zax', 3, 'Editor']]
        columnsarray=['Name', 'Age', 'Occupation']
        #from_records convert structured or record ndarray to DataFrame
        tablezip = pd.DataFrame.from_dict(dict(zip(columnsarray, zip(*dataarray))))
        print(tablezip)

    elif choice == '6':
        #Initialize lists of lists
        dataList = [['Tom',20], ['nick', 21], ['Krish', 19], ['Jack', 18]]
        #Creating a pandas DataFrame
        dataframe = pd.DataFrame(dataList, columns=['Name', 'Age'])
        #print dataframe
        print(dataframe)

    elif choice == '7':
        #Initializing data of lists
        dataIndex = [{'a': 1, 'b': 2, 'c': 3}, {'a': 10, 'b': 20, 'c': 30}]
        #Creating pandas DataFrame by passing 
        #lists of dictionaries and row index
        dataframeIndex = pd.DataFrame(dataIndex, index=['first', 'second'])
        #printing the data
        print(dataframeIndex)

    elif choice == '8':
        #Python code demonstrate creating
        #Pandas DataFrame from Dicts of series
        #Initialize data to lists
        dataseries = {'one': pd.Series([10, 20, 30, 40],index=['a', 'b', 'c','d']), 'two':pd.Series([30, 40, 50, 60],index=['a', 'b', 'c', 'd'])}
        #creating dataframe
        dataframeSeries = pd.DataFrame(dataseries)
        #print the data
        print(dataframeSeries)

    elif choice == '9':
        #Creating DataFrame from lists using zip.
        #list 1
        name = ['Sid','Tom','Dick','Harry']
        #List 2
        age = [13,34,56,67]
        #getting the list of tuples from two lists and 
        #merging them using zip()
        listofTuples = list(zip(name,age))
        #Converting listofTuples into pandas DataFrame
        dataUsingZip=pd.DataFrame(listofTuples, columns=['Name','Age'])
        #Printing data
        print(dataUsingZip)

    else:
        print("Invalid Input")

