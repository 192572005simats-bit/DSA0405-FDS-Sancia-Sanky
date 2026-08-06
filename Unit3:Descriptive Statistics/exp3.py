import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")

plt.hist(df["SalePrice"], bins=30)

plt.title("House Price Distribution")
plt.xlabel("Sale Price")
plt.ylabel("Frequency")

plt.show()

print("Bell shape = Normal Distribution")
print("Long right tail = Right Skewed")
print("Long left tail = Left Skewed")