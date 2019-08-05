# Datos distribuidos.

import pandas as pd

data = pd.read_csv("../../datasets/distributed-data/001.csv")
print(data.head())

"""
- Importar el primer fichero
- Hacemos un bucle para ir recorriendo todos y cada uno de los ficheros.
    - Importante tener una consistencia en el nombre de los ficheros.
    - Importamos los ficheros uno a uno.
    - Cada uno de ellos debe apendizarse (añadirse al final) del primer fichero que ya habíamos cargado.
- Repetimos el bucle hasta que no queden ficheros.
"""

filepath = "../../datasets/distributed-data/"
data = pd.read_csv(filepath + "001.csv")
final_length = len(data)
for i in range(2,333):
    if i < 10:
        filename = "00" + str(i)
    if 10 <= i < 100:
        filename = "0" + str(i)
    if i >= 100:
        filename = str(i)
    file = filepath + filename + ".csv"
    temp_data = pd.read_csv(file)
    final_length += len(temp_data)
    print(final_length)

    data = pd.concat([data, temp_data], axis = 0)

print(data.shape)
print(data.tail())
print(data.head())

print(final_length == data.shape[0])