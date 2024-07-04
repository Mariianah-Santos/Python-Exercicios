# crie uma função LISTA que mostre os numeros por extenso


num = ('zero', 'um', 'dois', 'três', 'quatro',
       'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
       'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
       'dezoito', 'dezenove', 'vinte')
while True:
    resp = int(input('QUAL NUMERO VOCÊ QUER VER EM EXTENSO? ~DE 0 ATÉ 20~ '))
    if 0 <= resp <= 20:
        break
    print('TENTE NOVAMENTE.', end=' ')
print('VOCÊ DIGITOU O NUMERO {}'.format(num[resp]))

# ou

r = 'S'
num = ('zero', 'um', 'dois', 'três', 'quatro',
       'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
       'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
       'dezoito', 'dezenove', 'vinte')
while True:
    resp = int(input('QUAL NUMERO VOCÊ QUER VER EM EXTENSO? ~DE 0 ATÉ 20~ '))
    print('VOCÊ DIGITOU O NUMERO {}'.format(num[resp]))
    if 0 <= resp <= 20:
        break
    print('TENTE NOVAMENTE.', end=' ')
while r in 'S':
    r = str(input('QUER TENTAR NOVAMENTE? [S/N] ')).upper().strip()[0]
    if r == 'S':
        resp = int(input('QUAL NUMERO VOCÊ QUER VER EM EXTENSO? ~DE 0 ATÉ 20~ '))
        print('VOCÊ DIGITOU O NUMERO {}'.format(num[resp]))

print('OBRIGADA POR USAR O SITE!!')