'''
Dentro do pacote utilidadesCev que criamos no Ex111,
temos um módulo chamado dado. Crie uma função chamada
leiaDinheiro() que seja capaz de funcionar como a função input(),
mas com uma validação de dados para aceitar apenas valores que sejam monetários.
'''

from Exercicio112.utilidadesCeV import moeda
from Exercicio112.utilidadesCeV import dado

p = dado.leiaDinheiro('Digite o preço: ')
moeda.resumo(p, 20, 12)
