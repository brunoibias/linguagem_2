
lista = []


class Utils:
    def add_lista(self, item):
        lista.append(item)
        print(lista)
        print('a) Maior Elemento', max(lista))
        print('b) Soma dos Elementos', sum(lista))


util = Utils()


while True:
    numero = int(input("Digite um numero: ou -0 para sair: "))
    util.add_lista(numero)
    if numero == -0:
        break
