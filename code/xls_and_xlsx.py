# Ficheros XLS y XLSX.

import pandas as pd

mainpath = "D:/PyCharm Work/Mach_Learn/machine_learning"
filename = "datasets/titanic/titanic3.xls"

titanic3 = pd.read_excel(mainpath + "/" + filename, "titanic3")

titanic3.to_csv(mainpath + "/out/titanic_custom.csv")

titanic3.to_excel(mainpath + "/out/titanic_custom.xls")

titanic3.to_json(mainpath + "/out/titanic_custom.json")