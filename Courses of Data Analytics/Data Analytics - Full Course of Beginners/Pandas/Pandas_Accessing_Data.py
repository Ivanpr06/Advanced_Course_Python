import pandas as pd
from datasets import load_dataset

dataset = load_dataset("lukebarousse/data_jobs")
df = dataset["train"].to_pandas()
df["job_posted_date"] = pd.to_datetime(df["job_posted_date"])

filtro = df.iloc[0:10]
print(filtro)

filtro2 = df.loc[:, "salary_rate":"salary_hour_avg"].dropna(subset=["salary_rate"])
print(filtro2)