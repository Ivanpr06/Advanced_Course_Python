import pandas as pd
from datasets import load_dataset
import ast


dataset = load_dataset("lukebarousse/data_jobs")
df = dataset["train"].to_pandas()
df["job_posted_date"] = pd.to_datetime(df["job_posted_date"])

df_salary = df[pd.notna(df["salary_year_avg"])].copy()

def projected_salary(salary):
    return salary * 1.03

# Creamos una nueva columna y donde aplicaremos el método anterior (hay maneras más simples)
df_salary["salary_year_inflated"] = df_salary["salary_year_avg"].apply(projected_salary)
#print(df_salary[["salary_year_avg", "salary_year_inflated"]])


def clean_list(skill_list):
    if pd.notna(skill_list):
        return ast.literal_eval(skill_list)


df[pd.isna(df["job_skills"])]
df["job_skills"] = df["job_skills"].apply(clean_list)
print(df["job_skills"][6])