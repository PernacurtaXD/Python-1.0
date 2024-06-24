import os 

os.system("cls || clear")

largura = float(input("Qual a largura da parede:"))
altura = float(input("QUal é a  altura da parede:"))

area = largura * altura
print(f"A parede possui uma altura de {altura}m e a largura de {largura}m,", end=" ")
print(f"com uma área de {area} m²,", end=" ")

tinta = area / 2

print(f"e para pintar essa parede você presica de {tinta} L")