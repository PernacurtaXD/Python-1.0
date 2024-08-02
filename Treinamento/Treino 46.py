import os 

os.system("cls || clear")


nome = input("Digite o nome do produto:")
preco = float(input("Qual é o preço do produto? R$"))

print("||Forma de pagamento||")
print("1- Á vista")
print("2- Parcelado")
forma_pagamento = int(input("Escolha a forma de pagamento:"))

match(forma_pagamento):

    case 1:
        os.system("cls || clear")
        desconto = preco - (preco * 5 / 100)
        print(f"O {nome} custava R${preco:.2f}, com 5% de desconto de R${desconto:.2f}")

    case 2:
        os.system("cls || clear")
        parcela = int(input("Deseja parcelar de quantas vezes?"))
        
        os.system("cls || clear")

        valor_parcelado = preco / parcela

        print("{} de R${:.2f} parcelado de {} vezes de R${:.2f}". format(nome, preco, parcela, valor_parcelado))

    case _: 
        print("Opção inválida")    

