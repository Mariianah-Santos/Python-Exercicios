# crie um codigo usando lista e sortei numeros. Mostre o maior numero sorteado e o menor sorrteado
import random
numero = 0
pc_escolhe = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))
print("o numero sorteado foi... {}".format(pc_escolhe))
if numero in pc_escolhe:
    print('{}'.format(numero), end=' ')
    print('O MAIOR NUMERO SORTEADO FOI {}'.format(max(pc_escolhe)))
    print('O MENOR NUMERO SORTEADO FOI {}'.format(min(pc_escolhe)))