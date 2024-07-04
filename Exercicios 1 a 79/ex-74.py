# Escreva um programa que solicite ao usuário um número e exiba se ele é múltiplo de 2 E de 3.

numero = int(input("Digite o numero => "))

if numero % 3 == 0:
    print("Numero multiplo de 3: numero ({})".format(numero))
elif numero % 2 == 0:
    print("Numero multiplo de 2: numero ({})".format(numero))
else:
    print("não há nenhum multiplo desse numero: entre o 2 e o 3 {}".format(numero))