import os
QUANTIDADES_NOTAS=3
soma=0
media=0
nota=0
os.system("cls || clear")

for i in range(QUANTIDADES_NOTAS):
    while True:
        nota=float(input(f"Digite a {i+1}ª nota: "))
        if nota<0 or nota>10:
            print("Nota Invalida \n")
        else:
            soma+=nota
            break
    


media=soma/QUANTIDADES_NOTAS
if media>=7:
        resultado="Aprovado"
elif media>=5:
      resultado="Reprovado"
else:
  resultado="Recuperacão"

print(media)
print(resultado)