from datasets import load_dataset

# Cargar un datos
dataset = load_dataset("lukebarousse/data_jobs")
# Convertir datos para pandas (se puede hacer con más cosas)
df = dataset["train"].to_pandas()

salario_medio_anyo = df["salary_year_avg"].median()
salario_medio_hora = df["salary_hour_avg"].median()

df_filled = df

# Rellenar los campos vacios
df_filled["salary_year_avg"] = df_filled["salary_year_avg"].fillna(salario_medio_anyo)
df_filled["salary_hour_avg"] = df_filled["salary_hour_avg"].fillna(salario_medio_hora)

filtro = df_filled.loc[:10, "salary_year_avg":"salary_hour_avg"]
print(filtro)

df_unique = df_filled
df_unique = df_unique.drop_duplicates()

print(f"Cantidad de columnas en el dataframe original: {len(df_filled)}")
print(f"Cantidad de Columnas no duplicadas: {len(df_unique)}")
print(f"Columnas eliminadas: {len(df_filled)-len(df_unique)}")

# Imprime un valor random, se puede pedir más sample(n)
# Random_state guarda los valores y no los altera
sample = df.sample(10, random_state=42)
print(sample)