import os 
def cab():
    os.system("cls || clear")
    print("|| SENAI ||")

QUANT = 4

def Notas():
    notas = []
    soma = 0 
    for i in range(QUANT):
       nota = float(input(f"Digite o {i+1}º número:"))
       notas.append(nota)
       soma+=nota

    return soma, notas 

def medias(soma):
    media = soma / QUANT

    return media 

def situacao(media):
    if media >= 7:
        resultado = "Aprovado"
    else: 
        resultado = "Reprovado"

    return resultado


soma_notas, lista_notas = Notas()
media = medias(soma_notas)
situacao_aluno = situacao(media)

cab()
for i, soma_notas in enumerate (lista_notas, start=1):
    print(f"Notas {i}ª = {soma_notas}")

print(f"Média do usuário vele {media}")
print(f"Situação do aluno : {situacao_aluno}")
