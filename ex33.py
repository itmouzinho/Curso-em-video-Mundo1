num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

if num1 > num2 > num3:
    print("o maior numero é {}, seguido por {} e seguido por {}".format(num1, num2, num3))
elif num2 > num1 > num3:
    print("o maior numero é {}, seguido por {} e seguido por {}".format(num2, num1, num3))
elif num2 > num3 > num1:
    print("o maior numero é {}, seguido por {} e seguido por {}".format(num2, num3, num1))
elif num1 > num3 > num2:
    print("o maior numero é {}, seguido por {} e seguido por {}".format(num1, num3, num2))
elif num3 > num2 > num1:
    print("o maior numero é {}, seguido por {} e seguido por {}".format(num3, num2, num1))
elif num3 > num1 > num2:
    print("o maior numero é {}, seguido por {} e seguido por {}".format(num3, num1, num2))