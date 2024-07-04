def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERROR!! DIGITE UM NUMERO VALIDO!\033[m')
        if ok:
            break
    return valor

n = leiaint('DIGITE UM NUMERO: ')
print(f'VOCE ACABOU DE DIGITAR UM NUMERO {n}')