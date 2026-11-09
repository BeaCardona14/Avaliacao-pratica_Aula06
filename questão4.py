
#Processamento de Vendas Diárias

#Perguntar a quantidade de vendas
qtd_vendas = int(input("quantas vendas foram realizadas no dia?"))

total = 0 
maior_venda = 0

#Usando o laço de repetição for para registrar as vendas
for i in range(qtd_vendas):
    valor = float(input(f"Digite o valor da venda da {i + 1}ª da venda : R$"))

#SOMA DOS VALORES DA VENDA
total = total + valor 

#MAIOR VENDA
if valor > maior_venda:
    maior_venda = valor

#Cálculo dos resultados
if qtd_vendas > 0:
    media = total / qtd_vendas

else:
    print("Nenhuma venda foi registrada")



print("-------- FECHAMENTO DO  CAIXA ------- ") 
print(f"Total bruto arrecadado; R$ {total:.2f}")
print(f"Média do valor gasto por venda: {maior_venda:.2f}")
print(f"Maior venda realizada: {maior_venda:.2f}")






