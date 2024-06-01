import os 

os.system("cls || clear")

n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))

s = n1 + n2
sub = n1 - n2
mul = n1 * n2
d = n1 / n2
divI = n1 // n2

print(f"Soma = {s}\nSubração = {sub}\nMultiplição = {mul}\nDivisão = {d}\nDivisão inteira = {divI}")