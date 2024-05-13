import os 


os.system("cls || clear")

n = input("Digite algo:") 

print("Tipo da variável", type(n))
print("Só tem espaços?", n.isspace())#Aceita apenas espaços 
print("É número?", n.isnumeric())#Aceita apenas números 
print("É alfabético?", n.isalpha())#Aceita apenas letras 
print("É alfanúmerico?", n.isalnum())#Aceita letras e números 
print("Está em maiúscula?", n.isupper())#Aceita apenas letras MAIÚSCULOS 
print("Está em minúscula?", n.islower())#Aceita apenas letras minúsculas
print("Está capitalizada?", n.istitle())#Aceita apenas letras nesse formato "Python"