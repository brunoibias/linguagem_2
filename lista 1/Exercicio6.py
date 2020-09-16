class Validar:
    def validar_numero_positivo_ou_negativo(self, numero1):
        if numero1 >= 0:
            print("Positivo")
        else:
            print("Negativo")

    def validar_impar_ou_par(self, numero1):
        resto = numero1 % 2
        if numero1 >= 0:
            print('Número é par')
        else:
            print('Número é impar')


validar = Validar()
numero = int(input("Digite um numero: "))

validar.validar_numero_positivo_ou_negativo(numero)
validar.validar_impar_ou_par(numero)
