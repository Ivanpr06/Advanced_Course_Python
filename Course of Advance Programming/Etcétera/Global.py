saldo = 0
# Con las clases global no tiene uso ya que self hace ya esta función
def main():
    print("Saldo: ",saldo)
    aumento(100)
    decrece(50)
    print("Saldo: ",saldo)

def aumento(n):
    global saldo
    saldo = saldo + n

def decrece(n):
    global saldo
    saldo = saldo - n

if __name__ == "__main__":
    main()