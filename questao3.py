
#Menu Interativo do Caixa com Match/case

#valor da venda
valor = 500.00

print("---- Forma de pagamento ---- ")
print("1 -  A vista em dinheiro/pix")
print("2 - Cartão de débito")
print("3- Cartão e crédito")
print("4 - Cartão de crédito parcelado")

#escolher o método de pagamento
forma_pagamento = int(input("Escolha o método de pagamento: \n"))

match forma_pagamento:
    case 1:
        valor_final = valor - (valor * 0.10)
        print("Pagamento a vista em dinheiro/pix ")
        print(f"valor final: {valor_final:.2f}")

    case 2:
        valor_final = valor - (valor * 0.05)
        print("Pagamento cartão de débito")
        print(f"valor_final : {valor_final:.2f}")

    case 3:
        valor_final = valor 
        print("Pagamento Cartão de crédito")
        print(f"valor_final : {valor:.2f}")

    case 4:
        valor_final = valor + (valor * 0.10) 
        print("Pagamento crédito parcelado")
        print(f"valor_final : {valor_final:.2f}")      
    



