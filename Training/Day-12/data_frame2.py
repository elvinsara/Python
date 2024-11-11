import pandas as pd
import numpy as np

df1 = {'Name':['Elvin','Sara','Eldho'],
       'Age':[24,24,55],
       'City':['Kochi','Trivandrum','Ernakulam']}
df2 = {'Name':['qwerty','fahad','fasil'],
       'Age':[24,24,55],
       'City':['Kochi','Trivandrum','Ernakulam']}

print(pd.DataFrame(df1))


df3 = pd.DataFrame(df1)

df3['City']=np.nan

df4 = pd.DataFrame(df2)
df5=pd.concat([df3,df4],ignore_index=True)
print(df5['City'].value_counts())

df5['City']=df5['City'].fillna('Chennai')
print(df5['City'].value_counts())