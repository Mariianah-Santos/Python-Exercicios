# crie um codigo para descobri a fatorial de um numero

from math import factorial
num = int(input('DIGITE O NUMERO DA FATORIAL => '))
f = factorial(num)
print('O FATORIAL DO NUMERO {} É {}'.format(num, f))

# ou 

num = int(input('DIGITE O NUMERO DA FATORIAL => '))
c = num
f = 1
print('CALCULANDO {}!='.format(num), end='')
while c > 0:
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else '= {}'.format(f), end=' ')
    f = f * c
    c = c - 1