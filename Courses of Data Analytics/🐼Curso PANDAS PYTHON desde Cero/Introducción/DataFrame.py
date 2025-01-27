import pandas as pd
from numpy.ma.extras import column_stack


def diccionario1():
    personas ={
        "Nombre": ["Juanjo", "Manolo", "Paco"],
        "Edad": [27,56,42],
        "Pais": ["España", "México", "Argentina"]
    }

    df = pd.DataFrame(personas)
    print(df)

    
def diccionario2():
    marcas = [
        "Audi",
        "Mercedes",
        "BMW",
        "Mercedes"
    ]
    precio = [
        20e3,
        30e3,
        40e3,
        25e3
    ]
    disponibilidad = [
        True,
        False,
        False,
        True
    ]

    diccionario={
        "Marca":marcas,
        "Precio":precio,
        "Disponibilidad":disponibilidad
    }

    print(pd.DataFrame(diccionario))

def lista1():
    # 1ºMétodo
    columna = ["Marca", "Precio","Disponibilidad"]
    cocheA = ["Mercedes", 10e3, True]
    cocheB = ["BMW", 20e3, False]

    print(pd.DataFrame([cocheA,cocheB], columns=columna))

def lista2():
    # 2º Método
    marcas=[
        "Audi",
        "Mercedes",
        "BMW",
        "Mercedes"
    ]
    precio=[
        20e3,
        30e3,
        40e3,
        25e3
    ]
    disponibilidad=[
        True,
        False,
        False,
        True
    ]
    # Zip va cogiendo los primeros datos de las diferentes listas
    df = pd.DataFrame(
        list(zip(marcas, precio, disponibilidad)),
        columns =["marca", "precio", "disponibilidad"]
    )
    print(df)

