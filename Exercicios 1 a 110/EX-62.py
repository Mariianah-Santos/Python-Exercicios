

primeiro = int(input('PRIMEIRO PA => '))
razão = int(input(R'RAZÃO => '))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        c = c + 1
        mais = int(input('quer colocar mais..?'))