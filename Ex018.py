import math
ang = float(input("Digite um angulo: "))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print(" O seno do angulo {} é {:.2f}. \n O Cosseno é {:.2f}. \n E sua tangente é {:.2f}".format(ang, seno, cosseno, tangente))
