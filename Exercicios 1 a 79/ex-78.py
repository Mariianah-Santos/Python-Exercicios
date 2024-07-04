# Escreva um programa que solicite ao usuário uma letra e exiba se ela é uma letra maiúscula OU uma letra minúscula.
letra = str(input("Digite uma letra => "))

if letra == (letra.upper()):
    print("Maiuscula")
else: 
    print("MInuscula")

# ou 

letra = str(input("Digite uma letra => "))

if letra == (letra.upper()):
    print("Maiuscula")
elif letra == (letra.lower()):
    print("MInuscula")

