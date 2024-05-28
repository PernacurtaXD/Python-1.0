import os 
import sys

os.system("cls || clear")

maior_num = -sys.maxsize - 1
menor_num = sys.maxsize 

numeros = []
for i in range (4):
   numero = int(input(f"Digite o {i+1}ª número:"))
   numeros.append(numero)
   
   if numero > maior_num:
      maior_num = numero
   if numero < menor_num:
      menor_num = numero

os.system("cls || clear")    

for i, numero in enumerate(numeros):
   print(f"{i+1}ª Número: {numero}")

print(f"Maior número = {maior_num}")
print(f"Menor número = {menor_num}")
   
