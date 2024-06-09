import os 

os.system("cls || clear")

salario = float(input("Qual é o seu salário?"))

novo = salario + (salario * 15 / 100)

print(f"Possuia um salário de R${salario:.2f}, com um aumento de 15%, fica com {novo:.2f}")