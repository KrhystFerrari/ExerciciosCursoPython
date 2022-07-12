# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# A) Qual o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input("Nome do produto: "))
    preço = float(input("Preço R$ "))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA!! '))
print(f"O total da compra foi R${total:.2f} ")
print(f"Temos {totmil} produto(s) custando mais de R$1000.00 ")
print(f"O produto mais barato foi {barato} e custa R${menor:.2f}")
