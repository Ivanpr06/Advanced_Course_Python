import re

nombre = input("Cual es tu nombre? : ").strip()
# Muy Simple
# if "," in nombre:
#     ultimo ,primero = nombre.split(",")
#     nombre = f"{primero} {ultimo}"
# print(f"Hola, {nombre}")

# Implementando re
if validar := re.search(r"^(.+), *(.+)$", nombre):
    nombre = validar.group(2) + " " + validar.group(1)
print(f"Hola, {nombre}")

