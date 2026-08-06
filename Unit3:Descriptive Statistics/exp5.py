import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

Q1 = df["math score"].quantile(0.25)
Q3 = df["math score"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["math score"] < lower) | (df["math score"] > upper)]

print("Outliers")
print(outliers)