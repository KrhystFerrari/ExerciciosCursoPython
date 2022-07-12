# Crie um programa onde o usuario pode digitar varios valores numericos e cadastre-os em uma lista.
# Caso o numero já exista lá dentro , ele não será adicionado .
# No final serão exibidos todos os valores unicos digitados, em ordem crescente.

numeros = list()
while True:
    n = int(input("Digite um valor: "))
    if n not in numeros:
        numeros.append(n)
        print("Valor adicionado com sucesso! ")
    else:
        print("Valor duplicado! Não vou adicionar... ")
    r = str(input('Quer continuar? [S/N] '))
    if r in "Nn":
        break
print('=-' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}')
print('=-' * 30)
