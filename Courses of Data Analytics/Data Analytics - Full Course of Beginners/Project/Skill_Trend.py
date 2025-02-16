import pandas as pd
from datasets import load_dataset
import ast
from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib.ticker import PercentFormatter

dataset = load_dataset("lukebarousse/data_jobs")
df = dataset["train"].to_pandas()
df["job_posted_date"] = pd.to_datetime(df["job_posted_date"])

# Elimina valores Nan (paso a paso en Pandas_Applying_Functions)
df["job_skills"] = df["job_skills"].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)

df_DA_US = df[(df["job_title_short"] == "Data Analyst") & (df["job_country"] == "United States")].copy()
df_DA_US["job_posted_month_no"] = df_DA_US["job_posted_date"].dt.month

df_DA_US_explode = df_DA_US.explode("job_skills")
df_DA_US_pivot = df_DA_US_explode.pivot_table(index="job_posted_month_no", columns="job_skills", aggfunc="size", fill_value=0)
df_DA_US_pivot.loc["Total"] = df_DA_US_pivot.sum()

df_DA_US_pivot = df_DA_US_pivot[df_DA_US_pivot.loc["Total"].sort_values(ascending=False).index]
df_DA_US_pivot = df_DA_US_pivot.drop("Total")
#print(df_DA_US_pivot)

# Calcula el porcentaje
DA_totals = df_DA_US.groupby("job_posted_month_no").size()
df_DA_US_percent = df_DA_US_pivot.div(DA_totals/100, axis=0)

# Transforma los meses inicialmente en numeros a letras
df_DA_US_percent = df_DA_US_percent.reset_index()
df_DA_US_percent["job_posted_month"] = df_DA_US_percent["job_posted_month_no"].apply(lambda x: pd.to_datetime(x, format="%m").strftime("%b"))
df_DA_US_percent = df_DA_US_percent.set_index("job_posted_month")
df_DA_US_percent = df_DA_US_percent.drop(columns="job_posted_month_no")

# Saca 5 valores
df_plot = df_DA_US_percent.iloc[:, :5]
sns.lineplot(data=df_plot, dashes=False, palette="tab10")
sns.set_theme(style="ticks")
# Elimina el marco derecho
sns.despine()

plt.title("Trending Top Skills for Data Analysts in the US")
plt.ylabel("Likelihood in Job Posting")
plt.xlabel("2023")
plt.legend().remove()

# Convierte el eje y en porcentaje
ax = plt.gca()
ax.yaxis.set_major_formatter(PercentFormatter(decimals=0))

for i in range(5):
    plt.text(11.5, df_plot.iloc[-1, i], df_plot.columns[i])
plt.show()