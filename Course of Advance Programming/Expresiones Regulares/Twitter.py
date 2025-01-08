import re

url = input("URL: ").strip()
# Simple
#
# nombre = url.removeprefix("https://twitter.com/")
# print(f"Nombre: {nombre}")
def caso_1():
    nombre = re.sub(r"^https://?twitter.com/", "",url)
    print(f"Nombre: {nombre}")
caso_1()

def caso_2():
    if validar := re.search(r"^https://?twitter\.com/(.+)$", url, re.IGNORECASE):
        print(f"Nombre: {validar.group(1)}")