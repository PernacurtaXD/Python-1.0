import os 

os.system("cls || clear")

preço  = float(input("Qual é o preço do produto?\nR$ "))

os.system("cls || clear")

print("1- Pagamento á vista\n2- Pagamento á prazo")
opcao = int(input("Escolha sua forma de pagamento:"))

 
match(opcao):
   case 1:
      os.system("cls || clear")

      preço_Alterado = preço -(preço * 10/100)
      
      print(f"Valor do produto: R$ {preço:.2f}")
      print("Forma de pagamento: à vista")
      print("Valor do desconto: R$ 10,00")
      print(f"Valor com desconto de 10%: {preço_Alterado:.2f}")
      
   case 2:
      os.system("cls || clear")

      quantidade = int(input("Digite a quantidade de parcelas que deseja pagar. Podendo pagar até 6x:"))
      
      os.system("cls || clear")

      preço_Parcelado = preço / quantidade

      print(f"Valor do produto: R$ {preço:.2f}")
      print("Forma de pagamento: à prazo")
      print(f"Quantidade de parcelas: {quantidade}x")
      print(f"Valor por parcela: R$ {preço_Parcelado:.2f}")
      print(f"Total à prazo: R$ {preço:.2f}")  

   case _:
      print("||Opção escolhida inválida||")  