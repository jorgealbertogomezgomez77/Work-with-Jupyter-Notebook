import matplotlib.pyplot as pl
import matplotlib as plt
import pandas as pd

data = pd.read_csv("../../datasets/customer-churn-model/Customer Churn Model.txt")

print(data.head(10))

#% matplotlib inline
# Scatter Plot (Nube de puntos).
data.plot(kind = "scatter", x = "Day Mins", y = "Day Charge")
plt.pyplot.show()

data.plot(kind = "scatter", x = "Night Mins", y = "Night Charge")
plt.pyplot.show()

figure, axs = pl.subplots(2, 2, sharey = True, sharex = True)
data.plot(kind = "scatter", x = "Day Mins", y = "Day Charge", ax = axs[0][0])
data.plot(kind = "scatter", x = "Night Mins", y = "Night Charge", ax = axs[0][1])
data.plot(kind = "scatter", x = "Day Calls", y = "Day Charge", ax = axs[1][0])
data.plot(kind = "scatter", x = "Night Calls", y = "Night Charge", ax = axs[1][1])
pl.show()


