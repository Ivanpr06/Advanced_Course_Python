import sys
import argparse


def version_1():
    for i in range(3):
        print("meow")


def version_2():
    MEOWS = 4
    for i in range(MEOWS):
        print("meow")


def version_3():
    class Gato:
        MEOWS = 3

        def meow(self):
            for i in range(Gato.MEOWS):
                print("meow")

    gato = Gato()
    gato.meow()


def version_4():
    def meow(n):
        for i in range(n):
            print("meow")

    numero = int(input("numero: "))
    meow(numero)


def version_5():
    def meow(n) -> str:
        """Meows n veces
        variable n: Numero de veces que se dice meow
        type n; int

        """
        return "meow\n" * n

    numero: int = int(input("numero: "))
    meows: str = meow(numero)
    print(meows, end="")


def version_6():
    if len(sys.argv) == 1:
        print("meow")
    elif len(sys.argv) == 3 and sys.argv[1] == "-n":
        n = int(sys.argv[2])
        for i in range(n):
            print("meow")
    else:
        print("Ubicación: Constantes.py")


def version_7():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n")
    args = parser.parse_args()

