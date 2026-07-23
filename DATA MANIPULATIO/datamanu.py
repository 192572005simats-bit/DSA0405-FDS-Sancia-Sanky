import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\pooja\OneDrive\Desktop\StudentsPerformance.csv")

print("Original Data:")
print(df.head())

print("\nSorted by Math Score:")
sorted_df = df.sort_values(by="math score", ascending=False)
print(sorted_df[["gender", "race/ethnicity", "math score"]].head(10))

print("\nAverage Math Score by Gender:")
grouped_df = df.groupby("gender")["math score"].mean()
print(grouped_df)

df["Rank"] = df["math score"].rank(ascending=False, method="dense")

print("\nStudents with Rank:")
print(df[["gender", "math score", "Rank"]].sort_values(by="Rank").head(10))

top10 = sorted_df.head(10)

plt.figure(figsize=(8,5))
plt.bar(top10.index.astype(str), top10["math score"])
plt.title("Top 10 Math Scores - Bar Graph")
plt.xlabel("Students")
plt.ylabel("Math Score")
plt.show()

plt.figure(figsize=(8,5))
plt.plot(top10.index.astype(str), top10["math score"], marker='o')
plt.title("Top 10 Math Scores - Line Graph")
plt.xlabel("Students")
plt.ylabel("Math Score")
plt.show()

plt.figure(figsize=(6,6))
plt.pie(grouped_df, labels=grouped_df.index, autopct='%1.1f%%', startangle=90)
plt.title("Average Math Score by Gender - Pie Chart")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df["math score"], bins=5)
plt.title("Math Score Distribution - Histogram")
plt.xlabel("Math Score")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(8,5))
plt.scatter(df.index, df["math score"])
plt.title("Math Score - Scatter Plot")
plt.xlabel("Student Index")
plt.ylabel("Math Score")
plt.show()

plt.figure(figsize=(6,5))
plt.boxplot(df["math score"])
plt.title("Math Score - Box Plot")
plt.ylabel("Math Score")
plt.show()