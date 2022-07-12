num = int(input("Digite um numero inteiro: "))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input("Sua opção: "))
if opção == 1:
    print('{} Convertido para BINARIO é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} Convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} Convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print("Opção inválida, tente novamente. ")