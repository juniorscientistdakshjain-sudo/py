import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Id": [1, 2, 3, 4],
    "Name": ["Pankaj", "Heghna", "David", "Lisa"],
    "Role": ["CEO", np.nan, np.nan, np.nan],
    "Salary": [100, 200, np.nan, np.nan]
}

df = pd.DataFrame(data)

print(df)

# Bar chart for Salary
plt.figure()
plt.bar(df["Name"], df["Salary"])
plt.xlabel("Name")
plt.ylabel("Salary")
plt.title("Salary Distribution")
plt.show()

# Line plot for Id vs Salary
plt.figure()
plt.plot(df["Id"], df["Salary"], marker='o')
plt.xlabel("Id")
plt.ylabel("Salary")
plt.title("Id vs Salary")
plt.show()
