'''
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo e realize uma contagem
Seu programa tem que realizar três contagens através da função criada:
 a) De 1 até 10, de 1 em 1.
 b) De 10 até 0, de 2 em 2.
 c) Uma contagem personalizada.
'''

from time import sleep


def lin():
    print('-=' * 30)


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até o {f} de {p} em {p}.')
    sleep(2)


    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print("FIM")


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de fazer a contagem!! ')
lin()
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
lin()
