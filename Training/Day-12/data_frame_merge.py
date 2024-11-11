import pandas as pd

df1 = {'Name':['Elvin','Sara','Eldho','XYZ','ABC'],
       'Experience':[1,2,3,4,6],
       'City':['Kochi','Trivandrum','Ernakulam','Meghalaya','fhg']}
df2 = {'Name':['Elvin','Sara','Eldho'],
       'Age':[4,6,5],
       'City':['Kochi','Trivandrum','Ernakulam']}

df3 = pd.DataFrame(df1)
df4 = pd.DataFrame(df2)

df5 = pd.merge(df3,df4,on='Name',how='left')


#df5['City'] = df5['City_y'].fillna('NYC')

#df5.loc[df5['Name']=='XYZ','Age'] = df5['Age'].fillna(df5['Age'].mean())
df5.loc[df5['Name']=='XYZ','Age'] = df5['Age'].mean()

df5.to_csv('test.csv',index=False)

print(df5)