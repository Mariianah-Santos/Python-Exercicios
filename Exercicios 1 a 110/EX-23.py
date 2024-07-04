# crie um codigo que irá mostra a unidade,dezena, centena e milhar

n = int(input('DIGITE 4 NUMEROS =>'))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('ANALISANDO OS NUMERO {}'.format(n))
print('UNIDADE: {}'.format(u))
print('DEZENA:{}'.format(d))
print('CENTENA:{}'.format(c))
print('MILHAR:{}'.format(m))