
import numpy


class Utils:
    def validar_numero(self):
        numeros = []
        numero = 0
        while numero == 0:
            numero = int(input("Entre com o 1º número: "))
            if numero == 0:
                print("O 1º número não pode ser zero.")
        numeros.append(numero)
        for j in range(9):
            numero = int(input("Entre com o %dº número: " % (j+2)))
            if numpy.in1d(numeros, [numero]) == True:
                print("Não pode numero iguais")
                break
            else:
                numeros.append(numero)
        maior = max(numeros)
        print("O numero mais dessa lista é", maior)


range_number = Utils()
range_number.validar_numero()
