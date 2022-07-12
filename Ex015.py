d = int(input("Quantos dias o carro foi alugado? "))
km = float(input("Quantos km o carro rodou? "))
p = (d * 60) + (km * 0.15)
print("O preço do aluguel ficou em R${:.2f}".format(p))
