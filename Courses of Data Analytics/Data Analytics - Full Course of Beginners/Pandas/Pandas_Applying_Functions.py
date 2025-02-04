import pandas as pd
from datasets import load_dataset


dataset = load_dataset("lukebarousse/data_jobs")
df = dataset["train"].to_pandas()
df["job_posted_date"] = pd.to_datetime(df["job_posted_date"])

filtro = df[pd.notna(df["salary_year_avg"])]["salary_year_avg"]

print(filtro)