# CRIE UM CODGI QUE MSTRE AS POSICÕES DA AE QUANTAS FORAM DIGITADAS

frase = str(input('DIGITE UM FRASE =>')).upper().strip()
print(frase.count('A'))
print('A LETRA A APARECEU NA PRIMERA POSIÇÃO {} '.format(frase.find('A')+1))
print('A ULTIMA POSIÇÃO APARECEU {}'.format(frase.rfind('A')+1))