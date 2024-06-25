#Alunos = Rafael Vitor dos Santos Souza e Luis Felipe de Jesus Santana 
from dataclasses import dataclass
import os 
@dataclass
class Produto:
    def __init__(self, codigo:int, nome:str, categoria:str, preco:float, fornecedor:str):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.fornecedor = fornecedor

def salvar(produtos):
    nome_arquivo = 'alunos.txt'
    with open(nome_arquivo, 'w') as arquivo:
        for Produto in produtos:
            arquivo.write(f"{Produto.codigo},{Produto.nome},{Produto.categoria}{Produto.preco}{Produto.fornecedor}")
    print(f"Dados gravados com sucesso.")
    
produtos = []
os.system("cls||clear")

while True:
    print("1\t Cadastrar Produto")
    print("2\t Exibir Produtos")
    print("3\t Remover Produto")
    print("4\t Gestão Fornecedores")
    print("5\t Segurança e Controle de Acesso")
    
    opcao = int(input("Escolha uma das opções acima: "))
    match(opcao):
        case 1:
            os.system("cls||clear")
            while True:
                codigo = input("Digite o codigo: ")
                os.system("cls||clear")
                nome = input("Digite o nome: ")
                os.system("cls||clear")
                
                while True:
                    opcaoCat = int(input("1-Perecivel\n2-Nâo Perecivel\nEscolha uma das opções:"))
                    if opcaoCat == 1:
                        categoria = "Perecivel"
                        os.system("cls||clear")
                        break
                    elif opcaoCat == 2:
                        categoria = "Não Perecivel"
                        os.system("cls||clear")
                        break
                    else :
                        os.system("cls||clear")
                        print("Opção invalida, digite novamente")

                preco = input("Digite o preço: R$")
                os.system("cls||clear")
                fornecedor = input("Digite o nome do fornecedor: ")
                produtos.append(Produto(codigo,nome,categoria,preco,fornecedor))
                os.system("cls||clear")
                escolha = input("Deseja cadastrar outro produto?s/n\n")
                escolha = escolha.lower()
                if escolha != 's':
                    break
        case 2:
            os.system("cls||clear")
            cont = 0
            for i in (produtos):
                cont += 1
                print(f"{cont} Produto")
                print(f"codigo : {i.codigo}")
                print(f"nome : {i.nome}")
                print(f"categoria : {i.categoria}")
                print(f"preco: R${i.preco}")
                print(f"fornecedor: {i.fornecedor}")
                print()
            input("Aperte enter para continuar...")
            os.system("cls||clear")
        
        case 3:
            usuariodelete = str(input("Digite o nome do usuario para deletar: "))
            for Produto in produtos:
                if usuariodelete == Produto.nome:
                    produtos.remove(Produto)
                    salvar(produtos)
                else:
                    print("produto nao encontrado")