import os 

os.system("cls || clear")

dias = int(input("Quantos dias alugados?"))
km = float(input("Quantos km percorreu?"))

pago = (dias * 60) + (km * 0.15)

print(f"O total a pagar é R${pago:.2f}")