import random
from time import sleep
def sorteio(lista):
    print('SORTEADOS OS NUMEROS DA LISTA:', end=' ')
    for c in range(0, 5):
        num = random.randint(1, 20)
        lista.append(num)
        print(f'{num}', end=' ', flush=True)
        sleep(0.3)
    print('PRONTO')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'SOMANDO OS VALORES PARES{lista} TEMOS {soma}')


numeros = list()
