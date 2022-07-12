# Crie um programa que leia a data de nascimento de sete pessoas.
# No final, mostre quantas pessoas não atingiram a maioridade e quantas ja são maiores.

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for p in range (1, 8):
    nasc = int(input("Em que ano a {}ª pessoa nasceu: ".format(p)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print("Ao todo tivemos {} pessoas maiores de idade.".format(totmaior))
print("E também tivemos {} menores de idade.".format(totmenor))
