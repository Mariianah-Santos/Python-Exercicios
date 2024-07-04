# crie um codigo. Pergunte alguns mumeros e mostre na tela a posições e quais os numeros que estao na posição.

valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'DIGITE O {cont+1}º NUMERO => ')))
for p, n in enumerate(valores):
    print(f'OS NUMEROS ESTÃO NA POSIÇÃO {p} E OS VALORES SÃO {n}')
print(f'O NUMERO MAIOR É {(max(valores))} E ESTA POSIÇÃO {valores.index(max(valores))}')
print(f'O MENOR NUMERO É {min(valores)} E ESTA NA POSIÇÃO {valores.index(min(valores))}')
print('VOCE DIGITOU ESSES NUMEROS {}'.format(valores))

# ou 

valores = list()
maior = 0
menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'DIGITE O {cont}º NUMERO => ')))
    if cont == 0:
        maior = menor = valores [cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
for p, n in enumerate(valores):
    print(f'OS NUMEROS ESTÃO NA POSIÇÃO {p} E OS VALORES SÃO {n}')
print(f'O NUMERO MAIOR É {(max(valores))} E ESTA POSIÇÃO {valores.index(max(valores))}')
print(f'O MENOR NUMERO É {min(valores)} E ESTA NA POSIÇÃO {valores.index(min(valores))}')
print('VOCE DIGITOU ESSES NUMEROS {}'.format(valores))
print(f'O MAIOR VALOR É {maior} QUE ESTA NA POSIÇÃO ', end= ' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end=' ')
print(f'O MENOR VALOR É {menor} E ESTA NA POSIÇÃO', end= ' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end=' ')