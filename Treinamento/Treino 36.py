import os 

os.system("cls || clear")

numero = int(input("DIgite um número:"))

os.system("cls || clear")

d = numero * 2
t = numero * 3
#raiz_quadrada = numero**(1/2)
raiz_quadrada = pow(numero, (1/2))

print(f"O dobro de {numero} vale {d}\nO triplo de {numero} vale {t}\nA raiz quadrada de {numero} vale {raiz_quadrada:.2f}")