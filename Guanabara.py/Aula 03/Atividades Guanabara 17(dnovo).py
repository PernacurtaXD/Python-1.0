from math import trunc
import os 

os.system("cls || clear")

num = float(input("Digite um número:"))

parte_inteira = trunc(num)

print(f"O número {num} tem a parte inteira {parte_inteira}")