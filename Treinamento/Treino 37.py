import os 


os.system("cls || clear")
soma = 0


for i in range(2):
    nota = float(input(f"Digite sua {i+1} nota:"))
    soma+=nota

media = soma / 2

print()