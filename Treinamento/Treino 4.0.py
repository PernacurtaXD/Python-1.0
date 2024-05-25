#Uso de parâmetros sem reorno e com retorno
import os 

os.system("cls || clear")

#Sem retorno
def cab():
    os.system("cls || clear")
    print(" ||Resultado|| ") 

#Com retorno
def numeros(n1, n2):
    resultado = n1 + n2
    mediar = resultado / 2
    return mediar

prim_num = int(input("Digite o primeiro número:"))
seg_numero = int(input("Digite o segundo número:"))    

media = numeros(prim_num,seg_numero)

cab()
print(f"Média vale {media}")