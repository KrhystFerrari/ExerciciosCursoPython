import random

letras_min = 'abcdefghijklmnopqrstuvwxyz'
letras_mai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
simb = '!@#$%¨&*()/\?'

usar = letras_min + letras_mai + num + simb
tamanho = 8

senha = ''. join(random.sample(usar, tamanho))

print(f"Sua senha gerada foi: {senha} ")


