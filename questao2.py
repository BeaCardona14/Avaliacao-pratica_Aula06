# Escreva um programa que leia o valor total de uma compra e aplique o desconto correto:

valor = float(input("Digite um valor da compra: "))
desconto = (valor * 0.5) 
desconto = (valor* 0.10) 
desconto = (valor * 0.15)

if valor < 100.00:
   print("Sem desconto\n")

elif valor  <=  299.99:
    print("5% de desconto")
elif valor <= 499.99:
    print("10% de desconto")
else:
    print("15% de desconto")         

valor_economizado = valor * (desconto / 100)
valor_final = valor - valor_economizado 

print(f"valor original:{valor}")

print(f"valor do desconto: {valor_economizado}")

print(f"Valor total : {valor_final}")


