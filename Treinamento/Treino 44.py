import os 


os.system("cls || clear")


salario_atual = float(input("Digite seu salário:"))

salario_com_desconto = salario_atual + (salario_atual * 15 / 100)

os.system("cls || clear")

print(f"O usuário com salário de R${salario_atual:.2f}, teve um aumento de 15% de desconto de R${salario_com_desconto:.2f}")