import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

grades = []

for mark in df["math score"]:
    if mark >= 90:
        grades.append("A")
    elif mark >= 80:
        grades.append("B")
    elif mark >= 70:
        grades.append("C")
    elif mark >= 60:
        grades.append("D")
    else:
        grades.append("F")

grade_count = pd.Series(grades).value_counts().sort_index()

print(grade_count)

grade_count.plot(kind="bar")

plt.title("Grade Frequency Distribution")
plt.xlabel("Grades")
plt.ylabel("Frequency")

plt.show()