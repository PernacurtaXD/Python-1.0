import os 

def cab():
    os.system("cls || clear")
    print("="*2,"Resultado","="*2)


def solicitando_Dados():
    nome = input("Digite seu nome:")
    idade = int(input("Digite sua idade:"))

    return nome, idade 

cab()
nome, idade = solicitando_Dados()
print(f"Seu nome é {nome} com {idade} anos")


