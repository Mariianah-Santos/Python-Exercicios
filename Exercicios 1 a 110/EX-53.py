# crie um codigo para saber se é polindromo (se de tras pra frente a frase continua a mesma. EX (ANA de tras pra frente ainda é ana))
frase = str(input('DIGITE UMA FRASE => ')).strip().upper()
words = frase.split()
junto =''.join(words)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('{} e {}'.format(junto, inverso))
if inverso == junto:
    print('TEMOS UM POLINDROMO')
else:
    print('NÃO TEMOS UM PALINDROMO')