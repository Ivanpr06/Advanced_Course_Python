import ast
import pandas as pd
from datasets import load_dataset
import matplotlib
from matplotlib.ticker import PercentFormatter
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from adjustText import adjust_text
import seaborn as sns


dataset = load_dataset("lukebarousse/data_jobs")
df = dataset["train"].to_pandas()
df["job_posted_date"] = pd.to_datetime(df["job_posted_date"])

# Elimina valores Nan (paso a paso en Pandas_Applying_Functions)
df["job_skills"] = df["job_skills"].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)

df_DA_US = df[(df["job_title_short"] == "Data Analyst") & (df["job_country"] == "United States")].copy()
df_DA_US = df_DA_US.dropna(subset=["salary_year_avg"])

df_DA_US_exploted = df_DA_US.explode("job_skills")
df_DA_US_exploted = df_DA_US_exploted[["salary_year_avg", "job_skills"]]
#print(df_DA_US_exploted)

df_DA_skills = df_DA_US_exploted.groupby("job_skills")["salary_year_avg"].agg(["count", "median"]).sort_values(by="count", ascending=False)
df_DA_skills = df_DA_skills.rename(columns={"count": "skill_count", "median": "median_salary"})
#print(df_DA_skills)

DA_job_count = len(df_DA_US)
df_DA_skills["skill_percent"] = df_DA_skills["skill_count"] / DA_job_count * 100
#print(df_DA_skills)

skill_percent = 5
df_DA_skills_high_demand = df_DA_skills[df_DA_skills["skill_percent"] > skill_percent]
#print(df_DA_skills_high_demand)

df_DA_skills_high_demand.plot(kind="scatter", x="skill_percent", y="median_salary")

texts = []
for i, text in enumerate(df_DA_skills_high_demand.index):
    texts.append(plt.text(df_DA_skills_high_demand["skill_percent"].iloc[i], df_DA_skills_high_demand["median_salary"].iloc[i], text))

adjust_text(texts, arrowprops=dict(arrowstyle="->"), color="gray", lw=1)

plt.xlabel("Percent of Data Analyst Jobs")
plt.ylabel("Median Salary")
plt.title("Most Optimal Skills for Data Analyst in the US")

ax = plt.gca()
ax.yaxis.set_major_locator(plt.FuncFormatter(lambda y, pos: f"${int(y/1000)}K"))
ax.yaxis.set_major_formatter(PercentFormatter(decimals=0))

plt.tight_layout()
plt.show()