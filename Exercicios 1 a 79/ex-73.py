# Escreva um programa que solicite ao usuário um número e exiba se ele é positivo E ímpar.

nuemro = int(input("informe um numero: "))

if nuemro > 0 and nuemro % 2 == 1:
    print("numero {} é impar/positivo".format(nuemro))
elif nuemro > 0 and nuemro % 2 == 0:
    print("numero {} é par/positivo".format(nuemro))
elif nuemro < 0 and nuemro % 2 == 1:
    print("numero {} é impar/negativo".format(nuemro))
elif nuemro < 0 and nuemro % 2 == 0:
    print("numero {} é par/negativo".format(nuemro))
