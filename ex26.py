frase = str(input("Digite uma frase: ")).strip()
print("A letra a aparece {} vezes".format(frase.upper().count("A")))
print("A primeira letra A apareceu na posição {}".format(frase.upper().find("A")))
print("A ultima letra A apareceu na posição {}".format(frase.upper().rfind("A"))) ## Rfind começa a contar de tras pra frente.