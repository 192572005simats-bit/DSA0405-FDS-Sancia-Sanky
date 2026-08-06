import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("SampleSuperstore.csv")

Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

clean = df[(df["Sales"] >= lower) & (df["Sales"] <= upper)]

plt.hist(df["Sales"], bins=20)
plt.title("Before Removing Outliers")
plt.show()

plt.hist(clean["Sales"], bins=20)
plt.title("After Removing Outliers")
plt.show()

plt.boxplot(df["Sales"])
plt.title("Box Plot Before")
plt.show()

plt.boxplot(clean["Sales"])
plt.title("Box Plot After")
plt.show()