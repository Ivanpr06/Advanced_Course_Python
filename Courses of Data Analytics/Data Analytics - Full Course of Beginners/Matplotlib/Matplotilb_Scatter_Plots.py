import ast
import  pandas as pd
from datasets import load_dataset
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from adjustText import adjust_text

# Cargar un datos
dataset = load_dataset("lukebarousse/data_jobs")
# Convertir datos para pandas (se puede hacer con más cosas)
df = dataset["train"].to_pandas()

df["job_posted_date"] = pd.to_datetime(df["job_posted_date"])
df["job_skills"] = df["job_skills"].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)

df = df[df["job_title_short"] == "Data Analyst"]

df_exploted = df.explode("job_skills")

skills_stats = df_exploted.groupby("job_skills").agg(skill_count=("job_skills", "count"), median_salary=("salary_year_avg", "median"))
skills_stats = skills_stats.sort_values("skill_count", ascending=False).head(10)
#print(skills_stats)

skills_stats.plot(kind="scatter", x="skill_count", y="median_salary")

texts = []
for i, text in enumerate(skills_stats.index):
    texts.append(plt.text(skills_stats["skill_count"].iloc[i], skills_stats["median_salary"].iloc[i], text))

adjust_text(texts, arrowprops=dict(arrowstyle="->"), color="gray", lw=1)

ax = plt.gca()
ax.yaxis.set_major_locator(plt.FuncFormatter(lambda y, pos: f"$int{int(y/100)}K"))
plt.xlabel("Count of Job Posting")
plt.ylabel("Median Salary")
plt.title("Salary VS Count of Job Posting for Top 10")
plt.tight_layout()
plt.show()