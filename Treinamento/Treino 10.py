import os 

os.system("cls || clear")

contador = 0
soma = 0
media = 0


while True:
    num = int(input(f"Digite um número:"))


    if num < 0:
      break   

    soma+=num
    contador+=1

media = soma / contador

print(f"Média = {media:.2f}")
   
