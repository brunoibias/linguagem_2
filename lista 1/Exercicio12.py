class Utils:
    def validar_numero(self, numero1, numero2):
        if numero1 > numero2:
            print(numero1)
        else:
            print(numero2)


range_number = Utils()
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if numero1 == numero2:
    print("Ops, não pode digitar numeros iguais.")
else:
    range_number.validar_numero(numero1, numero2)
