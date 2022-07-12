# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um numero entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessariios para vencer!

from random import randint

computador = randint(0, 10)
print("Olá sou o seu computador!! Acabei de pensar em um número entre 0 e 10 ")
print("Será que você consegue adivinhar qual foi? ")
acertou = False
palpite = 0
while not acertou:
    jogador = int(input("Qual o seu palpite? "))
    palpite = palpite + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais.. Tente outra vez. ")
        elif jogador > computador:
            print("Menos... Tente outra vez. ")
print("Acertou com {} tentativas. Parabens!! ".format(palpite))