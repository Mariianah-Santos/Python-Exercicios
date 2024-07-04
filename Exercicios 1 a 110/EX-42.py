# crie um codigo para saber se um triangulo é equilatero, isoceles ou escaleno

t1 = int(input('PRIMEIRO LADO: '))
t2 = int(input('SEGUNDO LADO: '))
t3 = int(input('TERCEIRO LADO: '))
if t1 < t2 + t3 and t2 < t3 + t1 and t3 < t1 + t2:
    print('PODE FAZER UM TRIANGULO', end=' ')
    if t1 == t2 == t3:
        print('\033[34;37mEQUILATERO \n TODOS OS LADOS DO TRIÂNGULO SÃO IGUAIS\033[m')
elif t1 == t2 or t2 == t3 or t3 == t1:
    print('\033[32;45mISOCELOS \n TENDO SÓ DOIS LADOS IGUAIS!\033[m')
else:
    print('\033[36;31mESCALENO NENHUM DOS LADOS SÃO IGUAIS!\033[m')