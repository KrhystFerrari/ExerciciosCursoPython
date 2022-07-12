'''
Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
- Quantidade de notas.
- A maior nota.
- A menor nota.
- A média da turma.
- A situação opcional.

Adicione também as docstrings da função.
'''


def notas(*n, sit=False):
    '''
    ->> Função para analisar notas e situações de varios alunos.
    :param n: uma ou mais notas dos alunos (aceita varias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da classe.
    by Krhys
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situaçao'] = "MTO BOM!!"
        elif r['média'] >= 5:
            r['situaçao'] = 'MAIS OU MENOS'
        else:
            r['situaçao'] = "HORRIVEL"
    return r


resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)
#help(notas)