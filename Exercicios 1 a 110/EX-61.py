# crie um codigo pra descobri a razao de um numero

primeiro = int(input('PRIMEIRO PA => '))
razão = int(input(R'RAZÃO => '))
termo = primeiro
c = 1
while c <= 10:
    print('{}'.format(termo), end=' -> ')
    termo = termo + razão
    c = c + 1
print('ACABOU')