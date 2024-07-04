# 24. Escreva um programa que solicite ao usuário uma letra e exiba se ela é uma vogal ou uma consoante.

palavra = str(input("informe qual quer saber => "))
if palavra == 'a' or palavra == 'e' or palavra == 'i' or palavra == 'o' or palavra == 'u':
    print(f"{palavra} é uma vogal")

else: 
    print(f"{palavra} é uma consoate")