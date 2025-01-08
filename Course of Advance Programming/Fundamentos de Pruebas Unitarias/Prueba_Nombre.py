from Hola import hola

def prueba():
    assert hola("Ivan") == "hola, Iván"

def prueba_argumento():
    for nombre in ["Hermione", "Harry", "Ron"]:
        assert hola() == f"hola, {nombre}"
