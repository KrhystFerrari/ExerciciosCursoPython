# Refaça o exercicio 09, porém agora usando um "laço" for

num = int(input("Digite um numero para mostrar sua tabuada: "))
for c in range(1, 11):
    print(f"{num} x {c:2} = {num * c}")
