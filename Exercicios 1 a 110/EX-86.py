# crie um codigo para mostra a matriz dos numeros digitado 

matriz = list()
for c in range(0, 3):
    for c1 in range(0, 3):
        matriz.append(int(input(f'DIGITE UMA VALOR PARA [{c},{c1}] => ')))
print(f'( {matriz[:3]} )')
print(f'( {matriz[3:6]} )')
print(f'( {matriz[6:9]} )')

 # ou

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for c1 in range(0, 3):
        matriz[c][c1] = int(input(f'DIGITE UMA VALOR PARA [{c},{c1}] => '))
for c in range(0, 3):
    for c1 in range(0, 3):
        print(f'[{matriz[c][c1]:^5}]', end=' ')
    print()
