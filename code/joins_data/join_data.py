
from IPython.display import Image
import pandas as pd

filepath = "../../datasets/athletes/"
data_main = pd.read_csv(filepath + "Medals.csv", encoding = "ISO-8859-1")
print(data_main.head())

a = data_main["Athlete"].unique().tolist()
print(len(a))
print(data_main.shape)

data_country = pd.read_csv(filepath + "Athelete_Country_Map.csv", encoding = "ISO-8859-1")
print(data_country.head())
print(len(data_country))

print(data_country[data_country["Athlete"] == "Aleksandar Ciric"])

data_sports = pd.read_csv(filepath + "Athelete_Country_Map.csv", encoding = "ISO-8859-1")

data_sport = pd.read_csv(filepath + "Athelete_Sports_Map.csv", encoding = "ISO-8859-1")
print(data_sport.head(10))

print(data_sport[(data_sport["Athlete"] == "Chen Jing") |
                 (data_sport["Athlete"] == "Richard Thompson") |
                 (data_sport["Athlete"] == "Matt Ryan")])

data_country_dp = data_country.drop_duplicates(subset = "Athlete")

data_main_country = pd.merge(left = data_main, right = data_country_dp, left_on = "Athlete", right_on = "Athlete")
print(data_main_country.head(10))
print(data_main_country.shape)

print(data_main_country[data_main_country["Athlete"] == "Aleksandar Ciric"])

data_sports_dp = data_sports.drop_duplicates(subset = "Athlete")
print(len(data_sports_dp) == len(a))
data_final = pd.merge(left = data_main_country, right = data_sports_dp, left_on = "Athlete", right_on = "Athlete")
print(data_final.head(10))

Image(filename = "../../resources/inner-join.png")

