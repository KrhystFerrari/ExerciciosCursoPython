# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro,
# na ordem de colocação. Depois mostre:
# a) Apenas os 5 primeiros colocados.
# b) Os ultimos 4 colocados da tabela.
# c) Uma lista com os times em ordem alfabética.
# d) Em que posição na tabela está o time Chapecoense.

times = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't')
print("-=" * 20)
print(f"Lista de {times}")
print("-=" * 20)
print(f"Os 5 primeiros são {times[0:5]}")
print("-=" * 20)
print(f"Os quatro ultimos são {times[-4:]}")
print("-=" * 20)
print(f'Times em ordem alfabetica: {sorted(times)}')
print("-=" * 20)
print(f'A posição de h é {times.index("h")+1}ª posição')

