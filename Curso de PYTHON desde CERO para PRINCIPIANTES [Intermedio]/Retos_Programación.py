# Ejercicos sacados de https://retosdeprogramacion.com/ejercicios/

"""
 Escribe un programa que muestre por consola (con un print) los
 números de 1 a 100 (ambos incluidos y con un salto de línea entre
 cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def FizzBuzz():
    for i in range(1,101):
        if i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(i)

"""
 Escribe una función que reciba dos palabras (String) y retorne
 verdadero o falso (Bool) según sean o no anagramas.
 - Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
 - NO hace falta comprobar que ambas palabras existan.
 - Dos palabras exactamente iguales no son anagrama.
 """

def Anagrama(palabra1, palabra2):
    if palabra1.lower() == palabra2.lower():
        return False
    elif sorted(palabra1.lower()) == sorted(palabra2.lower()):
        return True
    else:
        return False
# print(Anagrama("Roma", "Amor"))


"""
 Escribe un programa que imprima los 50 primeros números de la sucesión
 de Fibonacci empezando en 0.
 - La serie Fibonacci se compone por una sucesión de números en
 la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

def Fibonacci(lista):
    anterior = 0
    siguiente = 1

    for i in range(0, 50):
        lista.append(anterior)

        fib = siguiente + anterior
        anterior = siguiente
        siguiente = fib
    print(lista)

# Fibonacci([])

"""
 Escribe un programa que se encargue de comprobar si un número es o no primo.
 Hecho esto, imprime los números primos entre 1 y 100.
"""

def primo(lista):
    for numero in range(1, 100):
        if numero % 2 == 0:
            lista.append(numero)
    print(lista)
# primo([])

"""
 Crea una única función (importante que sólo sea una) que sea capaz
 de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.
"""

def area():
    poligono = input("Introduzca el polígono al que quiera calcular el área : ").lower()
    if poligono == "triangulo":
        base = int(input("Introduzca la base(m) :"))
        altura = int(input("Introduzca la altura(m) :"))
        area_t = (base * altura) / 2
        print("El área de tu triangulo es ", area_t)
    elif poligono == "cuadrado":
        lado = int(input("Introduzca la lado(m) :"))
        area_c = (lado * lado)
        print("El área de tu cuadrado es ", area_c)
    elif poligono == "rectangulo":
        largo = int(input("Introduzca la largo(m) :"))
        ancho = int(input("Introduzca la ancho(m) :"))
        area_r = (largo * ancho)
        print("El área de tu rectangulo es ", area_r)
    elif poligono.isnumeric():
        print("Pon el poligono no los datos")


"""
 Crea un programa que se encargue de calcular el aspect ratio de una
 imagen a partir de una url.
 - Url de ejemplo:
 https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
- Por ratio hacemos referencia por ejemplo a los "16:9" de una
imagen de 1920*1080px.
"""


"""
 Crea un programa que invierta el orden de una cadena de texto
 sin usar funciones propias del lenguaje que lo hagan de forma automática.
 - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def invertir(palabra):
    reves = palabra[::-1]
    print(reves)
# invertir("Hola Mundo")


"""
 Crea un programa que cuente cuantas veces se repite cada palabra
 y que muestre el recuento final de todas ellas.
 - Los signos de puntuación no forman parte de la palabra.
 - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 - No se pueden utilizar funciones propias del lenguaje que
   lo resuelvan automáticamente.
"""

def contarpalabras(frase):
    lista = []
    contador = 0
    for letra in frase.lower().replace(" ", ""):
        lista2 = []
        if letra in lista2:
            contador = + 1
        else:
            lista2.append(letra)
            lista.append(lista2)
        print(lista, contador)

# contarpalabras("Hola que pasa")


"""
 Crea un programa se encargue de transformar un número
 decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""

def decimal_binario(numero):
    lista = []
    while numero != 0:
        if numero % 2 == 0:
            num = 0
            lista.append(num)
        else:
            num = 1
            lista.append(num)
        numero = numero//2
    print(*lista)
        # // Se utiliza para descartar decimales (no redondea)
# decimal_binario(5)
"""
 Crea un programa que sea capaz de transformar texto natural a código
 morse y viceversa.
 - Debe detectar automáticamente de qué tipo se trata y realizar
   la conversión.
 - En morse se soporta raya "—", punto ".", un espacio " " entre letras
   o símbolos y dos espacios entre palabras "  ".
 - El alfabeto morse soportado será el mostrado en
   https://es.wikipedia.org/wiki/Código_morse.
"""

def codigo_morse(frase):
    lista = []
    for letra in frase.lower().replace(" ", ""):
        if letra == "a":
            morse = "·-"
            lista.append(morse)
        elif letra == "b":
            morse = "-···"
            lista.append(morse)
        elif letra == "c":
            morse = "-·-·"
            lista.append(morse)
        elif letra == "d":
            morse = "-··"
            lista.append(morse)
        elif letra == "e":
            morse = "·"
            lista.append(morse)
        else:
            pass
    print(*lista)
# codigo_morse("abcde")

"""
 Crea un programa que comprueba si los paréntesis, llaves y corchetes
 de una expresión están equilibrados.
 - Equilibrado significa que estos delimitadores se abren y cieran
 en orden y de forma correcta.
 - Paréntesis, llaves y corchetes son igual de prioritarios.
 No hay uno más importante que otro.
 - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 - Expresión no balanceada: { a * ( c + d ) ] - 5 }
"""

def expresiones_equilibradas(frase):
    if "{" in frase and "}" in frase and "[" in frase and "]" in frase and "(" in frase and ")" in frase:
        print("Frase balanceada")
    else:
        print("Frase no balanceada")
# expresiones_equilibradas("{Hola que pasa [ww(9)]}")

"""
 Crea una función que reciba dos cadenas como parámetro (str1, str2)
 e imprima otras dos cadenas como salida (out1, out2).
 - out1 contendrá todos los caracteres presentes en la str1 pero NO
  estén presentes en str2.
 - out2 contendrá todos los caracteres presentes en la str2 pero NO
 estén presentes en str1.
"""

def eliminar_caracteres(str1, str2):
    out1 = []
    out2 = []
    for palabra in str1:
        if palabra not in str2:
            out1.append(palabra)
    print(f"Out1 : {out1}")
    for palabra in str2:
        if palabra not in str1:
            out2.append(palabra)
    print(f"Out2 : {out2}")
# eliminar_caracteres("Hola", "Nano")

"""
 Escribe una función que reciba un texto y retorne verdadero o
 falso (Boolean) según sean o no palíndromos.
 Un Palíndromo es una palabra o expresión que es igual si se lee
 de izquierda a derecha que de derecha a izquierda.
 NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 Ejemplo: Ana lleva al oso la avellana.
"""

def palindromo(texto):
    texto = texto.lower().replace(" ", "")
    if texto == texto[::-1]:
        return True
    else:
        return False
# print(palindromo("Ana lleva al oso la avellana"))
