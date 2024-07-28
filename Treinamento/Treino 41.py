import os


os.system("cls || clear")


num = int(input("Digite um número:"))

for i in range(11):
    resultado = num * i

    print(f"{num} x {i} = {resultado}")