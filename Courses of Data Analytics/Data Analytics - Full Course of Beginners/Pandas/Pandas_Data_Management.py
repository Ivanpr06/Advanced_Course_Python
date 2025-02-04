from datasets import load_dataset

# Cargar un datos
dataset = load_dataset("lukebarousse/data_jobs")
# Convertir datos para pandas (se puede hacer con más cosas)
df_original = dataset["train"].to_pandas()

# Copy sirve para no cambiar los valores de nuestra df original
df_altered = df_original.copy()

salario_medio = df_altered["salary_year_avg"].median()
print(salario_medio)

df_altered["salary_year_avg"] = df_altered["salary_year_avg"].fillna(salario_medio)
print(df_altered.loc[:5, "salary_year_avg"])

print(df_original.loc[:5, "salary_year_avg"])


