import pandas as pd
from datasets import load_dataset
import ast
from matplotlib import pyplot as plt

dataset = load_dataset("lukebarousse/data_jobs")
df = dataset["train"].to_pandas()
df["job_posted_date"] = pd.to_datetime(df["job_posted_date"])

# Elimina valores Nan (paso a paso en Pandas_Applying_Functions)
df["job_skills"] = df["job_skills"].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)

def Box_Simple(df):
    df_DA_US = df[(df["job_title_short"] == "Data Analyst") & (df["job_country"] == "United States")].copy()
    df_DA_US = df_DA_US.dropna(subset=["salary_year_avg"])
    #print(df_DA_US["salary_year_avg"].sample(10))

    df_DA_US["salary_year_avg"].plot(kind="box", vert="False")
    plt.show()
#Box_Simple(df)

def Comparacion_Salario_Empleo():
    job_titles = ["Data Analyst", "Data Engineer", "Data Scientist"]
    df_US = df[(df["job_title_short"].isin(job_titles)) & (df["job_country"] == "United States")].copy()

    df_US = df_US.dropna(subset=["salary_year_avg"])
    job_list = [df_US[df_US["job_title_short"] == job_title]["salary_year_avg"] for job_title in job_titles]
    plt.boxplot(job_list, labels=job_titles, vert=False)
    plt.xlabel("Salary Distribution in the United States")
    plt.ylabel("Yearly Salary ($USD)")

    ax = plt.gca()
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${int(x/1000)}K"))
    plt.xlim(0, 600000)
    plt.show()
#Comparacion_Salario_Empleo()