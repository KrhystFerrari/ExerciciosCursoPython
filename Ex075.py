# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final mostre:
# a) Quantas vezes apareceu o valor 9.
# b) Em que posição foi digitado o primeiro valor 3.
# c) Quais foram os números pares.

num = (int(input('Digite um numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite o ultimo numero: ')))
print(f"Você digitou os valores {num}")
print(f"O valor 9 apareceu {num.count(9)} vezes")
if 3 in num:
       print(f"O numero 3 foi digitado na posição {num.index(3)+1}")
else:
       print("O valor 3 não foi digitado em nenhuma posição")
print("Os valores pares digitados foram ", end='')
for n in num:
       if n % 2 == 0:
           print(n, end=' ')

