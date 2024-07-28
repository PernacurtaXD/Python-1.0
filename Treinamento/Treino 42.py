import os 

os.system("cls || clear")

largura = float(input("Qual é a largura da parede?"))
altura = float(input("Qual é a altura da parede?"))

area = largura * altura 
tinta = area / 2

print(f"A parede possui uma altura de {altura}m e sua largura de {largura}m, tendo assim uma área de {area:.1f}m²")
print(f"Para realizar a pintura da parede vai se utilizar {tinta}l de tinta.")