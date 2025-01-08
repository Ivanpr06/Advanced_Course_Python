import random

class Sombrero:
    # Variable que se puede usar en todos los métodos
    casas = ["España","Marruecos","Inglaterra","Canada"]

    @classmethod
    def sort(cls, nombre):
        print(f"{nombre} esta en {random.choice(cls.casas)}")


Sombrero.sort("Harry")
