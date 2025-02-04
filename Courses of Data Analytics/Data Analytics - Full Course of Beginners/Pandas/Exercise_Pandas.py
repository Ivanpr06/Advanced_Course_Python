import  pandas as pd
from datasets import load_dataset

# Cargar un datos
dataset = load_dataset("lukebarousse/data_jobs")
# Convertir datos para pandas (se puede hacer con más cosas)
df = dataset["train"].to_pandas()

df["job_posted_date"] = pd.to_datetime(df["job_posted_date"])

df["job_country"].value_counts().head(20)
#print(df)

spain = df["job_country"].isin(["Spain"]).any()
#print(spain)

## Ejercicio

sp_jobs = df[df["job_country"] == "Spain"]
sp_jobs = sp_jobs[sp_jobs["salary_year_avg"].notna()]
sp_jobs = sp_jobs.groupby("job_title_short")["salary_year_avg"].agg(["median", "min", "max", "count"]).sort_values(by="median", ascending=False)
print(sp_jobs)