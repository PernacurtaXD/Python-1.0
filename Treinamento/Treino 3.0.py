import os 

media = 0
soma = 0
QUANT = 3
def cab():
    os.system("cls || clear")
    print("="*13)
    print("||RESULTADO||")
    print("="*13)

os.system("cls || clear")

notas = []

for i in range(QUANT):
    nota = float(input("Digite um número:"))
    notas.append(nota)
    soma+=nota


media = soma / QUANT
cab()
for nota in notas:
   print(f"Nota : {nota}") 

print(f"Média = {media:.2f}")
if media >= 7:
    print("Aprovado") 
elif media < 4:
    print("Reprovado")           