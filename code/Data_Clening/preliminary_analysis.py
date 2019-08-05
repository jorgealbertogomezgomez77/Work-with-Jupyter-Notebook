# Data Ceaning, análisis preliminar de los datos.

import pandas as pd
import os

mainpath = "D:/PyCharm Work/Mach_Learn/machine_learning/datasets"
filename = "titanic/titanic3.csv"
fullpath = os.path.join(mainpath, filename)
urldata = "https://raw.githubusercontent.com/jorgealbertogomezgomez77/machine_learning/master/datasets/titanic/titanic3.csv"

data = pd.read_csv(urldata)

print(data.head(10))
print(data.shape)
print(data.tail(10))
print(data.columns.values)

# Resumen de los estadísticos básicos de las variables numéricas.
print(data.describe())
print(data.dtypes)

# Missing values
print(pd.isnull(data["body"]))
print((pd.notnull(data["body"])).values.ravel().sum())

# Borrado de valores que faltan.
data.dropna(axis = 0, how = "all")

data2 = data
data2.dropna(axis = 0, how = "any")

data3 = data
data3.fillna(0)

data4 = data
data4 = data4.fillna("Desconocido")

data5 = data
data5["body"] = data5["body"].fillna(0)
data5["home.dest"] = data5["home.dest"].fillna("Desconocido")
print(data5.head(5))
pd.isnull(data5["age"]).values.ravel().sum()
data5["age"].fillna(data["age"].mean())
print(data5["age"][1291])
data5["age"].fillna(method = "ffill")
data5["age"].fillna(method = "backfill")

# Variables dummy.
dummy_sex = pd.get_dummies(data["sex"], prefix = "sex")
print(dummy_sex.head(10))
colum_names = data.columns.values.tolist()
print(colum_names)

# Borrar columna "sex" y agregar las variables dummy.
data = data.drop(["sex"], axis = 1)
data = pd.concat([data, dummy_sex], axis = 1)

def createDumies(df, var_name):
    dummy = pd.get_dummies(df[var_name], prefix = var_name)
    df = df.drop(var_name, axis = 1)
    df = pd.concat([df, dummy], axis = 1)
    return df
