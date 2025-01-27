from cProfile import label

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Datos/avocado.csv")
atlanta = df[df["region"] == "Atlanta"]

precio = atlanta["AveragePrice"]
# Ostilaciones menos distantes
precioPromediado = precio.rolling(25).mean()

volumen = atlanta["Total Volume"]

bolsasAguacates = atlanta["Total Bags"]

sbolsas = atlanta["Small Bags"]
lbolsas = atlanta["Large Bags"]
xbolsas = atlanta["XLarge Bags"]

# 221 significa : 2 = fila , 2 = columna , 1 = eje
plt.subplots(221)
plt.title("Precio Aguacate")
plt.plot(precio, label="Precio", color="green")
plt.plot(precioPromediado, label="Precio Promediado", color="orange")
plt.legend()

plt.subplots(222)
plt.title("Volumen Aguacate")
plt.plot(volumen, label="Volumen", color="red")
plt.legend()

plt.subplots(223)
plt.title("Bolsas Aguacate")
plt.plot(bolsasAguacates, label="Bolsas Totales", color="blue")
plt.legend()

plt.subplots(224)
plt.title("Bolsas por Tamaño")
plt.plot(sbolsas, label="Bolsas S", color="black")
plt.plot(lbolsas, label="Bolsas L", color="cyan")
plt.plot(xbolsas, label="Bolsas XL", color="yellow")
plt.legend()

plt.tight_layout()
plt.show()