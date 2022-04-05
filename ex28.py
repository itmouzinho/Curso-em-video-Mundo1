from random import randint

num = int(input("Digite um numero de 0 a 5: "))
r = randint(0, 5)
if num == r:
    print('Parabens voce acertou o numero, que eh: {}'.format(r))
else:
    print("Que pena, voce errou")
