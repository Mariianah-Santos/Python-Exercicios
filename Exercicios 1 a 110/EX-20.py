# Crie um codigo que pergunte o nome de 4 alunos e embaralhe as posições

import random
n1 =str(input('DIGITE SEU NOME => '))
n2 =str(input('DIGITE SEU NOME => '))
n3 =str(input('DIGITE SEU NOME => '))
n4 =str(input('DIGITE SEU NOME => '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(lista)

# ou

from random import shuffle
n1 =str(input('DIGITE SEU NOME => '))
n2 =str(input('DIGITE SEU NOME => '))
n3 =str(input('DIGITE SEU NOME => '))
n4 =str(input('DIGITE SEU NOME => '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(lista)