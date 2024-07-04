# crie um caixa eletronico usando o while

print('-=-'*14)
print('{:^40}'. format('BANCO MAZ'))
print('-=-'*14)
valor = int(input('QUANTO VOCÊ QUER SACAR? R$'))
total = valor
totced = 0
ced = 50 # so sai cedulas de 50 reais
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print('O TOTAL DE {} CÉDULAS DE R${}'.format(totced, ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('-=-'*14)
print('VOLTE SEMPRE!!')
    