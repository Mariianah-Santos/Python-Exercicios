#crie a tabuada usando a função for

s = 0
for c in range(0, 11):
    s = c * c
    print('[{}] x [{}] = [{}]'.format(c, c, s))
# ou
r = int(input('DIGITE UM NUMERO QUE QUER SABER A TABUADA => '))
for c in range(1, 11):
    print('[{}] x [{}] = [{}]'.format(r, c, r*c))