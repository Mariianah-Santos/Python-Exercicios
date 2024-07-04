# crie um codigo que mostre o seu primeir nome o ultimo

n = str(input('DIGITE O SEU NOME => ')).strip()
n = n.split()
print('SEU PRIMEIRO NOME:{}'.format(n[0]))
print('SEU ULTIMO NOME:{}'.format(n [len(n)-1]))