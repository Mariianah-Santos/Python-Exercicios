# crie um codigo para saber se algo está dentro do texto
c = input('DIGITE UMA CIDADE => ')
print('SANTOS' in c)

c = str(input('DIGITE UMA CIDADE => ')).strip()
print(c[:5].upper() == 'SANTOS')