# Escreva um programa que solicite ao usuário um número e exiba se ele é positivo OU se ele é divisível por 3 OU se ele é menor que -10.

numero = int(input("Informe um numero => "))

if numero >= 0:
    print("NUMERO POSITVO")
    if (numero % 3) == 0:
        print("NUMERO {} É DIVISIVEL POR 3".format(numero))
    elif numero < 0:
        print("numero menor que 0")