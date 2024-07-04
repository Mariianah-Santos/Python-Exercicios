# crie um codigo para saber a razao de uma numero 

primeiro = int(input('PRIMEIRO PA => '))
razão = int(input(R'RAZÃO => '))
decimo = primeiro + (10-1) * razão
for c in range(primeiro, decimo + razão, razão):
    print('{}'.format(c), end=' -> ')
print('ACABOU')