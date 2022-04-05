distancia = float(input("Digite a distancia da viagem: "))
if distancia <= 200:
    passagem = distancia*0.5
    print("O preço da passagem é: {}".format(passagem))
elif distancia > 200:
    passagem = distancia*0.45
    print("O preço da passagem é: {}".format(passagem))