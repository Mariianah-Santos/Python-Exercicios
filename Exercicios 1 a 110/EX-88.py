# crei um codigo para gerar numeros de sorteio

import random
from time import sleep
jogo = list()
lista = list()
print('='*40)
print('{:^40}'.format('JOGO DA VIRADA'))
print('='*40)
quant = int(input('QUANTOS JOGO VOCÊ QUER QUE EU SORTEIE? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        nfc = random.randint(1, 60)
        if nfc not in jogo:
            jogo.append(nfc)
            cont += 1
        if cont >= 6:
            break
    jogo.sort()
    lista.append(jogo[:])
    jogo.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO \033[30:41m{quant}\033[m JOGOS', '-=' * 3)
for i, l in enumerate(lista):
    print(f'\033[32mJOGO {i+1}: {l}\033[m')
    sleep(2)
print('-=' * 4, '< BOA SORTE!! >', '-=' * 4)