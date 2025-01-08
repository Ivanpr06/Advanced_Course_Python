def version_1():
    def total(centimos, euros, mil):
        return (mil * 1000 + euros) * 100 + centimos
    # Diferentes Formas

    # Lista
    # monedas = [10,5,1]
    # #*variable = divide la lista en orden con las variables de las monedas
    # print(total(*monedas), "céntimos")

    # Print Simple
    #print(total(centimos=10, euros=5, mil=1), "céntimos")

    # Biblioteca
    # Es la misma función de desempaquetar que la lista solo que con diccionario son 2 *
    monedas = {"centimos": 10, "euros": 5, "mil": 1}
    print(total(**monedas), "céntimos")

def version_2():
    def f(*args, **kwargs):
        # args crea lista
        #print("Posición:", args)

        # kwargs crea diccionario
        print("Nombre:", kwargs)

    f(centimos=10, euros=5, mil=1)