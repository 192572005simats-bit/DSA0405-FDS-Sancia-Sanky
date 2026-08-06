import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employee_salary_dataset.csv")

salary = df.select_dtypes(include="number").columns[-1]

plt.boxplot(df[salary])

plt.title("Salary Box Plot")

plt.show()

print("Points outside whiskers are outliers.")