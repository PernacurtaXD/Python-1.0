"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

The Zen of Pyton - by Tim Peters 

import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica.

[1] - Utilize Camel Case para os nomes de classes;

#Forma correta 
class Calculadora:
    pass
    
#Forma incorreta 
class calculadora_cientifica: #Ela tem começar com a letra maiúscula = Calculadora_cientifica
    pass                      #E não existe o "_" = Calculadoracientifica
                              #E a outra letra fica em maiúscula = CalculadoraCientifica

#Se o nome for simples (Calculadora), a palavra tem que começar com a letra maiúscula                            
#Se o nome for composto (CalculadoraCientifica), as duas palavras tem que começar com a letra maiúscula


[2] - Utilize nomes em minúsculo, separados por underline para a função ou variáveis;

def somar():
    pass

def somar_dois():
    pass 

numero = 4

numero_impar = 5

[3] - Utilize 4 espaços para identação! (Não use tab);

if 'a' in 'banana':
    print('tem')

[4] - Linhas em Branco;    

- Separar funções e definição de classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;

class Classe:
    pass
#pular 2 linhas em branco

class Outra:
    pass

[5] - Imports;
 
-Imports devem ser sempre feitos em linhas separadas 

#Import Errado 
import sys, os

#Import Certo 
import sys 
import os 

#Não há problema em utilizar:
from types import StringType, ListType

#Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:
from types import(
    StringType,
    ListType,
    SetType,
    OutroType
)

#Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e antes
#de constantes ou variáveis globais;

#Espaços em expressões e instruções 

#Não faça 
funcao( algo[ 1 ], { outro: 2 } )

#Faça 
funcao(algo[1], {outro: 2})

#Não faça 
algo (1)

#Faça 
algo(1)

"""