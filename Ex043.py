peso = float(input("Digite seu peso: (Kg) "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura ** 2)
print("Seu IMC é {:.1f}!".format(imc))
if imc < 18.5:
    print("Você está abaixo do peso! ")
elif 18.5 <= imc < 25:
    print("Você está no peso ideal, parabens!")
elif 25 <= imc < 30:
    print("Você está sobrepeso!")
elif 30 <= imc < 40:
    print("Você está obeso, cuidado!")
elif imc >= 40:
    print("Você está com obesidade morbida, procure um médico!")



