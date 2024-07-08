import os 

os.system("cls || clear")

nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
altura = float(input("Digite sua altura:"))
peso = float(input("Digite seu peso:"))

os.system("cls || clear")

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura:.2f}")
print(f"Peso: {peso:.1f}")
