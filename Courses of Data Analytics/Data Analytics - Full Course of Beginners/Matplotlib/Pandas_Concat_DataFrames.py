import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset

dataset = load_dataset("lukebarousse/data_jobs")
df = dataset["train"].to_pandas()
df["job_posted_date"] = pd.to_datetime(df["job_posted_date"])

df["job_posted_month"] = df["job_posted_date"].dt.strftime("%b")

# Unique no repite los valores
months = df["job_posted_month"].unique()

# Hemos creado este diccionario para saber que trabajos hubo en cada mes
dict_month = {month: df[df["job_posted_month"] ==  month] for month in months}
# Creamos un dataframe con los datos del diccionario
df_q1 = pd.concat([dict_month["Jan"], dict_month["Feb"], dict_month["Mar"]], ignore_index=True)

df_q1["job_posted_month"].value_counts().plot(kind="bar")
plt.show()

