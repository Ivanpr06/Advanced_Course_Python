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
allLanguages = lg[30294].split(";")

for row in lg:
    for lang in row.split(";"):
        if lang not in allLanguages:
            allLanguages.append(lang)

allLanguages = sorted(allLanguages)
#print(allLanguages)

meanSalary = pd.DataFrame(data=np.zeros(len(allLanguages)), index=allLanguages, columns=["Salary"])

for lang in allLanguages:
    mask = results["Languages"].str.contains(lang)
    # Mean hace las medias, loc toma argumentos
    average = results.loc[mask, "Salary"].mean()
    meanSalary.loc[lang, "Salary"] = average

# print(meanSalary)

# Gráfico
colors = [
    "#03071E",
    "#370617",
    "#6A040F",
    "#9D0208",
    "#D00000",
    "#DC2F02",
    "#E85D04",
    "#F48C06",
    "#FAA307",
    "#FFBA08"
]

fontdict = {
    'family': 'serif',
    'color':  'darkred',
    'weight': 'normal',
    'size': 16,
}

meanSalary.sort_values(by="Salary", ascending=True, inplace=True)
plt.style.use('ggplot')
plt.barh(meanSalary.index, meanSalary["Salary"], color=colors, height=0.8)
# Linea que represente el salario medio de todos los lenguajes
plt.vlines(meanSalary["Salary"].mean(),0,len(meanSalary["Salary"]), color="red", linestyles='dashed', label="Mean Salary")

plt.title("Programming Languages Yearly Compensatiom")
plt.xlabel("Mean Salary in $")
plt.ylabel("Languages")

# Pone dolares en los numeros
plt.gca().xaxis.set_major_formatter("${x:1.0f}")
plt.legend()
plt.tight_layout()
plt.show()
for row in lg:
    for lang in row.split(";"):
        allLanguages.append(lang)

allLanguages = list(set(allLanguages))
print(allLanguages.sort())
