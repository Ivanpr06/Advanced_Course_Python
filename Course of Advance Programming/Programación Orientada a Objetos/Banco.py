class Banco:
    def __init__(self,peseta=0, centimos=0, euros=0):
        self.peseta = peseta
        self.centimos = centimos
        self.euros = euros

    def __str__(self):
        return f"{self.peseta} Pesetas, {self.centimos} Céntimos y {self.euros} Euros"

    def _add__(self, otro):
        pesetas = self.peseta + otro.peseta
        centimos = self.centimos + otro.centimos
        euros = self.euros + otro.euros
        return Banco(pesetas, centimos, euros)


ivan = Banco(100,50,5)
print(ivan)

diego = Banco(25, 3, 100)
print(diego)

total = ivan + diego
print(total)
