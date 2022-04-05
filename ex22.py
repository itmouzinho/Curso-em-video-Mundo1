nome = input("Digite seu nome: ").strip() # Strip elimna os espaços antes e depois
print(nome.upper())
print(nome.lower())
lista = nome.split()
print("O seu primeiro nome tem {} letras".format(len(lista[0])))

print("Seu nome todo tem {} letras".format(len(nome) - nome.count(" ")))
