casa = float(input("Qual o valor da casa desejada? "))
salario = float(input("Qual o seu salário? "))
anos = int(input("Em quantos anos deseja pagar? "))
parcela = casa / (anos * 12)
erro = salario * 0.30
print("A casa desejada vale R${:.2f}, você gostaria de pagar em {} anos e seu salário é de R${:.2f}. Vou executar a sua analise!! ".format(casa, anos, salario))
if parcela > erro:
    print("Desculpe, o valor da parcela é muito alto para o seu salário. ")
else:
    print("Parabens, você foi aprovado!! Vamos dar continuidade ao seu pedido de emprestimo! ")