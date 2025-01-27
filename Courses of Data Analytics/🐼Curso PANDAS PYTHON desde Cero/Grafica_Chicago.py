import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Datos/avocado.csv')
print(df.head())

def region():
    # Selecciona las diez primeras regiones
    print(df["region"][:10])

chicago = df[df["region"]=="Chicago"]
# print(chicago.head(15))

def ordenar(chicago):
    # Establece como índice Date
    chicago = chicago.set_index("Date")

    # Ordena la fecha de másd antiguo a más reciente
    chicago = chicago.sort_values(by="Date")

    print(chicago.head(15))


def grafico(chicago):
    # Muestras que queremos cojer
    MAX_SAMPLES = 100
    precio = chicago["AveragePrice"][:MAX_SAMPLES]
    cantidad = chicago["Total Volume"][:MAX_SAMPLES]

    plt.plot(precio, label="Precio Medio")
    plt.plot(cantidad, label="Volumen Total")

    plt.title("Precio de los aguacates vs tiempo")
    # Legenda
    plt.xlabel("Fecha")
    plt.xticks(rotation=90)
    plt.ylabel("Precio en $")
    plt.legend()
    # Acceder al gráfico
    plt.show()

grafico(chicago)