
import numpy as np
import matplotlib.pyplot as plt

a = 1
b = 100
n = 20
data = np.random.uniform(a, b, n)

plt.hist(data)
plt.show()