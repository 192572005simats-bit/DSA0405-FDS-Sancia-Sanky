import pandas as pd

df = pd.read_csv("SampleSuperstore.csv")

Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

clean = df[(df["Sales"] >= lower) & (df["Sales"] <= upper)]

print("Original Shape:", df.shape)
print("Cleaned Shape:", clean.shape)

clean.to_csv("CleanedSales.csv", index=False)

print("Cleaned dataset saved")