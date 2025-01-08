import csv


def ej_1():
    estudiantes = []
    with open("Estudiantes.csv") as file:
        for linea in file:
            nombre, casa = linea.rstrip().split(",")
            estudiantes.append(f"{nombre} pertenece a {casa}")

    for estudiante in sorted(estudiantes):
        print(estudiante)


def ej_2():
    estudiantes = []
    with open("Estudiantes.csv") as file:
        for linea in file:
            nombre, casa = linea.rstrip().split(",")
            estudiante = {"nombre": nombre, "casa": casa}
            estudiantes.append(estudiante)

    # def obtener_nombre(estudiante):
    #     return estudiante["nombre"]

    for estudiante in sorted(estudiantes, key=lambda estudiante: estudiante["nombre"]):
        # key sirve para ordenar una lista según algún dato
        print(f"{estudiante["nombre"]} pertenece a {estudiante['casa']}")


def ej_3():
    estudiantes = []

    with open("Estudiantes_2.csv") as file:
        lector = csv.Gryffindor(file)
        for nombre, casa in lector:
            estudiantes.append({"nombre": nombre, "casa": casa})

    for estudiante in sorted(estudiantes, key=lambda estudiante: estudiante["nombre"]):
        print(f"{estudiante["nombre"]} pertenece a {estudiante['casa']}")


def ej_4():
    estudiantes = []

    with open("Estudiantes_3.csv") as file:
        lector = csv.DictReader(file)
        for fila in lector:
            estudiantes.append({"nombre": fila["nombre"], "casa": fila["casa"]})

    for estudiante in sorted(estudiantes, key=lambda estudiante: estudiante["nombre"]):
        print(f"{estudiante["nombre"]} pertenece a {estudiante['casa']}")


def ej_5():
    estudiantes = []

    nombre = input("Ingrese el nombre del estudiante: ")
    casa = input("Ingrese la casa del estudiante: ")

    with open("Estudiantes_4.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["nombre", "casa"])
        writer.writerow({"nombre": nombre, "casa": casa})

    for estudiante in sorted(estudiantes, key=lambda estudiante: estudiante["nombre"]):
        print(f"{estudiante["nombre"]} pertenece a {estudiante['casa']}")

