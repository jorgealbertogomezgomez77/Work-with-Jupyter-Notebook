
"""
Agregación de datos por categorioas.
"""

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

print(gender_data[1:10])
print(income_data[1:10])

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
print(data.head())

grouped_gender = data.groupby("Gender")
print(grouped_gender.groups)

for names, groups in grouped_gender:
    print(names)
    print(groups)

print(grouped_gender.get_group("Female"))

double_group = data.groupby(["Gender", "Economic Status"])
print(double_group.groups)

for names, groups in double_group:
    print(names)
    print(groups)

print(double_group.sum())
print(double_group.mean())
print(double_group.size())
print(double_group.describe())

grouped_income = double_group["Income"]
print(grouped_income.describe())

double_group.aggregate(
    {
        "Income": np.sum,
        "Age": np.mean,
        "Height": np.std
    }
)

double_group.aggregate(
    {
        "Age": np.mean,
        "Height": lambda h: (np.mean(h)) / np.std(h)
    }
)

print(double_group.aggregate([np.sum, np.mean, np.std]))
