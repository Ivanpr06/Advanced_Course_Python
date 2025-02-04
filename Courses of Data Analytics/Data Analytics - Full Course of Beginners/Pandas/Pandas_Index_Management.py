from datasets import load_dataset

# Cargar un datos
dataset = load_dataset("lukebarousse/data_jobs")
# Convertir datos para pandas (se puede hacer con más cosas)
df = dataset["train"].to_pandas()

df_usa = df[df["job_country"] == "United States"]
# Crea un nuevo indice (no elimina el anterior)
df_usa.reset_index(inplace=True)
#print(df_usa)

# Elimina el indice creado
#df_usa.set_index("job_index", inplace=True)
#print(df_usa)

median_pivot = df_usa.pivot_table(values="salary_year_avg", index="job_title_short", aggfunc=["median", "min", "max"])

median_pivot.sort_values(by="job_title_short", ascending=False)
# Ordena el indice en orden alfabetico
median_pivot.sort_index(inplace=True)
print(median_pivot)