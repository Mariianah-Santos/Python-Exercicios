# crie um codigo que diga ser é bissexto ou nao

ano = int(input('EM QUE ANO ESTAMOS? '))
if ano % 4 == 0:
    print('O ANO {} É BISSEXTO'.format(ano))
else:
    print('O ANO {} NÃO É BISSEXTO'.format(ano))

# ou

ano = int(input('EM QUE ANO ESTAMOS? '))
if ano % 4 == 0 or ano % 400 == 0:
    print('O ANO {} É BISSEXTO'.format(ano))
else:
    print('O ANO {} NÃO É BISSEXTO'.format(ano))

# ou

ano = int(input('EM QUE ANO ESTAMOS? '))
if ano % 4 == 0 or ano % 400 == 0 and % 100 != 0:
    print('O ANO {} É BISSEXTO'.format(ano))
else:
    print('O ANO {} NÃO É BISSEXTO'.format(ano))
# ou

from datetime import date
ano = int(input('EM QUE ANO ESTAMOS? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or % 400 == 0:
    print('O ANO {} É BISSEXTO'.format(ano))
else:
    print('O ANO {} NÃO É BISSEXTO'.format(ano))