# from math import sqrt
from math import sqrt, floor 

num = int(input("Digite um número:"))

raiz = sqrt(num)

# print("A raiz de {0} é igual a {1}". format(num, raiz))
print("A raiz de {0} é igual a {1}". format(num, floor(raiz)))