# crie um codigo para soma todos os valores impares de 1 ate 500 e dizer o acumulo

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A SOMA DE TODOS OS VALORES É {} E O ACULADO É {}'.format(soma, cont))