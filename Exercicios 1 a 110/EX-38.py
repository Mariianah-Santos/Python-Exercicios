# Crie um codigo para saber qual valor e maior e menor.

v1 = int(input('PRIMEIRO NÚMERO => '))
v2 = int(input('SEGUNDO NÚMERO => '))
if v1 > v2:
    print('O PRIMEIRO VALOR É O MAIOR \033[32m{}\033[m O SEGUNDO É O MENOR VALOR \033[31m{}'.format(v1, v2))
elif v2 > v1:
    print('O SEGUNDO VALOR É O MAIOR \033[32m{}\033[m O PRIMEIRO É O MENOR VALOR \033[31m{}'.format(v2, v1))
elif v1 == v2:
    print('NÃO TEM MAIOR OS DOIS SÃO IGUAIS \033[36m{}\033[m E \033[36m{}'.format(v1, v2))
