vel = int(input("Digite a velocidade do carro: "))
if vel > 80:
    print("voce ultrapassou o limite de velocidade e vai ser multado!")
    multa = (vel - 80)*7
    print("Sua multa foi de {} reais".format(multa))
else:
    print("Velocidade regular")