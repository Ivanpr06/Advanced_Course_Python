import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset

def grafico_simple():
    x = [1,2,3,4]
    y = [1,2,3,4]
    plt.plot(x,y)
    plt.show()

dataset = load_dataset("lukebarousse/data_jobs")
df = dataset["train"].to_pandas()
df["job_posted_date"] = pd.to_datetime(df["job_posted_date"])

def grafica_tiempo_trabajado():
    # Pasamos el tempo a meses para que sea más facil de calcular
    df["job_posted_date"] = df["job_posted_date"].dt.month
    contar = df.job_posted_date.value_counts()
    contar = contar.sort_index()

    # Plot te hace un gráfico de línea
    # Contar.index accede a los valores
    plt.plot(contar.index, contar)
    plt.show()
#grafica_tiempo_trabajado()

def uso_de_series():
    serie = pd.Series([10, 20, 30, 40, 50], index=["a", "b", "c", "d", "e"])
    index = serie.index
    values = serie.values
    print(serie)
#uso_de_series()

def grafico_cantidad_trabajadores():
    job_counts = df.job_title_short.value_counts()
    job_counts = job_counts.sort_values(ascending=True)
    # Bar hace un gráfico de barras verical
    # Barh hace un gráfico de barras horizontal

    # plt.bar(job_counts.index, job_counts)
    job_counts.plot(kind='bar') # Abrebiada
    plt.title("Posting by Job Title")
    plt.ylabel("Count")
    plt.xlabel("Job Title")
    plt.xticks(rotation=45, ha="right")
    plt.show()
#grafico_cantidad_trabajadores()
