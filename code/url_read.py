# Leer datos desde una URL.
# Primero importamos la librería y hacemos la conección con la web de los datos.
import os

import pandas as pd
import urllib3

medals_url = "http://winterolympicsmedals.com/medals.csv"
medals_data = pd.read_csv(medals_url)
medals_data.head()

http = urllib3.PoolManager()
r = http.request('GET', medals_url)
print("El estado de la respuesta es: " + str(r.status))
response = r.data

# El objeto response contiene un string binario, así que lo convertimos a un string descodificándolo en UTF-8.
str_data = response.decode('utf-8')

# Dividimos el string en un array de filas, separándolo por enters.
lines = str_data.split("\n")

# La primera línea contiene la cabecera, así que la extraemos.
col_names = lines[0].split(",")
n_cols = len(col_names)

# Generamos un diccionario vacío donde irá la información procesada desde la URL externa.
counter = 0
main_dict = {}
for col in col_names:
    main_dict[col] = []

# Procesamos fila a fila la información para ir rellenando el diccionario con los datos como haciamos antes.
for line in lines:
    # Nos saltamos la primera línea que es la que contiene la cabecera y ya tenemos procesada.
    if(counter > 0):
        # Dividimos cada string por las comas como elemento separador.
        values = line.strip().split(",")
        # Añadimos cada valor a su respectiva columna del diccionario.
        for i in range(len(col_names)):
            main_dict[col_names[i]].append(values[i])
    counter += 1

print("El data set tiene %d filas y %d columnas" %(counter, n_cols))

# Convertimos el diccionario procesado a Data Frame y comprobamos que los datos son correctos.
medals_df = pd.DataFrame(main_dict)
print(medals_df.head())

# Elegimos donde guardarlo (en la carpeta athletas es donde tiene mas sentido por el contexto del análisis)
mainpath = "D:/PyCharm Work/Mach_Learn/machine_learning"
filename = "out/athletas/downloaded_medals."
fullpath = os.path.join(mainpath, filename)

# Lo guardamos en CSV en JSON o en Excel según queremos.
medals_df.to_csv(fullpath + "csv")
medals_df.to_json(fullpath + "json")
medals_df.to_excel(fullpath + "xls")
