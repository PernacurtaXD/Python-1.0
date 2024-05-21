import os 

os.system("cls || clear")

contador = 0
soma = 0
media = 0
nome = str(input("Digite seu nome:"))
idade = int(input("Digite sua idade:"))

for i in range(1,5):
    nota = float(input(f"Digite sua {i}ª nota:"))
    soma+=nota
    contador = contador + 1

 
media = soma / contador

print(f"Aluno {nome} com {idade} anos")
for i in range (1,5):
     print(f"{i}ª Nota: {nota}") 
