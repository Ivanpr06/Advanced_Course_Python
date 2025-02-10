import pandas as pd
from datasets import load_dataset
import ast
from matplotlib import pyplot as plt

dataset = load_dataset("lukebarousse/data_jobs")
df = dataset["train"].to_pandas()
df["job_posted_date"] = pd.to_datetime(df["job_posted_date"])

# Elimina valores Nan (paso a paso en Pandas_Applying_Functions)
df["job_skills"] = df["job_skills"].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)

df_DA = df[df["job_title_short"] == "Data Analyst"].copy()

df_DA["job_posted_month_no"] = df_DA["job_posted_date"].dt.month

df_DA_explode = df_DA.explode("job_skills")
# print(df_DA_explode)

# Cuenta la cantidad de trabajo en cada mes
df_DA_pivot = df_DA_explode.pivot_table(index="job_posted_month_no", columns="job_skills", aggfunc="size", fill_value=0)
# Crea una fila donde suma toda la cantidad de trabajo en cada mes
df_DA_pivot.loc["Total"] = df_DA_pivot.sum()
# Ordena las columnas por la fila con más trabajos
df_DA_pivot = df_DA_pivot[df_DA_pivot.loc["Total"].sort_values(ascending=False).index]
# Eliminamos esta fila para que no salga en el gráfico
df_DA_pivot = df_DA_pivot.drop("Total")
# print(df_DA_pivot)

df_DA_pivot.iloc[:, 0:5].plot(kind="line", linewidth=4, linestyle=":", colormap="viridis", marker="o", markersize=5, figsize=(10, 5))
plt.title("Top 5 Skills for Data Analyst per Month")
plt.xlabel("Months")
plt.ylabel("Count")
plt.show()