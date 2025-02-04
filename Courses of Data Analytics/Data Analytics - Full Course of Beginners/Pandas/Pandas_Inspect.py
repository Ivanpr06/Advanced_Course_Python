from datasets import load_dataset

# Cargar un datos
dataset = load_dataset("lukebarousse/data_jobs")
# Convertir datos para pandas (se puede hacer con más cosas)
df = dataset["train"].to_pandas()

# Imprime las 5 primeros filas (se puede especificar con un número)
print(df.head())

# Especificamos busqueda, si son varios valores hay que ponerlos en una lista
print(df[["job_title_short", "job_location"]].head(10))

# Especificar busqueda por su id o tambien se pueden pasar nombres de las columnas (para elegir varios valores ponemos primero fila y despues columna)
use_iloc = df.iloc[90:100, 0:2]
print(use_iloc)

# Filtrar datos
data_analyst = df[(df.job_title_short == "Data Analyst") & (df.salary_year_avg > 100000)]
print(data_analyst)

# Imprime informacion de las columnas
print(df.info())

# Calcula los datos numericos
print(df.describe())