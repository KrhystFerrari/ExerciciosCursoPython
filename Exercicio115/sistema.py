'''
Crie um pequeno sistema modularizado que permita cadastrar
pessoas pelo seu nome e idade e em um arquivo de texto simples
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas
as pessoas cadastradas.
'''
from Exercicio115.lib.interface import *
from Exercicio115.lib.arquivo import *
from time import sleep

arq = 'curso.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar novas Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...')
        break

    else:
        print('ERRO! Digite uma opção válida! ')
    sleep(2)
