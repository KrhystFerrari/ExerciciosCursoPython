# Crie um programa que vai ler varios numeros e colocar em uma lista.
# Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores impares digitados, respectivamente
# Ao final mostre o conteudo das 3 listas geradas.

numeros = list()
pares = list()
impares = list()
while True:
    numeros.append(int(input("Digite um valor: ")))
    resp = str(input('Quer continuar? [S/N] ' ))
    if resp in "Nn":
        break
for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('=-' * 30)
print(f'A lista completa é {numeros}')
print(f'A lista de numeros pares é {pares}')
print(f'A lista de numeros impares é {impares}')
print('=-' * 30)
