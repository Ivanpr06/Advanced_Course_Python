def main():
    x = int(input("Ingrese un numero: "))
    print(f"x sqared is {square(x)}")

def square(n):
    # Error Intencional
    #return n+n
    return n*n

# Evitar que el código de prueba o ejemplos de uso en un
# archivo se ejecuten cuando el archivo es importado como módulo.
if __name__ == "__main__":
    main()