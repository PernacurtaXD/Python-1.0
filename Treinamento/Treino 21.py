import os 

os.system("cls || clear")

morango = int (input("Quantos kg de morango deseja:"))
#maçã = int (input("Quantos kg de maçã deseja:"))

 
if morango <= 5:
    preco = morango * 2.50
    print(f"O usuário adquiriu {morango}kg, com preço de R${preco:.2f}")

if morango > 5:
    preco = morango * 2.20
    print(f"O usuário adquiri {morango}kg, com preço de R${preco:.2f}")


if morango >= 8:
    os.system("cls || clear")  
    preco = morango * 2.20 
    
    if preco >= 25.00:
    
     desconto = preco - (preco * 10 / 100)   
     print(f"O usuário adquiriu {morango}kg, com 10% de desconto no preço de R${desconto:.2f}")


   
