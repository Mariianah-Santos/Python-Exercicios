# crei um codigo de matriz, mostres os numeros pares, impares a soma dos numeros pares. Qual o maior numero digitado na segunda linha e z soma da terceira  coluna

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = list()
soma = 0
maior = 0
scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'DIGITE UMA VALOR PARA [{l},{c}] => '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
            par.append(matriz[l][c])
for l in range(0, 3):
    scol += matriz[l][2]
for c in range(0, 3):
        if c == 0:
            maior = matriz[1][c]
        elif matriz[1][c] > maior:
            maior = matriz[1][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'\033[34m[{matriz[l][c]:^5}]\033[m', end=' ')
    print()
print(f'OS NUMEROS PARES DIGITADS SÃO => \033[32m{sorted(par)}\033[m A SOMA DESSES NUMEROS PARES É => \033[31m{soma}\033[m')
print(f'O MAIOR NUMERO DA SEGUNDA LINHA É => \033[37m{maior}\033[m')
print(f'A SOMA DOS NUMEROS DA TERCEIRA COLUNA É => {scol}')
