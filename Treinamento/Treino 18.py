import os 

os.system("cls || clear")

preço = float(input("Digite o preço do produto:"))

desconto = preço - (preço * 5 / 100)

print(f"O preço do produto era de R${preço:.2f}, ao adicionar 5% de desconto fica com R${desconto:.2f}")