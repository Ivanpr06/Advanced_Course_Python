import pandas as pd
from datasets import load_dataset
import ast
from matplotlib import pyplot as plt
import seaborn as sns

dataset = load_dataset("lukebarousse/data_jobs")
df = dataset["train"].to_pandas()
df["job_posted_date"] = pd.to_datetime(df["job_posted_date"])

# Elimina valores Nan (paso a paso en Pandas_Applying_Functions)
df["job_skills"] = df["job_skills"].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)

df_DA_US = df[(df["job_title_short"] == "Data Analyst") & (df["job_country"] == "United States")].copy()
df_DA_US = df_DA_US.dropna(subset=["salary_year_avg"])

df_DA_US = df_DA_US.explode("job_skills")
df_DA_US = df_DA_US[["salary_year_avg", "job_skills"]]
df_DA_US_group = df_DA_US.groupby("job_skills")["salary_year_avg"].agg(["count", "median"])

# Primera condición
df_DA_top_pay = df_DA_US_group.sort_values(by="median", ascending=False).head(10)
print(df_DA_top_pay)

# Segunda condición
df_DA_skills = df_DA_US_group.sort_values(by="count", ascending=False).head(10).sort_values(by="median", ascending=False)
print(df_DA_skills)

fig, ax = plt.subplots(2,1)
# Cambia el fondo
sns.set_theme(style="ticks")
# Usamos Seaborn
sns.barplot(data=df_DA_top_pay, ax=ax[0], x="median", y= df_DA_top_pay.index, hue="median", palette="dark:b_r")
ax[0].legend().remove()

# [::-1] Cambia la dirección de los valores (de más a menos)
#df_DA_top_pay[::-1].plot(kind="barh",y="median", ax=ax[0], legend=False)
ax[0].set_title("Top 10 Highest Paid Skills for Data Analysts")
ax[0].set_xlabel("")
ax[0].set_ylabel("")
ax[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${int(x / 1000)}K"))

# Usamos Seaborn
# Hue especifica donde queremos aplicar los cambios y palette elige el color (_r = invierte los colores) (mirar pagina web de Seaborn para más opciones)
sns.barplot(data=df_DA_skills, ax=ax[1], x="median", y= df_DA_skills.index, hue="median", palette="light:b")
ax[1].legend().remove()

#df_DA_skills[::-1].plot(kind="barh",y="median", ax=ax[1], legend=False)
# Iguala los valores de la x en ambos gráficos
ax[1].set_title("Top 10 Highest Demand Skills for Data Analysts")
ax[1].set_xlabel("Median Salary (USD)")
ax[1].set_ylabel("")
ax[1].set_xlim(ax[0].get_xlim())
ax[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${int(x / 1000)}K"))

fig.tight_layout()
plt.show()