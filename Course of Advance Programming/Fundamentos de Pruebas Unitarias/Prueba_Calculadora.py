from Calculadora import square

def main():
    test_square()

def test_square():
    # La pruebas deberian ser minimo 2

    # if square(2) != 4:
    #     print("2 elevado a 2 no es 4")
    # if square(3) != 9:
    #     print("3 elevado a 3 no es 9")

    # Forma más limpia( assert = confirmar )
    # try:
    #     assert square(2) == 4
    # except:
    #     print("2 elevado a 2 no es 4")
    #
    # try:
    #     assert square(3) == 9
    # except:
    #     print("3 elevado a 3 no es 9")
    #
    # try:
    #     assert square(-2) == 4
    # except:
    #     print("-2 elevado a -2 no es 4")
    #
    # try:
    #     assert square(-3) == 9
    # except:
    #     print("-3 elevado a -3 no es 9")
    #
    # try:
    #     assert square(0) == 0
    # except:
    #     print("0 elevado a 0 no es 0")

    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0



if __name__ == '__main__':
    main()