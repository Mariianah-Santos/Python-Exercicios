# Escreva um programa que solicite ao usuário duas palavras e exiba se ambas têm o mesmo número de caracteres OU se a primeira palavra é maior que a segunda.

palavra_1 = str(input("informe a primeria palavra => "))
palavra_2 = str(input("informe a segunda palavra => "))

if len(palavra_1) == len(palavra_2):
    print("Tem o mesmo numeros de Caracteres P1 ( {} ) e P2 ( {} ) ".format(palavra_1, palavra_2))
else:
    print("não são iguais P1 ( {} ) e P2 ( {} ) ".format(palavra_1, palavra_2))