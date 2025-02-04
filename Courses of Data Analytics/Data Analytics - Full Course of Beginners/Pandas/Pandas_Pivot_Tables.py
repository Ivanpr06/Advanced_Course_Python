import  pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt

# Cargar un datos
dataset = load_dataset("lukebarousse/data_jobs")
# Convertir datos para pandas (se puede hacer con más cosas)
df = dataset["train"].to_pandas()

df["job_posted_date"] = pd.to_datetime(df["job_posted_date"])


# Pivot_table se utiliza para reorganizar y resumir datos en un formato tabular más útil.
# Aggfunc define qué función de agregación se aplicará a los datos al crear la tabla pivote(size no hace nada pero se puede hacer operaciones como sumar o restar entre otras)
print(df.pivot_table(values="salary_year_avg", index="job_country",columns="job_title_short", aggfunc="median"))

def grafica_paises_mas_trabajo_y_salario_medio():
    top_paises = df["job_country"].value_counts().head(6).index

    # Creamos la tabla de datos
    df_salario_pais = df.pivot_table(values="salary_year_avg", index="job_country", columns="job_title_short", aggfunc="median")
    # Filtramos los paises con más trabajo en nuestra tabla
    df_salario_pais = df_salario_pais.loc[top_paises]
    # Especificamos trabajos
    trabajos = ['Data Analyst', 'Data Engineer', 'Data Scientist']
    # Filtramos los trabajos en nuesstra tabla
    df_salario_pais = df_salario_pais[trabajos]
    df_salario_pais.plot(kind="bar")
    plt.ylabel("Salario Medio $")
    plt.xlabel("")
    plt.title("Salario Medio Por Paises Con Más Trabajo")
    plt.xticks(rotation=45, ha="right")
    plt.show()