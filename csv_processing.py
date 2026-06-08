import pandas as pd

df = pd.read_csv("sales.csv")

total_sales = df["sales_amount"].sum()

print("Total Sales:", total_sales)
