import os
QUANTIDADES_NOTAS=3
soma=0
media=0
nota=0
os.system("cls || clear")

notas = []
for i in range(QUANTIDADES_NOTAS):

    while True:
        os.system("cls || clear")
        
        nota=float(input(f"Digite a {i+1}ª nota: "))
        notas.append(nota)
        if nota<0 or nota>10:
            input("Nota Invalida, tente novamente \n")
        else:
            soma+=nota
            break
    


media=soma/QUANTIDADES_NOTAS
if media>=7:
        resultado="Aprovado"
elif media<=5:
      resultado="Reprovado"
else:
  resultado="Reprovado"

for i, nota in enumerate (notas):
  print(f"{i+1}ª Nota: {nota}")
print(f"Média = {media:.2f}, Aluno do Instituto Educacional está {resultado}.")
