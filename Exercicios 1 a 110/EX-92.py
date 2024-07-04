# crie um codigo para saber se o clente ja pode se apoesenta ou quando vai

from datetime import date
pessoa = {}
for c in range(0, 1):
    pessoa['nome'] = str(input('NOME: '))
    pessoa['ano'] = int(input('ANO DE NASCIMENTO: '))
    ano = date.today().year
    pessoa['idade'] = ano - pessoa['ano']
    pessoa['carteira'] = int(input('CARTEIRA DE TRABALHO (0 NÃO TEM): '))
    if pessoa['carteira'] != 0:
        pessoa['anoc'] = int(input('ANO DE CONTRATAÇÃO: '))
        pessoa['sal'] = float(input('SEU SALÁRIO R$ '))
        pessoa['apos'] = pessoa['idade'] + (pessoa['anoc'] + 35) - date.today().year
print(f'NOME DO CLIENTE: {pessoa["nome"]}')
print(f'A IDADE DE {pessoa["nome"]} É {pessoa["idade"]}')
print(f'CTPS É {pessoa["carteira"]}')
print(f'O ANO QUE O CLIENTE FOI CONTRATADO É DE {pessoa["anoc"]}')
print(f'SALÁRIO ATUAL R${pessoa["sal"]}')
print(f'{pessoa["nome"]} VAI SE APOSENTAR COM {pessoa["apos"]} ANOS')