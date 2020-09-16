class Utils:
    def calcular_volume(self, comprimento, largura, altura):
        volume = comprimento * largura * altura
        print('O resultado final é ', volume)


range_number = Utils()

comprimento = int(input("Digite o valor do comprimento: "))
largura = int(input("Digite o valor da largura: "))
altura = int(input("Digite o valor da altura: "))

range_number.calcular_volume(comprimento, largura, altura)
