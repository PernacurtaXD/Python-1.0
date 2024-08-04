from math import pow, sqrt
import os 

os.system("cls || clear")

cateto_oposto = int(input("Qual é o número como cateto oposto? "))
cateto_adjacente = int(input("Qual é o número como cateto adjacente? "))

os.system("cls || clear")

x = pow(cateto_oposto,2) + pow(cateto_adjacente,2)

hipotenusa = sqrt(x)

print(f"O triângulo possui um cateto oposto de {cateto_oposto} e um cateto adjacente de {cateto_adjacente}")
print(f"Tendo um comprimento de uma hipotenusa {hipotenusa}")