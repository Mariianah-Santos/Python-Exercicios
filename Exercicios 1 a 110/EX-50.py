# crie um codigo para soma todos os valores digitados e mostra quantos numeros foram digitados.

s = 0
for c in range (0, 6):
    num = int(input('DIGITE UM NUMERO => '))
    if num % 2 == 0:
        s = s + num
        
print('A SOMA É {}'.format(s))

# ou

s = 0
cont = 0
for c in range(0, 6):
    num = int(input('DIGITE UM NUMERO => '))
    if num % 2 == 0:
        s = s + num
        cont = cont + 1
print('A SOMA É {} O CONTADOR É {}'.format(s, cont))