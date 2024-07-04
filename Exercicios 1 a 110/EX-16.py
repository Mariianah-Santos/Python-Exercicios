# CRIE UM CODIGO QUE DO TIPO FLOAT E PEÇA A INTEIRA DO VALOR

import math
num = float(input('DIGITE UM NUMERO => '))
nr = math.trunc(num)
print('A PORÇAO INTEIRA DE {} É {}'.format(num, nr))

# OU

from math import trunc
num = float(input('DIGITE UM NUMERO => '))
nr = trunc(num)
print('A PORÇAO INTEIRA DE {} É {}'.format(num, nr))