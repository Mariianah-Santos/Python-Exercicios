pessoa = dict()
galera = list()
soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('NOME: '))
    while True:
        pessoa['sexo'] = str(input('SEXO [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERROR!! POR FAVOR, ESCOLHA UMA DAS OPÇÕES (M = MASCULINO) OU (F = FEMININO)')
    pessoa['idade'] = int(input('IDADE: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        r = str(input('QUER CONTINUAR? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('ERROR!! ESCOLHAR S OU N!')
    if r == 'N':
        break
print(f'A) AO TODO TEMOS {len(galera)} DE PESSOAS CADASTRADAS')
media = soma / len(galera)
print(f'B) A MEDIA DA IDADE É {media:5.2f}')
print('C) MULHERES CADASTRADAS FORA', end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}')
print('D) A MEDIA DAS PESSOAS ACIMA É', end=' ')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
print('>>>> ENCERRADO <<<<')