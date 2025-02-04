import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset

dataset = load_dataset("lukebarousse/data_jobs")
df = dataset["train"].to_pandas()
df["job_posted_date"] = pd.to_datetime(df["job_posted_date"])

salario = df.groupby("job_title_short")["salary_year_avg"].median().sort_values()

salario.plot(kind="barh")
plt.xlabel("Salario $")
plt.ylabel("Trabajos")
plt.title("Salario Medio por Trabajos")
plt.show()
