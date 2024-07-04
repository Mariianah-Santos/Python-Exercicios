# 22 - Escreva um programa que solicite ao usuário um número e exiba se ele é positivo, negativo ou igual a zero.

numero = int(input("Informe um numero => "))
if numero > 0:
    print(f" {numero} POSITIVO")
elif numero < 0: 
    print(f"{numero} NEGATIVO")
else:
    print("numero é igual a ZERO")