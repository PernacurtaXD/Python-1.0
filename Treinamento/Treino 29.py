import os 

os.system("cls || clear")
soma = 0

for i in range (2):
    nota = float(input("Digite sua nota:"))
    soma+=nota

media = soma / 2

print(f"Média = {media}")
