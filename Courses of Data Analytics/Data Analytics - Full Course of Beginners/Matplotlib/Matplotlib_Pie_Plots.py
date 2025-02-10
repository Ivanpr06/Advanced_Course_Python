import pandas as pd
from datasets import load_dataset
import ast
from matplotlib import pyplot as plt

# Recomendable usar Pie para cuando haya menos de 4 valores
dataset = load_dataset("lukebarousse/data_jobs")
df = dataset["train"].to_pandas()
df["job_posted_date"] = pd.to_datetime(df["job_posted_date"])

# Elimina valores Nan (paso a paso en Pandas_Applying_Functions)
df["job_skills"] = df["job_skills"].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)

def Trabajo_Casa():
    # Startangle regula el punto de inicio, Autopct pone los valores de cada segmento (%1.1f = aproxima, %% pone %)
    df["job_work_from_home"].value_counts().plot(kind="pie", startangle=90, autopct="%1.1f%%")
    plt.title("Work from Home Status")
    plt.ylabel("")
    plt.show()
#Trabajo_Casa()

def Multi_Pie():
    fig, ax = plt.subplots(1, 3)

    dict_column = {
        "job_work_from_home": "Work from Home",
        "job_no_degree_mention": "Job Degree Req",
        "job_health_insurance": "Health Insurance Offered"
    }
    # Enumerate crea índices en los valores, .items() devuelve los valores de un diccionario en una tupla
    for i, (column, title) in enumerate(dict_column.items()):
        # Con labels establecxes los valores, primero se pone el mas predominante
        ax[i].pie(df[column].value_counts(), startangle=90, autopct="%1.1f%%", labels=["False", "True"])
        ax[i].set_title(title)
    plt.show()
#Multi_Pie()