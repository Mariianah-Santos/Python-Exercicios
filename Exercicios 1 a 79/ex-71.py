# 30. Escreva um programa que solicite ao usuário um número e exiba se ele é primo ou não (um número é primo se é divisível apenas por 1 e por ele mesmo).

numero = int(input("Verificar numeros primos ate: "))
multiplo=0

for cont in range(2,numero):
    if (numero % cont == 0):
        print("Múltiplo de",cont)
        multiplo += 1

if(multiplo == 0):
    print("É primo")
else:
    print("Tem",multiplo," múltiplos acima de 2 e abaixo de",numero)
