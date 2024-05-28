import os 


os.system("cls || clear")
soma = 0 
QUANT = 4
media = 0

notas = []
for i in range (QUANT):
  nota = float(input(f"Digite sua {i+1}ª nota:"))
  notas.append(nota)
  soma+=nota
media = soma / QUANT

os.system("cls || clear")

for i, nota in enumerate(notas):
  print(f"{i+1}ª Nota: {nota}")  
print(f"Média = {media}")

if media >= 7:
  print("Aprovado")
elif media >= 5 or media >= 6.9:
  print("Recuperação")  
elif media < 5:
  print("Reprovado")  