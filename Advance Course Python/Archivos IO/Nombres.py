# Forma normal
# nombres = []
#
# for _ in range(3):
#     nombre = input("Cual es tu nombre? : ")
#     nombres.append(nombre)
#
# for nombre in sorted(nombres):
#     print(f"Hola, {nombre}")

# Forma con open (Guarda datos)
def ej_1():
    nombre = input("Cual es tu nombre? : ")

    # file = open("nombres.txt", "a") # a = se guarda siempre / w = se va eliminando
    # file.write(f"{nombre}\n")
    # file.close()
    # Simplificado
    with open("nombres.txt","a") as file:
        file.write(nombre+"\n")

def ej_2():
    # Largo
    # with open("nombres.txt","r") as file:
    #     lineas = file.readlines() # Imprime file
    #
    # for linea in lineas:
    #     print(f"Hola, {linea.rstrip()}") # rstrip = Elimina salto de línea o espacios

    # Simplificado
    with open("nombres.txt","r") as file:
        for linea in file:
            print(f"Hola, {linea.rstrip()}")

def ej_3():
    # Largo
    # nombres = []
    # with open("nombres.txt","r") as file:
    #     for linea in file:
    #         nombres.append(linea.rstrip())
    #
    # for nombre in sorted(nombres):
    #     print(f"Hola, {nombre}")

    # Simplificado
    with open("nombres.txt","r") as file:
        for linea in sorted(file):
            print(f"Hola, {linea.rstrip()}")
