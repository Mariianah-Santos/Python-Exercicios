# crie um codigo para saber quem tem o maior peso e o menor peso

menor = 0 
maior = 0
for c in range(1, 5):
    peso = float(input("Informe seu peso => "))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso >= maior:
            maior = peso
        elif peso <= menor:
            menor = peso
print("maior {}".format(maior))
print("menor {}".format(menor))