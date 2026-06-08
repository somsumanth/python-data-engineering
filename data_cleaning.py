import pandas as pd

df = pd.read_csv("employees.csv")

df = df.drop_duplicates()
df = df.fillna("Unknown")

print(df.head())
