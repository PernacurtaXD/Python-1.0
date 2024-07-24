import os 


os.system("cls || clear")

numero = int(input("Digite um número para adicionar na tabuada:"))

for i in range(11):
    result = numero * i
    print(f"{numero} x {i} = {result}")