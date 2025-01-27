import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

results = pd.read_csv('Datos/Results.csv')

languages = "LanguageHaveWorkedWith"
salary = "ConvertedCompYearly"

results.rename(columns={languages:"Languages", salary:"Salary"}, inplace = True)
# Elimina datos vacios que se suelen llamar Nan, subset elige el campo
results.dropna(subset=["Salary","Languages"],inplace=True)

# Los : recohge todos los datos pero nosotros especificamos las columanas con results.loc
results = results.loc[:, ["Country","Salary","Languages"]].sort_values(by="Salary")

filtro = (results["Salary"] >= 10000) & (results["Salary"] <= 3e6)
results = results[filtro]
#print(results)

lg = results["Languages"]
allLanguages = lg[21403].split(";")

for row in lg:
    for lang in row.split(";"):
        allLanguages.append(lang)

allLanguages = list(set(allLanguages))
print(allLanguages.sort())