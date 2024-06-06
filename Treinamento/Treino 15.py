import os 

os.system("cls || clear")

login_cadastrado = "Luis"
senha_cadastrada = "123" 

login = input("Digite seu login:")
senha = input("Digite sua senha:")

if login_cadastrado == login and senha_cadastrada == senha:
    print("Seja Bem vindo!!")
else:
    print("Login ou senha inválido!!")   