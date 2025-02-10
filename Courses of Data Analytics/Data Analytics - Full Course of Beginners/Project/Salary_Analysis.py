import matplotlib
import pandas as pd
from datasets import load_dataset
import ast
from matplotlib import pyplot as plt
import seaborn as sns
matplotlib.use("TkAgg")

dataset = load_dataset("lukebarousse/data_jobs")
df = dataset["train"].to_pandas()
df["job_posted_date"] = pd.to_datetime(df["job_posted_date"])

# Elimina valores Nan (paso a paso en Pandas_Applying_Functions)
df["job_skills"] = df["job_skills"].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)

def Box_Salary_Analysis(df):
    df_US = df[(df["job_country"] == "United States")].dropna(subset=["salary_year_avg"])
    job_titles = df_US["job_title_short"].value_counts().index[:6].tolist()
    #print(job_titles)

    df_US_top6 = df_US[df_US["job_title_short"].isin(job_titles)]
    # Ordenamos los valores
    job_order = df_US_top6.groupby("job_title_short")["salary_year_avg"].median().sort_values(ascending=False).index

    sns.boxplot(data=df_US_top6, x="salary_year_avg", y="job_title_short", order=job_order)
    plt.xlabel("Salary Distribution in the United States")
    plt.ylabel("Yearly Salary ($USD)")

    ax = plt.gca()
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${int(x / 1000)}K"))
    plt.xlim(0, 600000)
    plt.show()
#Box_Salary_Analysis(df)

def Most_Paid_VS_Most_Median(df):
    df_DA_US = df[(df["job_title_short"] == "Data Analyst") & (df["job_country"] == "United States")].copy()
    df_DA_US = df_DA_US.dropna(subset=["salary_year_avg"])

    df_DA_US = df_DA_US.explode("job_skills")
    df_DA_US = df_DA_US[["salary_year_avg", "job_skills"]]
    #print(df_DA_US)

    df_DA_top_pay = df_DA_US.groupby("job_skills")["salary_year_avg"].agg(["count", "median"]).sort_values(by="median", ascending=False)
    df_DA_top_pay = df_DA_top_pay.head(10)
    #print(df_DA_top_pay)

    df_DA_skills = df_DA_US.groupby("job_skills")["salary_year_avg"].agg(["count", "median"]).sort_values(by="count", ascending=False)
    df_DA_skills = df_DA_skills.head(10).sort_values(by="median", ascending=False)
    #print(df_DA_skills)

    fig, ax = plt.subplots(2,1)
    # Cambia el fondo
    sns.set_theme(style="ticks")
    # Usamos Seaborn
    sns.barplot(data=df_DA_top_pay, ax=ax[0], x="median", y= df_DA_top_pay.index, hue="median", palette="coolwarm_r")
    ax[0].legend().remove()

    # [::-1] Cambia la dirección de los valores (de más a menos)
    #df_DA_top_pay[::-1].plot(kind="barh",y="median", ax=ax[0], legend=False)
    ax[0].set_title("Top 10 Highest Paid Skills for Data Analysts")
    ax[0].set_xlabel("")
    ax[0].set_ylabel("")
    ax[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${int(x / 1000)}K"))

    # Usamos Seaborn
    # Hue especifica donde queremos aplicar los cambios y palette elige el color (_r = invierte los colores) (mirar pagina web de Seaborn para más opciones)
    sns.barplot(data=df_DA_skills, ax=ax[1], x="median", y= df_DA_skills.index, hue="median", palette="coolwarm_r")
    ax[1].legend().remove()

    #df_DA_skills[::-1].plot(kind="barh",y="median", ax=ax[1], legend=False)
    # Iguala los valores de la x en ambos gráficos
    ax[1].set_title("Top 10 Highest Demand Skills for Data Analysts")
    ax[1].set_xlabel("Median Salary (USD)")
    ax[1].set_ylabel("")
    ax[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${int(x / 1000)}K"))

    fig.tight_layout()
    plt.show()
Most_Paid_VS_Most_Median(df)