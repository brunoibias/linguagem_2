
class Validar:
    def validar_numero(self, numero1):
        if numero1 >= 0:
            print("positivo")
        else:
            print("negativo")


validar = Validar()
numero = int(input("Digite um numero: "))

validar.validar_numero(numero)
