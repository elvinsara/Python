import pandas as pd

df = pd.read_csv(r"C:\Users\Administrator\Downloads\train_and_test2.csv")
print(df.head())


print(df["Age"].head())

print(df[["Age","Sex"]].head())


print(df[df["Age"]<25])

print(len(df.index))

print(df["Age"].mean())