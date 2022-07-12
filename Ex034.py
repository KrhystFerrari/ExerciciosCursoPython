salario = float(input("Qual é o salario do funcionario? R$"))
if salario <= 1250:
    novo = salario + (salario * 0.15)
else:
    novo = salario + (salario * 0.10)
print("Quem ganhava R${:.2f}, passa a ganhar R${:.2f}".format(salario, novo))
