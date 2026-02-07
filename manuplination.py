import pandas as pd
import numpy as np

data = {
    "Id": [1, 2, 3, 4],
    "Name": ["Pankaj", "Heghna", "David", "Lisa"],
    "Role": ["CEO", np.nan, np.nan, np.nan],
    "Salary": [100, 200, np.nan, np.nan]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Fill missing Role with 'Employee'
df["Role"] = df["Role"].fillna("Employee")

# Fill missing Salary with average salary
avg_salary = df["Salary"].mean()
df["Salary"] = df["Salary"].fillna(avg_salary)

print("\nAfter Filling Missing Values:")
print(df)

# Sort by Salary
df_sorted = df.sort_values(by="Salary")
print("\nSorted by Salary:")
print(df_sorted)

# Filter employees with salary > 120
filtered_df = df[df["Salary"] > 120]
print("\nEmployees with Salary > 120:")
print(filtered_df)

# Add new column Bonus (10% of salary)
df["Bonus"] = df["Salary"] * 0.10

print("\nWith Bonus Column:")
print(df)
