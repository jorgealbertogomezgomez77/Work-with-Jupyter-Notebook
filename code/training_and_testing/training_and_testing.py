
# Conjunto de entrenamiento y conjunto de testing.

from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sklearn

filepath = "../../datasets/customer-churn-model/Customer Churn Model.txt"

data = pd.read_csv(filepath)
print(len(data))

# Dividir utilizando la distribución normal.
a = np.random.randn(len(data))
plt.hist(a)
plt.show()

check = (a < 0.5)
print(check)
#plt.hist(check)
#plt.show()

training = data[check]
testing = data[~check]

print(testing)
print(training)

# Con la librería sklearn.
train, test = train_test_split(data, test_size = 0.25)
print(train)
print(test)

# Usando una función de shuffle.
print(data.head())
data = sklearn.utils.shuffle(data)
print(data)
cut_id = int(0.75 * len(data))
train_data = data[:cut_id]
test_data = data[cut_id + 1:]
print(len(train_data))
print(len(test_data))

