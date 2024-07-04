from time import sleep
def cont():
    print(f'CONTAGEM DE 1 ATE 10 EM 1 E 1:')
    for c in range(1, 11):
        print(c, end=' ')
        sleep(0.5)
    print()
    print('~'*30)
    print(f'CONTAGEM DE 10 ATE 1 EM 2 EM 2:')
    for c1 in range(10, 1, -2):
        print(c1, end=' ')
        sleep(0.5)
    print()
    print('~' * 30)
def c2():
        print('AGORA VOCÊ VAI ESCOLHER O NUMEROS :) ')
        inicio = int(input('INICIO: '))
        fim = int(input('FIM: '))
        passo = int(input('PASSO: '))
        print('-' * 30)
        if passo < 0:
            passo *= -1
        if passo == 0:
            passo = 1
        if inicio < fim:
            con = inicio
            while con <= fim:
                print(f'{con}', end=' ', flush=True)
                sleep(0.5)
                con += passo
            print('FIM')
        else:
            con = inicio
            while con >= fim:
                print(f'{con}', end=' ', flush=True)
                sleep(0.5)
                con -= passo
            print('FIM')


cont()
c2()

# ou

from time import sleep
def cont(i, f, p):
    print('~'*30)
    print(f'CONTAGEM DE {i} ATE {f} EM {p} E {p}:')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        con = i
        while con <= f:
            print(f'{con}', end=' ', flush=True)
            sleep(0.5)
            con += p
        print('FIM')
    else:
        con = i
        while con >= f:
            print(f'{con}', end=' ', flush=True)
            sleep(0.5)
            con -= p
        print('FIM')


cont(1, 10, 1)
cont(10, 0, 2)
print('AGORA VOCÊ VAI ESCOLHER O NUMEROS :) ')
inicio = int(input('INICIO: '))
fim = int(input('FIM: '))
passo = int(input('PASSO: '))
cont(inicio, fim, passo)