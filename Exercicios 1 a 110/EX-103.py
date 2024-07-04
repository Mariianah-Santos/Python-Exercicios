def ficha(n='<desconhecido>', g=0):
    print(f'O JOGADOR {n} FEZ {g} GOLS NO CAMPEONATO')


nome = str(input('NOME DO JOGADOR: '))
gol = str(input('GOLS: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(g=gol)
else:
    ficha(nome, gol)