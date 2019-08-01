
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

n = 1000000

data = pd.DataFrame(
    {
        "A": np.random.randn(n),
        "B": 1.5 + 2.5 * np.random.randn(n),
        "C": np.random.uniform(5, 32, n)
    }
)

print(data.describe())
plt.hist(data["A"])
plt.show()
plt.hist(data["B"])
plt.show()
plt.hist(data["C"])
plt.show()

data2 = pd.read_csv("../../datasets/customer-churn-model/Customer Churn Model.txt")
columns_names = data2.columns.values.tolist()
length = len(columns_names)

data3 = pd.DataFrame(
    {
        "Columns_names": columns_names,
        "A": np.random.randn(length),
        "B": 1.5 + 2.5 * np.random.randn(length),
        "C": np.random.uniform(5, 32, length)
    },
    index = range(1, 1 + length)
)

print(data3)
#print(columns_names)
#print(data2.head())