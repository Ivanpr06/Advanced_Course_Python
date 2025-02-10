import pandas as pd
from datasets import load_dataset
import ast
from matplotlib import pyplot as plt

dataset = load_dataset("lukebarousse/data_jobs")
df = dataset["train"].to_pandas()
df["job_posted_date"] = pd.to_datetime(df["job_posted_date"])

# Elimina valores Nan (paso a paso en Pandas_Applying_Functions)
df["job_skills"] = df["job_skills"].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)

fig, ax = plt.subplots(1,2)

df["job_title_short"].value_counts().plot(kind="bar", ax=ax[0])
df["job_schedule_type"].value_counts().head(3).plot(kind="bar", ax=ax[1])

fig.tight_layout()
#plt.show()

def top_skills(df):
    df_skills = df.copy()
    df_skills = df_skills.explode("job_skills")
    skills_count = df_skills.groupby([ "job_skills", "job_title_short"]).size()
    df_skills_count = skills_count.reset_index(name="skill_count")
    df_skills_count.sort_values(by="skill_count", ascending=False, inplace=True)

    job_titles = ["Data Scientist", "Data Engineer", "Data Analyst"]

    fig, ax = plt.subplots(3,1)
    for i, job_title in enumerate(job_titles):
        df_plot = df_skills_count[df_skills_count["job_title_short"] == job_title].head(5)
        df_plot.plot(kind="barh", x="job_skills", y="skill_count", ax=ax[i], title= job_title)
        ax[i].invert_yaxis()
        ax[i].set_ylabel("")
        ax[i].legend().set_visible(False)
        ax[i].set_xlim(0,120000)

    fig.suptitle("Counts of Top Skills in Job Postings", fontsize=15, fontweight='bold')
    fig.tight_layout()
    plt.show()
#top_skills(df)