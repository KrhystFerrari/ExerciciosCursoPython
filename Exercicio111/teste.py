'''
Crie um pacote chamado utilidadesCeV que tenha dois módulos internos
chamados moeda e dado.
Transfira todas as funções utilizadas nos exercicios anteriores
para o primeiro pacote e deixe tudo funcionando.
'''

from Exercicio111.utilidadesCeV import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 20, 12)
