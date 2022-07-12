print("{:=^105}".format(" LOJA01 "))
preço = float(input("Preço das compras: R$ "))
print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão de crédito
[ 4 ] 3x ou mais no cartão de crédito""")
opção = int(input("Qual a opção de pagamento? "))
if opção == 1:
    total = preço - (preço * 0.10)
elif opção == 2:
    total = preço - (preço * 0.05)
elif opção == 3:
    total = preço
    parcela = total / 2
    print("Sua compra será parcelada em 2x de R${:.2f}". format(parcela))
elif opção == 4:
    total = preço + (preço * 0.20)
    totparc = int(input("Quantas parcelas? "))
    parcela = total / totparc
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS! ".format(totparc, parcela))
else:
    total = preço
    print("OPÇÃO INVALIDA")
print("Sua compra de R${:.2f} vai custas R${:.2f} no final. ".format(preço, total))
