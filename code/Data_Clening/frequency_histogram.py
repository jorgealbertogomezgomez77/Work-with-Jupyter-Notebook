import matplotlib.pyplot as pl
import pandas as pd
import numpy as np

data = pd.read_csv("../../datasets/customer-churn-model/Customer Churn Model.txt")

k = int(np.ceil(1 + np.log2(3333)))
pl.hist(data["Day Calls"], bins = k)
#pl.hist(data["Day Calls"], bins = 25)
#pl.hist(data["Day Calls"], bins = [0, 60, 90, 120, 150, 180])
pl.xlabel("Número de llamadas al día")
pl.ylabel("Frecuencia")
pl.title("Histograma del número de llamadas al día")
pl.show()