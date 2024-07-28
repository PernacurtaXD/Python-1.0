import os 

os.system("cls || clear")

reais = float(input("Quanto você tem na carteira:"))

dolar = reais / 3.27

os.system("cls || clear")

print(f"Ele possui R${reais:.2f} na carteira\nAdquiriu US${dolar:.2f}")
