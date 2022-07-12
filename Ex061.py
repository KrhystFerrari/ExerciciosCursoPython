# Refaça o desafio 051, lendo  o primeiro termo  de uma PA, mostrando os 10 primeiros termos
# da progressão usando estrutura while.

print("GERADOR DE PA")
print("-=" * 10)
primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão da PA: "))
termo = primeiro
cont = 1
while cont <= 10:
    print("{} → ".format(termo), end='')
    termo += razão
    cont += 1
print("FIM")
