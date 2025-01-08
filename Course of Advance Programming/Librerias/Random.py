import random

def moneda():
    moneda = random.choice(["cara","cruz"])
    print(f"El resultado es {moneda}")

def numero():
    # Randint es solo para int no str ni float
    numero = random.randint(1,10)
    print(f"El numero es {numero}")

def cartas():
    # Parecido a choice pero te imprime la lista entera
    cartas = ["rey","reina","joker"]
    random.shuffle(cartas)
    print(cartas)
    # for carta in cartas:
    #     print(carta)
