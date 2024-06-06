import os 

os.system("cls || clear")


idade = int(input("Digite sua idade:"))

if idade <= 18 or idade >= 65:
    print (f"A idade desse usuário de {idade} anos, não é obrigatório a votar.")
else:
        print ("É obrigatório a votar.")