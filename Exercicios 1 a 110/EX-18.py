# crie um codigo que pergunteo angulo e mostre o seno, conseno, tangeno

import math
an = float(input('DIGITE O ÂNGULO => '))
seno = math.sin(math.radians(an))
print('O ÂNGULO DO SENO DE {} É {:.2f}'.format(an, seno))
cos = math.cos(math.radians(an))
print('O ÂNGULO DE CONSENO DE {} É {:.2f}'.format(an, cos))
tan = math.tan(math.radians(an))
print('O ÂNGULO DE TANGENO DE {} É {:.2f}'.format(an, tan))

# ou

from math import radians, sin, cos, tan
an = float(input('DIGITE O ÂNGULO => '))
seno = sin(radians(an))
print('O ÂNGULO DO SENO DE {} É {:.2f}'.format(an, seno))
cos = cos(radians(an))
print('O ÂNGULO DE CONSENO DE {} É {:.2f}'.format(an, cos))
tan = tan(radians(an))
print('O ÂNGULO DE TANGENO DE {} É {:.2f}'.format(an, tan))