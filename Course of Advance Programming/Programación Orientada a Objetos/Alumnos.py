class Alumno:
    def __init__(self, nombre, casa, poder=None):
        # None = opcional
        self.nombre = nombre
        self.casa = casa
        self.poder = poder

    def __str__(self):
        return f"{self.nombre} es de {self.casa} con poder de {self.poder}"

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre:
            raise ValueError("Falta el nombre")
        self._nombre = nombre

    @property
    def casa(self):
        return self._casa

    @casa.setter
    def casa(self, casa):
        if casa not in ["España", "Marruecos", "Inglaterra", "Canada"]:
            raise ValueError("Casa no valido")
        self._casa = casa

    def poderes(self):
        match self.poder:
            case "Fuego":
                return "🔥"
            case "Agua":
                return "💧"
            case "Ninguno":
                return "😵"


def main():
    estudiante = info_estudiante()
    print(estudiante)


def info_estudiante():
    # nombre = input("Ingrese el nombre del estudiante: ")
    # casa = input("Ingrese la casa: ")
    # return [nombre, casa]
    # Aplicando diccionario
    # estudiante = {
    #     "nombre": input("Nombre del estudiante: "),
    #     "casa": input("Casa del estudiante: "),
    # }
    # return estudiante
    # Aplicando clase
    nombre = input("Nombre del estudiante: ")
    casa = input("Casa del estudiante: ")
    poder = input("Poder del estudiante: ")
    return Alumno(nombre, casa, poder)


if __name__ == "__main__":
    main()