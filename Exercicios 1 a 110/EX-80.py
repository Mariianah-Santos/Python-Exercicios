# crie um codigo para o usuario digitar um valor 5 vezes e mostre a ordem dos numeros digitados e a posições deles

valor = []
for c in range(0, 5):
    num = (int(input('DIGITE UM VALOR => ')))
    if c == 0 or num > valor[-1]:
        valor.append(num)
        print('ADICIONADO AO FINAL DA LISTA...')
    else:
        pos = 0
        while pos < len(valor):
            if num <= valor[pos]:
                valor.insert(pos, num)
                print(f'ADICIONADO NA POSIÇÃO {pos} DA LISTA!')
                break
            pos += 1
print('OS VALORES EM ORDEM SÃO {}'.format(valor))