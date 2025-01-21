## SyntaxError
# Error = print "Hola Mundo"
print("Hola Mundo")

## NameError
# Error = print(nombre)
apellido = "Garcia"
print(apellido)

## IndexError
mi_lista = ["Python", "HTML5", "CSS"]
print(mi_lista[0])
print(mi_lista[1])
print(mi_lista[2])
# Error = print(mi_lista[3])

# ModulesNotFoundError
# Error = import maths
import math

# AttributeError
# Error = print(math.PI)
print(math.pi)

# KeyError
diccionario = {"nombre": "Manolo", "apellido": "Garcia", "edad": 31, "lenguaje": "Python"}
print(diccionario["nombre"])
# Error = print(diccionario["apelllido"])

# TypeError
# Error = print(mi_lista["apellido"])
print(mi_lista[::-1])


# ImportError
# Error = from math import PI
from math import pi
print(pi)

# ValueError
# Error = mi_int = int("10 Años")
mi_int = int(10)
print(type(mi_int))

# ZeroDivisionError
# Error = print(4/0)
print(4/2)