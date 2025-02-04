import  pandas as pd
from datasets import load_dataset

# Cargar un datos
dataset = load_dataset("lukebarousse/data_jobs")
# Convertir datos para pandas (se puede hacer con más cosas)
df = dataset["train"].to_pandas()

df["job_posted_date"] = pd.to_datetime(df["job_posted_date"])

print(df.describe())

# Cuenta la cantidad de datos que hay en una columna
print(df.count())

# Calcula la media de una columna (tiene que ser numerica)
media = df["salary_year_avg"].median()
print(media)

# Enseña el valor más bajo
min = df["salary_year_avg"].min()
print(min)

# Busca los indices (en este caso del valor mínimo)
buscar_index = df["salary_year_avg"].idxmin()
print(buscar_index)

# Busca los datos de ese index
print(df.iloc[buscar_index])

contar_valores = df["job_title_short"].value_counts()
print(contar_valores)

# Encontrar el sueldo menor de cada trabajo
salarios_min = df.groupby("job_title_short")["salary_year_avg"].min()
print(salarios_min)

# Encontrar el sueldo medio de cada trabajo en cada país
salarios_medio = df.groupby(["job_title_short", "job_country"])[["salary_year_avg", "salary_hour_avg"]].median()
print(salarios_medio)

# Agg sirve para hacer muchas operaciones
todos_salarios = df.groupby("job_title_short")["salary_year_avg"].agg(["min", "max", "median"])
print(todos_salarios)