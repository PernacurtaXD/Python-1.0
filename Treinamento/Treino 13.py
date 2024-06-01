import os 

os.system("cls || clear")

preco = float(input("Digite o preço do produto, para adicionar o desconto: R$"))

#Calculando porcentagem 
desconto = preco - (preco * 5 / 100)

print(f"Preço digitado pelo usuário R$ {preco:.2f}, com 5% de desconto de R$ {desconto:.2f}")