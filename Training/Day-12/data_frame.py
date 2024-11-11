import pandas as pd

df1 = {'Name':['Elvin','Sara','Eldho'],
       'Age':[24,24,55],
       'City':['Kochi','Trivandrum','Ernakulam']}
df2 = {'Name':['Elvin','Sara','Eldho'],
       'Age':[24,24,55],
       'City':['Kochi','Trivandrum','Ernakulam']}

print(pd.DataFrame(df1))


df3 = pd.DataFrame(df1)
df3.loc[df3['Name']=='Eldho','City']='Ernakulam'
df4 = pd.DataFrame(df2)
print(pd.concat([df3,df4],ignore_index=True))