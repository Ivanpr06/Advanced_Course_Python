def main():
    n = int(input("Que es n? : "))
    for oveja in ovejas(n):
        print(oveja)


def ovejas(n):
    for i in range(n):
        """yield es una orden muy similar a un return, con una gran diferencia,
        yield pausará la ejecución de tu función y guardará el estado 

        de la misma hasta que decidas usarla de nuevo."""
        yield "🐑" * i


if __name__ == "__main__":
    main()