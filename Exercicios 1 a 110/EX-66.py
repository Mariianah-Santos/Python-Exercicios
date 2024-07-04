# crie um codigo que mostre a soma dos numeros digitados e quantas vezes foram digitados
num = 1
soma = cont = 0
print('-=-'*20)
print('\033[30mDIGITE VARIOS NUMEROS!!! O PROGRAMA IRÁ PARAR QUANDO DIGITAR \033[34m[999]\033[m')
print('-=-'*20)
while True:
    num = int(input('DIGITE O NUMERO => '))
    if num == 999:
        break
    soma += num
    cont += 1
print('FORAM DIGITADOS \033[32m{}\033[m NUMEROS \nA SOMA DOS NUMEROS É \033[31m{}'.format(cont, soma))