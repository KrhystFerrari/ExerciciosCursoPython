import time
from random import randint
from time import sleep
computador = randint(0, 5) #faz o compútador "pensar"
time.sleep(5)
print("-=-" * 20)
print("Vou pensar em um numero entre 0 e 5..Tente adivinhar... ")
print("-=-" * 20)
jogador = int(input("Em que numero eu pensei? ")) #jogador tenta adivinhar
print("PROCESSANDO.....")
sleep(5)
if jogador == computador:
    print("PARABENS!!! Eu pensei no nomero {}. Você conseguiu me vencer!".format(computador))
else:
    print("Ganhei! EU pensei no numero {} e nao no numero {}".format(computador, jogador))
