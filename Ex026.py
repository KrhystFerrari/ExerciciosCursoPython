frase = str(input("Diga uma frase: ")).upper().strip()
print("A letra 'a' aparece {} vezes. ".format(frase.count('A')))
print("A primeira letra 'a' aparece na posição {}".format(frase.find('A')+1))
print("E a letra 'a' aparece por ultimo na posição {}".format(frase.rfind('A')+1))
