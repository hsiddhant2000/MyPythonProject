import pandas as pd 
data={'Name':['IND','JEC','PMD'],'Age':[23,34,45],'Address':['delhi','goa','jaipur']}
df=pd.DataFrame(data)
print(df)

df["Name"]=df["Name"].str.lower()
df["Address"]=df["Address"].str.upper()
print(df)

df.dropna(inplace=True)
df["Address"]=df["Address"].str.split("a",n=1, expand=True)
print(df)
