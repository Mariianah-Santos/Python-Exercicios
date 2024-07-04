time = list()
futebol = {}
partidas = list()
while True:
    futebol.clear()
    futebol['nome'] = str(input('NOME DO JOGADOR OU JOGADORA: '))
    tot = int(input('PARTIDAS JOGADAS: '))
    for c in range(0, tot):
        partidas.append(int(input(f'QUANTOS GOLS {futebol["nome"]} FEZ NA {c+1} PARTIDA? ')))
    futebol['gols'] = partidas[:]
    futebol['tot'] = sum(partidas)
    time.append(futebol.copy())
    while True:
        r = str(input('QUER CONTINUAR? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('ERROR! POR FAVOR DIGITE (S = SIM) OU (N = NÃO)')
    if r == 'N':
        break
print('-=-'*15)
print('cod', end=' ')
for i in futebol.keys():
    print(f'{i:>10}', end=' ')
print()
print('-'*45)
for k, v in enumerate(time):
    print(f'{k:>4}', end='  ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*45)
while True:
    busca = int(input('QUAL DADO DOS JOGADORES VOCÊ QUER VER? (999 PARA PARAR) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'error! não existe jgador com essa {busca}')
    else:
        print(f'LEVATAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    NO JOGO {i+1} FEZ {g} GOLS')
for k, v in futebol.items():
    print(f'o campo {k} tem valor {v}')
for r, m in enumerate(futebol["gols"]):
    print(f'=> NA {r+1} PARTIDA FEZ {m} GOLS')
print(f'TOTAL DE GOLS {futebol["tot"]}')
print('>>> VOLTE SEMPRE <<<')