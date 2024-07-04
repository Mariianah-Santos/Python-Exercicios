# crie um codigo e converta para binario, octal e hexadecimal

num = int(input('DIGITE UM NUMERO INTEIRO => '))
print('''ESCOLHA UMA DAS BASE DE CONVERSÕES:
[1] BINARIO 
[2] OCTAL 
[3] HEXADECIMAL''')
opc = int(input('SUA OPÇÃO: '))
if opc == 1:
    print('{} CONVERTIDO PARA BINARIO É IGUAL A {}'.format(num, bin(num)[2:]))
elif opc == 2:
    print('{} CONVERTIDO EM OCTAL É IGUAL E {}'.format(num, oct(num)[2:]))
elif opc == 3:
    print('{} CONVERTIDO EM HEXADECIMAL É IGUAL A {}'.format(num, hex(num)[2:]))
else:
    print('OPÇÃO INVALIDA!!')