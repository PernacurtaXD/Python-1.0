import os 


os.system("cls || clear")

soma = 0
num_desejado = int(input("Digite quantos números deseja digitar:"))

os.system("cls || clear")


for i in range (num_desejado):
    num = int(input(f"Digite o {i+1}ª número:"))
    soma+=num

   
media = soma / num_desejado
  
print(f"Média = {media}")