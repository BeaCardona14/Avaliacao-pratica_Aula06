#ENTRADA DE DADOS E OPERAÇÕES FINANCEIRAS
#Crie um programa em Python ques imule a compra de um produto.
# O script deve:

nomeproduto = input("Digite o nome do produto: ")
PreçoUnitario= float(input("Diite o preço do produto: "))
Qtdvendida = int(input("Dgite a quantidade: "))
subtotaldavenda = (PreçoUnitario * Qtdvendida)
print(f"----subtotal---{subtotaldavenda}")

imposto = (subtotaldavenda + PreçoUnitario) * 0.8 

print(f"Valor do imposto:{imposto} ")

valortotal = (subtotaldavenda + imposto)
print(f"valor total: {valortotal:.2f}")




