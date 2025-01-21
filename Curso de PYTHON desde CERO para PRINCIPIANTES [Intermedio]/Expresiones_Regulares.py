## Re
import re

texto = "Hola q pasa"
texto_otro = "Como estan los maquinas"

def match():

    # re.I = Perform case-insensitive matching; expressions like [A-Z] will also match lowercase letters.
    match = re.match("Hola", texto,re.I)
    print(match)
    # Número de caracteres que coincide
    print(match.span())
    # Imprime lo que coincide
    print(match.group())

    principio, final = match.span()
    print(texto[principio:final])

    print(re.match("Hola", texto))
    print(re.match("Hola", texto_otro))
    print(re.match("pasa", texto))

    match = re.match("Hola", texto_otro)
    if not match == None:
        print(match)
    else:
        print("No hay match")

def search():
    search = re.search("Hola", texto, re.I)
    print(search)

def findall():
    find = re.findall("Hola", texto, re.I)
    print(find)

def split():
    texto = "Hola q\n pasa"
    print(re.split("\n", texto))

def sub():
        print(re.sub("Hola|hola","Manolo", texto))

def pattern():
    pattern = r"[0-4]"
    print(re.findall(pattern, texto))

    pattern = r"\D"
    print(re.findall(pattern, texto))

    pattern = r"[a-z]"
    print(re.findall(pattern, texto))

    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$"

    email = "ivan.ponti.rubio06@gmail.com"
    print(re.match(pattern, email))
    print(re.findall(pattern, email))
    print(re.search(pattern, email))

    email2 = "ivan.ponti.rubio06@gmail.com.90"
    print(re.findall(pattern, email2))