import pandas as pd

df = pd.read_csv("input.csv")

df["salary"] = df["salary"] * 1.10

df.to_csv("output.csv", index=False)

print("ETL completed")
