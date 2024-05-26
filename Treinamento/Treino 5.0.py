import os 

os.system("cls || clear")


nome = str(input("Digite seu nome:"))
idade = int(input("Digite sua idade:"))
email = str(input("Digite seu email:"))
tel = int(input("Seu telefone:"))

os.system("cls || clear")

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
    case 2:
        print(f"Seu nome é {nome} \nSeu email é {email}")
    case 3:
        print(f"Seu nome é {nome} \nSeu telefone {tel}")   
    case 4: 
        print(f"Seu nome: {nome} \nSua idade: {idade} \nSeu email: {email} \nSeu telefone: {tel}") 
    case 0:
        print("Programa encerrado")
    case _:          
        print("||Opção incorreta, tente novamente||")

        print("1- \tMostrar o nome e idade")
        print("2- \tMostrar nome e email")
        print("3- \tMostrar nome e telefone")
        print("4- \tMostrar todas as informacoes")
        print("0- \tSair do programa")
        opcao2 = int(input("Escolha uma das opcoes?"))   
        
        os.system("cls || clear")
        
        match (opcao2):
            case 1:
               print(f"Seu nome é {nome} e tem {idade} anos de idade")
            case 2:
               print(f"Seu nome é {nome} \nSeu email é {email}")
            case 3:
               print(f"Seeu nome é {nome} \nSeu telefone {tel}")   
            case 4: 
               print(f"Seu nome: {nome} \nSua idade: {idade} \nSeu email: {email} \nSeu telefone: {tel}") 
            case 0:
              print("Programa encerrado")