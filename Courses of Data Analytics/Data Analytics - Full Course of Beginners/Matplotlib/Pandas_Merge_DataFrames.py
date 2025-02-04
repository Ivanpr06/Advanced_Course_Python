import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset

dataset = load_dataset("lukebarousse/data_jobs")
df = dataset["train"].to_pandas()
df["job_posted_date"] = pd.to_datetime(df["job_posted_date"])

df_US = df[df["job_country"] == "United States"].copy()
# Strftime te da acceso a elegir una manera del representar el tiempo, con %B dice el nombre del mes
df_US["job_posted_month"] = df_US["job_posted_date"].dt.strftime("%B")

#Size cuenta las veces que se repite
df_US_pivot = df_US.pivot_table(index="job_posted_month", columns="job_title_short", aggfunc="size")

# Extraemos el numero del mes creando una nueva columna llamada month_no
df_US_pivot.reset_index(inplace=True)
df_US_pivot["month_no"] = pd.to_datetime(df_US_pivot["job_posted_month"], format="%B").dt.month
# Crearemos esta columna para poder ordenar los meses numericamente y después la eliminaremos
df_US_pivot.sort_values("month_no", inplace=True)
df_US_pivot.set_index("job_posted_month", inplace=True)
df_US_pivot.drop(columns="month_no", inplace=True)

datos2 = pd.read_csv("https://lukeb.co/software_csv", index_col="job_posted_month")
# Unimos ambas tablas
df_US_Merge = df_US_pivot.merge(datos2, on="job_posted_month")
#print(df_US_pivot)

top_5 = (df_US_Merge.sum().sort_values(ascending=False)
         .head().index.tolist())
df_US_Merge[top_5].plot(kind="line")
plt.title("Top 5 Job Posted in the US")
plt.xlabel("2023")
plt.ylabel("Job Count")
plt.legend()
plt.show()