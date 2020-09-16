class Utils:
    def validar_idade(self, idade_homem_1, idade_homem_2, idade_mulher_1, idade_mulher_2):
        if idade_homem_1 > idade_homem_2:
            if idade_mulher_1 > idade_mulher_2:
                somar = idade_homem_2 + idade_mulher_1
                print("Homem mais velhos que mulheres")
        else:
            sonar = idade_mulher_1 + idade_mulher_2
            print("Mulheres mais velhas que homens")


range_number = Utils()
idade_homem_1 = int(input("Digite a idade do 1º homem: "))
idade_homem_2 = int(input("Digite a idade do 2º homem: "))

idade_mulher_1 = int(input("Digite a idade da 1º mulher: "))
idade_mulher_2 = int(input("Digite a idade da 2º mulher: "))

if idade_homem_1 == idade_homem_2 and idade_mulher_1 == idade_mulher_2:
    print("Existem idades iguais.")
else:
    range_number.validar_idade(
        idade_homem_1, idade_homem_2, idade_mulher_1, idade_mulher_2)
