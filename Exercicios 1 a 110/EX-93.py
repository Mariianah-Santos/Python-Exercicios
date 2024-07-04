# crie um codigo de futebol, onde deve mostra quantas partidas foram jogadas , o nomedo jogador(a) quantos gols fez pr partida e total de glols
futebol = {}
partidas = list()
futebol['nome'] = str(input('NOME DO JOGADOR OU JOGADORA: '))
tot = int(input('PARTIDAS JOGADAS: '))
for c in range(0, tot):
    partidas.append(int(input(f'QUANTOS GOLS {futebol["nome"]} FEZ NA {c+1} PARTIDA? ')))
futebol['gols'] = partidas[:]
futebol['tot'] = sum(partidas)
for k, v in futebol.items():
    print(f'o campo {k} tem valor {v}')
for r, m in enumerate(futebol["gols"]):
    print(f'=> NA {r+1} PARTIDA FEZ {m} GOLS')
print(f'TOTAL DE GOLS {futebol["tot"]}')