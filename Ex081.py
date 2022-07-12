# Crie um programa que vai ler varios numeros e colocar em uma lista.
# Depois disso, mostre:
# a) Quantos numeros foram digitados.
# b) A lista de valores, ordenada de forma decrescente.
# c) Se o valor 5 foi digitado e está ou não na lista.

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input("Quer constinuar? [S/N]"))
    if resp in 'Nn':
        break
print('=-' * 30)
print(f"Você digitou {len(valores)} elementos.")
valores.sort(reverse=True)
print(f'Os valores  em ordem decrescente são {valores}')
if 5 in valores:
    print("O valor 5 faz parte da lista!")
else:
    print('O valor 5 não foi encontrado na lista!')
print('=-' * 30)