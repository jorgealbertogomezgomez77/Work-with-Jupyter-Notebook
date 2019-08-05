import matplotlib.pyplot as pl
import pandas as pd
import numpy as np

data = pd.read_csv("../../datasets/customer-churn-model/Customer Churn Model.txt")

pl.boxplot(data["Day Calls"])
pl.ylabel("Número de llamadas diarias")
pl.title("Boxplot de llamadas diarias")
pl.show()

print(data["Day Calls"].describe())

IQR = data["Day Calls"].quantile(0.75) - data["Day Calls"].quantile(0.25)
print(data["Day Calls"].quantile(0.25) - 1.5 * IQR)