class Persona:
    def __init__(self, nombre):
        if not nombre:
            raise ValueError("Falta un nombre")
        self.nombre = nombre

class Alumno(Persona): # Alumno es una subclase de Persona
    def __init__(self,nombre,casa):
        super().__init__(nombre)
        self.casa=casa


class Profesor(Persona): # Profesor es una subclase de Persona
    def __init__(self,nombre,asignatura):
        super().__init__(nombre)
        self.asignatura=asignatura

persona = Persona("humano")
alumno = Alumno("Paco", "España")
profesor = Profesor("Juan","Matemáticas")