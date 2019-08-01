# Imports sentences
import pandas as pd

data = pd.read_csv("../../datasets/customer-churn-model/Customer Churn Model.txt")
print(data.head())

# Crear un subconjunto de datos.
account_length = data["Account Length"]
print(account_length.head())
print(type(account_length))

subset = data[["Account Length", "Phone", "Eve Charge", "Night Calls"]]
print(subset.head())
print(type(subset))

desired_colums = ["Account Length", "Phone", "Eve Charge", "Day Calls"]
subset = data[desired_colums]
print(subset.head())

all_columns_list = data.columns.values.tolist()
print(all_columns_list)

sublist = [x for x in all_columns_list if x not in desired_colums]
print(sublist)

subset =data[sublist]
print(subset.head())

# Primeras 25 filas del datasets incluyendo la cabecera.
print(data[0:25])

# Usuarios con "Day Mins" mayor que 200.
data1 = data[data["Day Mins"] > 200]
print(data1)

# Usuarios de New York (State = "NY").
data2 = data[data["State"] == "NY"]
print(data2)

## AND -> &.
data3 = data[(data["Day Mins"] > 300) & (data["State"] == "NY")]
print(data3)

## OR -> |.
data4 = data[(data["Day Mins"] > 300) | (data["State"] == "NY")]
print(data4)

# Datos donde las llamadas de noche sean mayores que las de dia.
data5 = data[data["Night Calls"] > data["Day Calls"]]
data5.shape
print(data5)


# Minutos de dia, de noche y longitud de la cuenta de los primeros 50 individuos.
subset_first_50 = data[["Day Mins", "Night Mins", "Account Length"]][:50]
print(subset_first_50.head())


#Primeras 10 filas y de la columna 3 a la 6.
#print(data.ix[1:10, 3:6])  # is deprecated
print(data.iloc[1:10, 3:6])

data.iloc[:, 3:6]
data.iloc[1:10, :]
data.iloc[1:10, [2, 5, 7]]
data.iloc[[1, 5, 8, 36], [2, 5, 7]]
data.loc[[1, 5, 8, 36], ["Area Code", "VMail Plan", "Day Mins"]]    # iloc porque estamos accediendo por etiquetas.



data["Total Mins"] = data["Day Mins"] + data["Night Mins"] + data["Eve Mins"]
print(data["Total Mins"].head())

data["Total Calls"] = data["Day Calls"] + data["Night Calls"] + data["Eve Calls"]
print(data["Total Calls"].head())
print(data.shape)