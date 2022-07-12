# Faça um programa que calcule a soma entre todos os numeros impares que são multiplos de 3
# E que se encontram em um intervalo de 1 até 500.

soma = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        count = count + 1
        soma = soma + c
print("A soma de todos os {} valores solicitados é {}".format(count, soma))
