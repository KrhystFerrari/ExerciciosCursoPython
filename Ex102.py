'''
Crie um programa que tenha uma função fatorial()
que receba dois parametros: o primeiro que indique o número a calcular
e o outro chamado show, que será um valor lógico (opcional) indicando se
será mostrado ou não na tela o processo de cálculo fatorial.
'''


def fatorial(n, show=False):
    '''
    -> Calcula o fatorial de um número.
    :param n: o número a ser calculado.
    :param show: mostrar ou nao a conta
    :return: o valor fatorial de um numero n.
    by Krhys
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#print(fatorial(5, show=True))
help(fatorial)