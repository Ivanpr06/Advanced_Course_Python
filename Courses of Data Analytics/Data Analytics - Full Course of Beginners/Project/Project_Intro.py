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

df_DA_US = df[(df["job_title_short"] == "Data Analyst") & (df["job_country"] == "United States")].copy()

def USA_Job_Location(df_DA_US):
    # to_frame convierte el estilo de la serie en un dataframe
    df_plot = df_DA_US["job_location"].value_counts().head(10).to_frame()
    #print(df_plot)

    sns.set_theme(style="whitegrid")
    sns.barplot(data=df_plot, x="job_location", y="count", hue="count", palette="coolwarm_r", legend=False)
    plt.title("Counts of Job Locations for Data Analyst in the US")
    plt.xlabel("")
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Number of Jobs")
    plt.tight_layout()

    plt.show()

#USA_Job_Location(df_DA_US)

def USA_Job_Plus(df_DA_US):
    dict_column = {
        "job_work_from_home": "Work from Home",
        "job_no_degree_mention": "Job Degree Req",
        "job_health_insurance": "Health Insurance Offered"
    }

    fig, ax = plt.subplots(1, 3)
    fig.set_size_inches(12, 5)

    # Enumerate crea indices en los valores, .items() devuelve los valores de un diccionario en una tupla
    for i, (column, title) in enumerate(dict_column.items()):
        # Con labels establecxes los valores, primero se pone el mas predominante
        ax[i].pie(df_DA_US[column].value_counts(), startangle=90, autopct="%1.1f%%", labels=["False", "True"])
        ax[i].set_title(title)
    plt.show()

#USA_Job_Plus(df_DA_US)

def USA_Companies(df_DA_US):
    # to_frame convierte el estilo de la serie en un dataframe
    df_plot = df_DA_US["company_name"].value_counts().head(10).to_frame()
    #print(df_plot)

    sns.set_theme(style="whitegrid")
    sns.barplot(data=df_plot, x="company_name", y="count", hue="count", palette="coolwarm_r", legend=False)
    plt.title("Counts of Job Locations for Data Analyst in the US")
    plt.xlabel("")
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Number of Jobs")
    plt.tight_layout()

    plt.show()

#USA_Companies(df_DA_US)





