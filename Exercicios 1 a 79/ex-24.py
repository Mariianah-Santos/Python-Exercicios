# Como criar uma lista de números ímpares em Python?

lista = []

numero = int(input("numero: "))
if numero % 2 == 1:
    lista.append(numero)

print(lista)