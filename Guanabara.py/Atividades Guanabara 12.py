import os 

os.system("cls || clear")

real = float(input("Quanto você tem na carteira? R$"))

dolar = real / 3.27

print(f"Com R$ {real:.2f}, você pode comprar US$ {dolar:.2f}")