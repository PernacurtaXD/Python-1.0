import os 
from math import trunc

os.system("cls || clear")

numero = float(input("Digite um número decimal:"))

numero_alterado =  trunc(numero)

print(f"Número digitado {numero}, e sua porção inteira é {numero_alterado}")
