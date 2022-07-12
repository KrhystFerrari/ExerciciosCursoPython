'''
Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante a função input() do Python,
só que fazendo a validação para aceitar apenas um valor númerico.
Ex:
n = leiaInt('Digite um n')
'''

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
        else:
            print('\033[0;31mERRO!! Digite um número válido.\033[m')
        if ok:
            break
    return valor

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}. ')