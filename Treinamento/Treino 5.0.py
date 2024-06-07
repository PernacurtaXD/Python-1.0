import os 

os.system("cls || clear")


nome = str(input("Digite seu nome:"))
idade = int(input("Digite sua idade:"))
email = str(input("Digite seu email:"))
tel = int(input("Seu telefone:"))

os.system("cls || clear")

while True:

 print("1- \tMostrar o nome e idade")
 print("2- \tMostrar nome e email")
 print("3- \tMostrar nome e telefone")
 print("4- \tMostrar todas as informacoes")
 print("0- \tSair do programa")
 opcao = int(input("Escolha uma das opcoes?"))

 os.system("cls || clear")

 match (opcao):
    case 1:
        print(f"Seu nome é {nome} e tem {idade} anos de idade")
        break
    case 2:
        print(f"Seu nome é {nome} \nSeu email é {email}")
        break
    case 3:
        print(f"Seu nome é {nome} \nSeu telefone {tel}")   
        break
    case 4: 
        print(f"Seu nome: {nome} \nSua idade: {idade} \nSeu email: {email} \nSeu telefone: {tel}") 
        break
    case 0:
        print("Programa encerrado")
        break
    case _:          
        print("||Opção incorreta, tente novamente||")

        