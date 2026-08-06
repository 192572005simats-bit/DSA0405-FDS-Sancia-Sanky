import pandas as pd

df = pd.read_csv("employee_salary_dataset.csv")

print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

print("\nStatistical Summary")
print(df.describe(include='all'))