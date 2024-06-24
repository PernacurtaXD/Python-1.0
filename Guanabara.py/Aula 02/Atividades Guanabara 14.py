import os 

os.system("cls || clear")

salarioAtual = float(input("Digite seu salário atual:"))

salarioAjustado = salarioAtual + (salarioAtual * 15 / 100)

print(f"Salário com aumento de R${salarioAjustado:.2f}")