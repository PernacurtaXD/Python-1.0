import os 

os.system("cls || clear")


preço = float(input("Digite o preço do produto:"))

preçoAlterado = preço - (preço * 5/100)

print(f"Preço com desconto de 5% vale R$ {preçoAlterado:.2f}")