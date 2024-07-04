# crie um codigo para cadastra pessoas e seus peso. Pergunte se o usuario quer add mais pessoas.
# mostra pessoas com menos de 70 sao leves, maior que esse valor é pesado



pessoa = list()
dado = list()
r = 'S'
cont = 0
maior = menor = 0
mm = mn = 0
print('-§-'*10)
while r in 'S':
    dado.append(str(input('NOME => ')))
    dado.append(float(input('PESO => ')))
    if len(pessoa) == 0:
        mm = mn = dado[1]
    else:
        if dado[1] > mm:
            mm = dado[1]
        elif dado[1] < mn:
            mn = dado[1]
    r = str(input('QUER CONTINUAR? [S/N] => ')).upper().strip()[0]
    pessoa.append(dado[:])
    dado.clear()
    cont += 1
for peso in pessoa:
    if peso[1] <= 70:
        print(f'{peso[0]} SÃO PESOS LEVES')
        menor += 1
    elif peso[1] >= 100:
        print(f'{peso[0]} SÃO PESOS PESADOS')
        maior += 1

print('-§-'*10)
print(f'PESSOAS CADASTRA => {cont}')
print(f'[{maior}] pessoas com pesos maior que 100')
print(f'[{menor}] pessoas com pesos menor que 70')
print(f'PESSOAS CADASTRAS E SEUS PESOS: {pessoa}')
print(f'PESSOA DE MAIOR PESO {mm} E DE MENOR PESO {mn}')
for p in pessoa:
    if p[1] == mm:
        print(f'MAIOR PESO FOI => {p[0]}')
for p in pessoa:
    if p[1] == mn:
        print(f'MENOR PESO FOI => {p[0]}')
print('-§-'*10)