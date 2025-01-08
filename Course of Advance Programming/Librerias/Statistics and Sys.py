import statistics
import sys
import cowsay

def nota(nota1,nota2):
    nota = statistics.mean([nota1,nota2])
    print(nota)
#nota(100,80)

def hola():
    try:
        print("Hola me llamo",sys.argv[0])
    except:
        print("Pocos argumentos")

def hola_1():
    if len(sys.argv) < 2:
        sys.exit("Pocos argumentos")
    elif len(sys.argv) > 2:
        sys.exit("Pocos argumentos")
    else:
        print("Hola me llamo", sys.argv[1])

def hola_2():
    if len(sys.argv) < 2:
        sys.exit("Pocos argumentos")

    for arg in sys.argv[1:-1]:
        print("Hola me llamo", arg)

def cow():
    cowsay.cows("Hello," + sys.argv[1])