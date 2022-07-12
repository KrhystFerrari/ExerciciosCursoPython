distancia = float(input("Qual a distancia da sua viagem? "))
print("Você esta prestes a iniciar uma viagem de {:.0f}km".format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print("E o preço da sua passagem sera R${:.2f}!".format(preço))
