import math
import os 

os.system("cls || clear")

num = int(input("Digite um número:"))
raiz = math.sqrt(num)

print(f"A raiz quadrada de {num} vale {math.ceil(raiz)}")#ceil faz arredondamento para cima 
print(f"A raiz quadrada de {num} vale {raiz}") 
print(f"A raiz quadrada de {num} vale {math.floor(raiz)}")#floor faz arredondamento para baixo