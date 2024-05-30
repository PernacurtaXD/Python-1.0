import os 

os.system("cls || clear")

numeros = []
QUANT = 6
pares = 0
impares = 0

for i in range(QUANT):
    numero = int(input(f"Digite o {i+1}ª número:"))
    numeros.append(numero)
    
    if numero % 2 == 0:
        pares+=1
    else:
        impares+=1

os.system("cls || clear")

for i, numero in enumerate(numeros):
  
 print(f"{i+1}ª número = {numero}")

print(f"Quantidade de pares = {pares}") 
print(f"Quantidade de impares = {impares}") 
