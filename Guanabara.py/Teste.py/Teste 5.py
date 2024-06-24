import math
import os 


os.system("cls || clear")
num = int(input("Digite um número:"))

raiz = math.sqrt(num)


#print(f"A raiz de {num} é igual a {math.ceil(raiz)}")
print(f"A raiz de {num} é igual a {math.floor(raiz):.2f}")