"""
Filtrado de datos.
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

gender = ["Male", "Female"]
income = ["Poor", "Middle Class", "Rich"]

n = 500
gender_data = []
income_data = []

for i in range(0, n):
    gender_data.append(np.random.choice(gender))
    income_data.append(np.random.choice(income))

height = np.round(160 + 30 * np.random.randn(n), 2)
weight = np.round(65 + 25 * np.random.randn(n), 2)
age = np.round(30 + 12 * np.random.randn(n), 0)
income = np.round(18000 + 3500 * np.random.randn(n), 2)

data = pd.DataFrame(
    {
        "Gender": gender_data,
        "Economic Status": income_data,
        "Height": height,
        "Weight": weight,
        "Age": age,
        "Income": income
    }, index = range(1, 1 + n)
)

double_group = data.groupby(["Gender", "Economic Status"])

print(double_group["Age"].filter(lambda x: x.sum() > 2400))

# Transformación de variables.
zscore = lambda x: (x - x.mean()) / x.std()
z_group = double_group.transform(zscore)
print(z_group)

plt.hist(z_group["Age"])
plt.show()

# Reemplazar los valores N.A. por la media.
fill_na_mean = lambda x: x.fillna(x.mean())
double_group.transform(fill_na_mean)

# Operaciones diversas muy utiles.
print(double_group.head(1))
print(double_group.tail(1))
# El lugar número 32.
print(double_group.nth(32))

data_sorted = data.sort_values(["Age", "Income"])
print(data_sorted)
age_grouped = data_sorted.groupby("Gender")
print(age_grouped.head(1))
print(age_grouped.tail(1))