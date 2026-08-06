import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Iris.csv")

print("Dataset Information")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

print("\nDescriptive Statistics")
print(df.describe())

df.hist(figsize=(10,8))
plt.show()

df.boxplot(figsize=(10,6))
plt.show()

columns = ["SepalLengthCm",
           "SepalWidthCm",
           "PetalLengthCm",
           "PetalWidthCm"]

clean = df.copy()

for col in columns:

    Q1 = clean[col].quantile(0.25)
    Q3 = clean[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    clean = clean[(clean[col] >= lower) &
                  (clean[col] <= upper)]

print("\nCleaned Dataset Shape")
print(clean.shape)

clean.to_csv("Cleaned_Iris.csv", index=False)

print("Cleaned dataset saved")