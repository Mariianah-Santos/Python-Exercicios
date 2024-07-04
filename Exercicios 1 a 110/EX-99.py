from time import sleep
def maior(*num):
    cont = maior = 0
    print('ANALISANDO OS NUMEROS...')
    sleep(0.5)
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'FORAM INFORMADOS {cont} VALORES')
    print(f'O MAIOR VALOR INFORMADO É {maior}')
    print('-'*40)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()