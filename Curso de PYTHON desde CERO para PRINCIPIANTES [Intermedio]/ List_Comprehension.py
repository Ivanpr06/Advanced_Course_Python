mi_lista_original = [1, 2, 3, 4, 5, 6, 7]

rango = range(8)
print(list(rango))

mi_lista = [i + 2 for i in range(8)]
print(mi_lista)

mi_lista = [i * 2 for i in range(8)]
print(mi_lista)

mi_lista = [i * i for i in range(8)]
print(mi_lista)

def sumar_cinco(numero):
    return numero + 5

mi_lista = [sumar_cinco(i) for i in range(8)]
print(mi_lista)