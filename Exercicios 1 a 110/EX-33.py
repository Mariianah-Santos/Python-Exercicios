# crie um codigo para saber qual numero é maior e o menor (fazer com 3 numeros)

v1 = int(input('DIGITE O NUMERO => '))
v2 = int(input('DIGITE O NUMERO => '))
v3 = int(input('DIGITE O NUMERO => '))
if v1 > v2 and v1 > v3:
    print('O MAIOR VALOR É {}'.format(v1))
if v2 > v1 and v2 > v3:
    print('O MAIOR VALOR É {}'.format(v2))
if v3 > v1 and v3 > v2:
    print('O MAIOR VALOR É {}'.format(v3))
if v1 < v2 and v1 < v3:
    print('O MENOR VALOR É {}'.format(v1))
if v2 < v1 and v2 < v3:
    print('O MENOR VALOR É {}'.format(v2))
if v3 < v1 and v3 < v2:
    print('O MENOR VALOR É {}'.format(v3))

# ou

v1 = int(input('DIGITE O NUMERO => '))
v2 = int(input('DIGITE O NUMERO => '))
v3 = int(input('DIGITE O NUMERO => '))
menor = v1
maior = v1
if v2<v1 and v2<v3:
    menor = v2
if v3<v1 and v3<v2:
    menor = v3
if v2>v1 and v2>v3:
    maior = v2
if v3>v1 and v3>v2:
    maior = v3
print('MAIOR {}'.format(maior))
print('MENOR {}'.format(menor))