# Mismo ejercicio pero implementando todo lo aprendido
class Alumnos:
    def __init__(self,nombre,casa):
        self.nombre=nombre
        self.casa=casa

    def __str__(self):
        return f"{self.nombre} - {self.casa}"

    @classmethod
    def datos(cls):
        nombre=input("Ingrese el nombre del alumno: ")
        casa=input("Ingrese la casa del alumno: ")
        return cls(nombre,casa)

def main():
    estudiante = Alumnos.datos()
    print(estudiante)

if __name__=="__main__":
    main()