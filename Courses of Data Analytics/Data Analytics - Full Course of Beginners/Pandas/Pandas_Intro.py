import pandas as pd

df = pd.read_csv("../Data/california_housing_test.csv")
print(df["total_bedrooms"])

# Seleciona un dato con su id
total = df.total_bedrooms[0]
print(total)

