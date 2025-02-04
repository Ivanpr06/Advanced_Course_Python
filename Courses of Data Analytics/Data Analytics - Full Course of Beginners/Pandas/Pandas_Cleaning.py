import  pandas as pd
from datasets import load_dataset

# Cargar un datos
dataset = load_dataset("lukebarousse/data_jobs")
# Convertir datos para pandas (se puede hacer con más cosas)
df = dataset["train"].to_pandas()

print(df.info())
# Convertimos un objeto en una fecha
date = pd.to_datetime(df.job_posted_date)
print(date)

print(df.info())

ordenar = df.sort_values(by="job_posted_date", ascending=False)
print(ordenar)

# Elimina una columna, con axis especificamos su posición
eliminar = df.drop(labels="salary_hour_avg", axis=1)
print(eliminar)

# Con el dropna elinima las filas que tenga como dato Nan
# Con el inplace se asegura de realizar los cambios en el DataFrame original
nan = df.dropna(subset="salary_year_avg", inplace=True)
print(nan)