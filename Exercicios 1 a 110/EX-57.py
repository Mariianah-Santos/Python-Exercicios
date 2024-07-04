# crie um codigo para registrar os generos de sexos dos usuarios. Mostra erro se nao for escolhido as letras M/F e repetir a pergunta automaticamente


sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('DIGITE SEU SEXO [M/F] ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('\033[31mCONOTAÇÃO ERRADA \033[33m \nDIGITE A LETRA M OU F! \033[m')
print('SEXO {} REGISTRADO COM SUCESSO'.format(sexo))