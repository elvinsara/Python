import pandas as pd
df = pd.read_csv(r"C:\Users\Administrator\Downloads\tested.csv")


avg_age_survived = df[df['Survived']==1]['Age'].mean()
avg_age_notsurvived = df[df['Survived']==0]['Age'].mean()
print(avg_age_survived)


avg_survival_rate_by_gender = df.groupby('Sex')['Survived'].mean()*100
print(avg_survival_rate_by_gender)

df['Family Size'] = df['SibSp']+df['Parch']
print(df)

avg_survival_rate_by_family_size = df.groupby('Family Size')['Survived'].mean().reset_index()
print(avg_survival_rate_by_family_size)

avg_survival_rate_by_family_size.columns = ['Family Size','Family Survival rate']
print(avg_survival_rate_by_family_size)


df = pd.merge(df,)