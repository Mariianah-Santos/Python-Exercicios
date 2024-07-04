# Como criar uma lista de números pares em Python?

lista = []

numero = int(input("numero: "))
if numero % 2 == 0:
    lista.append(numero)

print(lista)