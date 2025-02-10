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

df_US = df[df["job_country"] == "United States"]

df_skills = df_US.explode("job_skills")
skills_count = df_skills.groupby(["job_skills", "job_title_short"]).size()
df_skills_count = skills_count.reset_index(name="skill_count")
df_skills_count.sort_values(by="skill_count", ascending=False, inplace=True)
df_US["job_title_short"].value_counts().reset_index(name="jobs_total")

# Calculamos el total de trabajos para cada skill
df_job_title_count = df_US["job_title_short"].value_counts().reset_index(name="jobs_total")
df_skills_perc = pd.merge(df_skills_count, df_job_title_count, how="left", on="job_title_short")
df_skills_perc["skill_percent"] = (df_skills_perc["skill_count"] / df_skills_perc["jobs_total"]) *100
#print(df_skills_perc.head())

job_titles = df_skills_count["job_title_short"].unique().tolist()
job_titles = sorted(job_titles[:3])

fig, ax = plt.subplots(len(job_titles),1)
sns.set_theme(style="ticks")
for i, job_title in enumerate(job_titles):
    df_plot = df_skills_perc[df_skills_perc["job_title_short"] == job_title].head(5)
    sns.barplot(data=df_plot, x="skill_percent", y="job_skills", ax=ax[i], hue="skill_count", palette="coolwarm_r")
    ax[i].set_title(job_title)
    ax[i].set_ylabel("")
    ax[i].set_xlabel("")
    ax[i].legend().set_visible(False)
    ax[i].set_xlim(0, 80)

    for n, v in enumerate(df_plot["skill_percent"]):
        ax[i].text(v + 1, n, f"{v:.0f}%", va="center")

    ax[i].set_xticks([])

fig.suptitle("Likelihood of Skills Requested in US Job Posting", fontsize=15, fontweight='bold')
fig.tight_layout(h_pad=0.5)
plt.show()
