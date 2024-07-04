from time import sleep
import random
from operator import itemgetter
nfc = {}
print('-+-'*10)
print('     VALORES SORTEADOS!!')
print('-+-'*10)
for c in range(0, 4):
    nfc = random.randint(1, 6)
    print(f'O JOGADOR NUMERO {c}º JOGOU {nfc}')
    sleep(2)
ranking = list()
print()
print('\ RANKING DOS JOGADORES /')
ranking = sorted(nfc.items(), key=itemgetter(1), reverse=True)
for i, p in enumerate(ranking):
    print(f'O {i+1} LUGAR É DO JOGADOR {p[0]} QUE TIROU O NUMERO {p[1]}')

# ou 

from time import sleep
from random import randint
from operator import itemgetter
print('-+-'*10)
print('     VALORES SORTEADOS!!')
print('-+-'*10)
nfc = {'JOGADOR1': randint (1, 6),
        'JOGADOR2': randint(1, 6),
        'JOGADOR3': randint(1, 6),
        'JOGADOR4': randint(1, 6)}
for k, v in nfc.items():
    print(f'O JOGADOR NUMERO {k}º JOGOU {v}')
    sleep(2)
ranking = dict()
print()
print('\  RANKING DOS JOGADORES  /')
ranking = sorted(nfc.items(), key=itemgetter(1), reverse=True)
for i, c in enumerate(ranking):
    print(f'O {i} É DO JOGADOR {c[0]} {c[1]}')