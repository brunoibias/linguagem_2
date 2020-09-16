class Utils:
    def validar_nota(self, nota1, nota2, nota3):
        somar = (nota1 + nota2 + nota3) / 3
        if somar >= 7:
            print("Parabes você passou !!!")
        else:
            print("Você reprovou seu Burro !!!")


range_number = Utils()
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
range_number.validar_nota(nota1, nota2, nota3)
