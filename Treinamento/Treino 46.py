import os 


os.system("cls || clear")


nome = input("Digite o nome do produto:")
preco = float(input("Qual é o preço do produto?"))

print("Forma de pagamento")
print("1- Á vista")
print("2- Parcelado")

forma_pagamento = input("Escolha forma de pagamento:")

match(forma_pagamento):

    case 1:
        print(f"")
