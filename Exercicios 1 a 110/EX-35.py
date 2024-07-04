# Crie um codig para saber se 3 lados fazem um triangulo.

r1 = int(input('PRIMEIRA RETA => '))
r2 = int(input('SEGUNDA RETA => '))
r3 = int(input('TERCEIRA RETA => '))
if r1+r2 > r3 and r2+r3 > r1 and r3+r1 > r2:
    print('OS LADOS FORMAM UM TRIÂNGULO')
else:
    print('OS LADOS NÃO FORMAR UM TRIÂNGULO')