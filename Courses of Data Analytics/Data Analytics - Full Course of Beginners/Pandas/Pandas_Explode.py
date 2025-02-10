import pandas as pd
from datasets import load_dataset
import ast
from matplotlib import pyplot as plt

dataset = load_dataset("lukebarousse/data_jobs")
df = dataset["train"].to_pandas()
df["job_posted_date"] = pd.to_datetime(df["job_posted_date"])

# Elimina valores Nan (paso a paso en Pandas_Applying_Functions)
df["job_skills"] = df["job_skills"].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)

#print(df[["job_title_short","job_skills"]].head(5))

df_exploted = df.explode("job_skills")
#print(df_exploted)

# Contamos la cantidad de skill que hay pero en una Serie
skills_count = df_exploted.groupby(["job_title_short", "job_skills"]).size()
# Lo pasamos a un dataframe
df_skills_count = skills_count.reset_index(name="skill_count")
# Lo ordenamos de más a menos
df_skills_count = df_skills_count.sort_values(by="skill_count", ascending=False)
#print(df_skills_count)

job_title = "Data Analyst"
top_skills = 10
# Filtra el tipo de trabajo que queremos
df_skill_final = df_skills_count[df_skills_count["job_title_short"] == job_title].head(top_skills)
df_skill_final.plot(kind="barh", x="job_skills", y="skill_count")
# Cambia de posicion los valores en el gráfico (el de abajo ahora esta arriba)
plt.gca().invert_yaxis()
plt.title(f"Top {top_skills} Skills for {job_title}")
plt.xlabel("Job Posting Count")
plt.ylabel("Skill Count")
# Elimina la layenda
plt.legend().set_visible(False)
plt.show()
