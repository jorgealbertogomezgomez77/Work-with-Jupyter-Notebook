
# Carga de datos a través de la función read_csv.
import pandas as pd
import os

mainpath = "D:/PyCharm Work/Mach_Learn\machine_learning/datasets"
filename = "titanic/titanic3.csv"
fullpath = os.path.join(mainpath, filename)

data = pd.read_csv(fullpath)
#data = pd.read_csv("../datasets/titanic/titanic3.csv")
#other = pd.read_csv( filepath_or_buffer = "D:/PyCharm Work/Mach_Learn\machine_learning/datasets/titanic/titanic3.csv")

data2 = pd.read_csv(mainpath + "/" + "customer-churn-model/Customer Churn Model.txt")

print(data.head())
print(data2.head())
print(data2.columns.values)
#print(other.head())

data_cols = pd.read_csv(mainpath + "/" + "customer-churn-model/Customer Churn Columns.csv")
data_col_list = data_cols["Column_Names"].tolist()

print(data_col_list)

data2 = pd.read_csv(mainpath + "/" + "customer-churn-model/Customer Churn Model.txt", header = None, names = data_col_list)
print(data2.columns.values)

data3 = open(mainpath + "/" + "customer-churn-model/Customer Churn Model.txt", "r")
cols = data3.readline().strip().split(",")
n_cols = len(cols)

print(cols)

counter = 0
main_dict = {}
for col in cols:
    main_dict[col] = []

for line in data3:
    values = line.strip().split(",")
    for i in range(len(cols)):
        main_dict[cols[i]].append(values[i])
    counter += 1

print("El dataset tiene %d filas y %d columnas" %(counter, n_cols))

df3 = pd.DataFrame(main_dict)
print(df3.head())


infile = "../datasets/titanic/titanic3.csv"
outfile = "../out/titanic_new.txt"
with open(infile, "r") as infile:
    with open(outfile, "w") as outfile:
        for line in infile:
            fields = line.strip().split(",")
            outfile.write("\t".join(fields))
            outfile.write("\n")


