import os 


os.system("cls || clear")

n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2

os.system("cls || clear")

print(f"O {n1} e {n2} valem:\nSoma = {soma}")
print(f"Subtração = {sub}\nMultiplicação = {mult}\nDivisão = {div}")