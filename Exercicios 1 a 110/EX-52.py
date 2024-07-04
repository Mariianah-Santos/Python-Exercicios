# CRIE UM CODIGO PARA SABER QUANTOS NUMEROS SÃO DIVISIVEIS E QUAIS SÃO PRIMOS

numero = int(input("Digite um numero => "))
total = 0 
for c in range(1, numero+1):
    if numero % c == 0:
        print('\033[34m', end= ' ')
        total += 1
    else:
         print('\033[31m', end= ' ')
    print('{}'.format(c), end= ' ')

print('\n \033[m TOTAL DE VEZES DIVISIVEIS {}'.format(total))
if total == 2:
    print('POR ISSO ELE É PRIMO')
else:
    print('POR ISSO NÃO É PRIMO')