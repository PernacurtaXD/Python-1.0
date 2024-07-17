import os 


os.system("cls || clear")

print("\Selecione um personagem/")
print("1- Leonardo\n2- Raphael\n3- Donattelo\n4- Michelangelo")
opcao = int(input("Escolha uma das opções:"))

match(opcao):
    case 1:
        os.system("cls || clear")
        print("\t||Personagem||")
        print("\tLeonardo")
        print("\tIdade: 20 anos")
        print("\tHabilidade: Ninja")
        print("\tFaixa Azul")
        print("\tArma: Katana")

    case 2:
        os.system("cls || clear")
        print("\t||Personagem||")
        print("\tRaphael")
        print("\tIdade: 18 anos")
        print("\tHabilidade: Ninja")
        print("\tFaixa Vermelha")
        print("\tArma: Sai")

    case 3:            
        os.system("cls || clear")
        print("\t||Personagem||")
        print("\tDonattelo")
        print("\tIdade: 16 anos")
        print("\tHabilidade: Ninja")
        print("\tFaixa Roxo")
        print("\tArma: Bastão")

    case 4:
        os.system("cls || clear")
        print("\t||Personagem||")
        print("\tMichelangelo")
        print("\tIdade: 13 anos")
        print("\tHabilidade: Ninja")
        print("\tFaixa Laranja")
        print("\tArma: Nunchaku")

    case _:
        os.system("cls || clear")
        print("Opção inválida")                
