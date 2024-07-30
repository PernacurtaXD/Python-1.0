"""
Recebendo dados do usuário
"""
#Entrada de dados 
print("Qual é o seu nome?")
nome = input()# Input -> Entrada 

# Exemplo de print "antigo" 2.x
# print("Seja bem-vindo(a) %s" % nome)

# Exemmplo de print "moderno" 3.x
# print("Seja bem-vindo(a) {0}". format(nome))

# Exemplo de print "atual" 3.7
print(f"Seja bem vindo(a) {nome}")


print("Qual é a sua nota?")
idade = input()

#Processamento

#Saída 
# Exemplo de print "antigo" 2.x
# print("A %stem %s anos" % (nome, idade)) 

#Exemmplo de print "moderno" 3.x
# print("A {0} tem {1} anos".format(nome, idade))