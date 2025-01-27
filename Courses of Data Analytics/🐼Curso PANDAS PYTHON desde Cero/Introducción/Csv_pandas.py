import pandas as pd

# Index_col especifica el dato que queremos que sea indice
df = pd.read_csv("pandas.csv", index_col="hero")
# Head imprime las 5 primeras líneas, el numero especifica cuantas líneas quieres
# print(df.head(1))
print(df)