# 21 Escreva um programa que solicite ao usuário um número e exiba se ele é par ou ímpar.

resposta = int(input("Digite um numero => "))
if resposta % 2 == 0:
    print("Numero dgitaido {} é PAR ".format(resposta))
else:
    print("Numero dgitaido {} é IMPAR ".format(resposta))
