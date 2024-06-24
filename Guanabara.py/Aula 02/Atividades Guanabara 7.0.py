import os 

os.system("cls || clear")

numero = int(input("Digite um número:"))

sucessor = numero + 1
antecessor = numero - 1
#Sem variavel
print(f"Antecessor = {numero - 1} || Sucessor = {numero + 1}")
#Com variavel
print(f"Antecessor  = {antecessor}  ({numero}) ", end= " ")
print(f"Sucessor = {sucessor}")


