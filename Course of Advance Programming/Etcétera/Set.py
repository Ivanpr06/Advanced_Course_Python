estudiantes = [
    {"nombre":"Ivan", "nacionalidad":"España"},
    {"nombre": "Jesús", "nacionalidad": "Maruecos"},
    {"nombre": "Charles", "nacionalidad": "Inglaterra"},
    {"nombre": "Diego", "nacionalidad": "España"},
]

nacionalidades = set()
for estudiante in estudiantes:
    nacionalidades.add(estudiante["nacionalidad"])

for nacionalidad in sorted(nacionalidades):
    print(nacionalidad)