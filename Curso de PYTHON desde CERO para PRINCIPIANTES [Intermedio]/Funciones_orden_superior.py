from functools import reduce

# Función Simple
def sumar_uno(valor):
    return valor + 1

def sumar_cinco(valor):
    return valor + 5

def sumar_y_anyade_uno(num1, num2, f_suma):
    return f_suma(num1 + num2)

# print(sumar_y_anyade_uno(5, 2, sumar_cinco))
# print(sumar_y_anyade_uno(5, 2, sumar_uno))

### Closures ###

def sumar_diez(valor_original):
    def anyadir(valor):
        return valor + 10 + valor_original
    return anyadir

anydir_closure = sumar_diez(1)
print(anydir_closure(5))

# Forma abreviada
print(sumar_diez(5)(1))


### Map = map nos permite aplicar una función sobre los items de un objeto iterable ###
numeros = [2, 5, 10, 21]

def multiplicar_por_dos(numero):
    return numero * 2


print(list(map(multiplicar_por_dos, numeros)))
print(list(map(lambda numero: numero * 2, numeros)))

### Filter ###
def filter_mayor_diez(numero):
    if numero > 10:
        return True
    else:
        return False

print(list(filter(filter_mayor_diez, numeros)))
print(list(filter(lambda numero: numero > 10, numeros)))

### Reduce ###

def sumar(num1, num2):
    return num1 + num2

print(reduce(sumar, numeros))