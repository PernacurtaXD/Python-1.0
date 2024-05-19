import os


os.system("cls || clear")

numero = int(input("Digite um número:"))

dobro = numero * 2
triplo = numero * 3
raizq = numero**(1/2)

print(f"O dobro de {numero} vale {dobro}")
print(f"O triplo de {numero} vale {triplo}")
print(f"A raiz quadrada de {numero} vale {raizq:.3}")