import os 


os.system("cls || clear")

nota1 = float(input("Digite sua primeira nota:")) 
nota2 = float(input("Digite sua segunda nota"))
os.system("cls || clear")

soma = nota1 + nota2
media = soma / 2

print(f"Primeira Nota = {nota1}\nSegunda Nota = {nota2}")
print(f"Média = {media}")