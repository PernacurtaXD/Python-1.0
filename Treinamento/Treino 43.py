import os 

os.system("cls || clear")

preco = float(input("Digite o preço do produto: R$"))

desconto = preco - (preco * 5 / 100)

print(f"O preço do produto é de R${preco:.2f}\nAo adicionar 5% de desconto R${desconto:.2f}")
