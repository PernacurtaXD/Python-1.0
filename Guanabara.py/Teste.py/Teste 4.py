import os 



os.system("cls || clear")

numero1 = int(input("Digite o primeiro número:"))
numero2 = int(input("Digite o segundo número:"))

s = numero1 + numero2
m = numero1 * numero2
d = numero1 / numero2
di = numero1 // numero2
e = numero1 ** numero2

print(f" Soma = {s}\n Multiplicação = {m}\n Divisão = {d:.2},", end = " ")
print(f"Divisão inteira = {di}, Potência = {e}")




