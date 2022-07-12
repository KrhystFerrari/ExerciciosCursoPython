import math
num1 = float(input("Cateto oposto: "))
num2 = float(input("Cateto adjacente: "))
hip = math.hypot(num1, num2)
print("A hipotenusa dos comprimentos {:.0f} e {:.0f} é igual a {:.2f}".format(num1, num2, hip))
