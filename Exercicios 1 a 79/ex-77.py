# Escreva um programa que solicite ao usuário um número e exiba se ele é maior que 10 E menor que 20 OU se ele é maior que 30 E menor que 40.

numero = int(input("Informe um numero: "))

if numero > 10 and numero < 20:
    print("O numero é {} maior que 10".format(numero))
elif numero >= 30 or numero < 40:
    print("O numero é {} é maior que 30".format(numero))
else: 
    print("Digite um numero valido")