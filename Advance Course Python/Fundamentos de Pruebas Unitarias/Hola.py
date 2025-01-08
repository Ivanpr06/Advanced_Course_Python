def main():
    nombre = input("Cual es tu nombre? :")
    print(hola(nombre))

def hola(to="mundo"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()