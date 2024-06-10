import os 

os.system("cls || clear")

m = float(input("Digite a distância em metros:"))

os.system("cls || clear")
dm = m * 10
cm = m * 100
mm = m * 1000
dam = m / 10
hm = m / 100
km = m / 1000

print(f"Valor em metros = {m}m \nConvertido em dm = {dm}dm\nConvertido em cm = {cm}cm\nConvertido em mm = {mm}mm")
print(f"Convertido em dam = {dam}dam\nConvertido em hm = {hm}hm\nConvertido em km = {km}km ") 