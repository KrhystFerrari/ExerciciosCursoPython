nota1 = float(input("Primeiro semestre: "))
nota2 = float(input("Segundo semestre: "))
média = (nota1 + nota2) / 2
print("Tirando {:.1f} e {:.1f} a média do aluno foi {:.1f}! ".format(nota1, nota2, média))
if 7 > média >= 5:
    print("RECUPERAÇÃO!!")
elif média < 5:
    print("REPROVADO!!")
elif média >= 7:
    print("APROVADO!!")