# crie um codigo de emprestimo de banco
print('-=-'*20)
print('        BEM-VINDO AO BANCO MARIMAXIMO         ')
print(' PARA EMPRESTIMOS ATE 12X | 24X | 36X | 48X   ')
print('-=-'*20)
print()
nome = str(input('DIGITE SEU NOME, POR FAVOR => '))
valorC = float(input('DIGITE O VALOR DA CASA => R$ '))
Sal = float(input('ESCREVA SEU SALÁRIO R$ '))
anos = int(input('PRETENDE FINANCIAR POR QUANTOS ANOS? '))
prestação = valorC / (anos * 12)
minimo = (Sal*30)/100
print('A PESTAÇÃO FICARÁ POR R$ {:.2f}'.format(prestação))
if prestação <= minimo:
    print('EMPRESTIMO PODE SER CONCEDIDO')
else:
    print('EMPRESTIMO NEGADO')