import os 

os.system("cls || clear")

numero = int(input("Digite um número:"))

dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
os.system("cls || clear")

print(f"Número digitado {numero}\nDobro de {numero} vele {dobro}\nTriplo de {numero} vale {triplo}\nRaiz quadrada de {numero}  vale {raiz:.2f}")