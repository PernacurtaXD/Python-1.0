import os 

os.system("cls || clear")

morango = int(input("Quantos kg de morango deseja:"))
maca = int(input("Quantos kg de maçã deseja:"))



if morango <= 5:
    quant_morango = morango * 2.50
else:
    quant_morango = morango * 2.20

if  maca <= 5:
    quant_maca = maca * 1.80  
else:
    quant_maca = maca * 1.20
   

quant_kg = morango + maca
total_mm = quant_morango + quant_maca

if quant_kg > 8 or total_mm > 25.00:
    os.system("cls || clear")
    desconto = total_mm - (total_mm * 10 / 100)

    print(f"Você adquiriu {morango}kg de morango e {maca}kg de maçã")
    print(f"Subtotal (morango): R${quant_morango:.2f}\nSubtotal (maçã): R${quant_maca:.2f}")
    print(f"Total à se pagar com 10% de desconto: {desconto:.2f}")

else:
    os.system("cls || clear")
    print(f"Você adquiriu {morango}kg de morango e {maca}kg de maçã")
    print(f"Subtotal (morango): R${quant_morango:.2f}\nSubtotal (maçã): R${quant_maca:.2f}")
    print(f"Total: R${total_mm}")