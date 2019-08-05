
# Concatenar y apendizar data sets.

import pandas as pd

red_wine = pd.read_csv("../../datasets/wine/winequality-red.csv", sep = ";")
print(red_wine.head(10))
print(red_wine.columns.values.tolist())
print(red_wine.shape)

white_wine = pd.read_csv("../../datasets/wine/winequality-white.csv", sep = ";")
print(white_wine.head(10))
print(white_wine.columns.values.tolist())
print(white_wine.shape)


wine_data = pd.concat([red_wine, white_wine], axis = 0)
print(wine_data.shape)
print(wine_data.head(10))

data1 = wine_data.head(10)
data2 = wine_data[300: 310]
data3 = wine_data.tail(10)

wine_scramble = pd.concat([data1, data2, data3], axis = 0)
print(wine_scramble)