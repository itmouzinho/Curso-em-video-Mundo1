salario = float(input("Digite seu salario: "))
if salario > 1250:
    salario = salario*1.1
    print("Seu novo salario é de: {:.3f}".format(salario))
elif salario <= 1250:
    salario = salario*1.15
    print("Seu novo salario é de: {:.3f}".format(salario))