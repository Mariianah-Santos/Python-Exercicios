# 19. Escreva um programa que solicite ao usuário dois números e exiba se o
# primeiro número é maior, menor ou igual ao segundo número.

num_1 = int(input("Número 1: "))
num_2 = int(input("Número 2: "))

if num_1 > num_2:
    print("numero um é maior")
elif num_1 < num_2:
    print("numero um é menor")
elif num_1 == num_2:
    print("numeros iguais")