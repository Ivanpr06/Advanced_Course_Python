def main():
    yell( ["Esto", "es", "CS50"])

def yell(palabras):
    # Muy Simple
    # mayuscula = []
    # for palabra in palabras:
    #     mayuscula.append(palabra.upper())

    # Reducido
    # mayusculas = [palabra.upper() for palabra in palabras]
    # print(*mayusculas)

    # Usando map
    mayuscula = map(str.upper, palabras)
    # *variable = quita sintaxis de lista
    print(*mayuscula)



if __name__ == "__main__":
    main()