
# Generación de números aleatorios.
import pandas as pd
import numpy as np
import random

data = pd.read_csv("../../datasets/customer-churn-model/Customer Churn Model.txt")

## Generar un número aleatorio entero entre 1 y 100.
np.random.randint(1, 100)

## La forma más clásica de generar un número aleatorio es entre 0 y 1 (con decimales).
np.random.random()

## Función que genera una lista de números aleatorios enteros dentro del intervalo [a, b].
def randint_list(n, a, b):
    x = []
    for i in range(n):
        x.append(np.random.randint(a, b))
    return x

print(randint_list(25, 1, 50))

# Imprimir multiplos de 7 aleatorios entre 0 y 100.
for i in range(10):
    print(random.randrange(0, 100, 7))

## Shuffling.
a = np.arange(100)
print(a)
np.random.shuffle(a)
print(a)

## Choise.
column_list = data.columns.values.tolist()
print(column_list)
print(np.random.choice(column_list))
print(np.random.seed(2018))
for i in range(5):
    print(np.random.random())
