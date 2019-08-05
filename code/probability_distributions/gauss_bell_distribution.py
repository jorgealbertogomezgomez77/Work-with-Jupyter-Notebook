# Normal Distribution
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(100000)
x = range(1, 100001)
plt.plot(x, data)
plt.show()

plt.hist(data)
plt.show()

plt.plot(x, sorted(data))
plt.show()

mu = 5.5
std = 2.5
data = mu + std * np.random.randn(10000)    # z = (x - mu) / std  -> x = mu + std * z
plt.hist(data)
plt.show()

data2 = np.random.randn(2, 4)
print(data2)