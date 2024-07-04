from datetime import date
def voto():
    nasc = int(input('DIGITE SEU ANO DE NASCIMENTO: '))
    ano = date.today().year
    idade = ano - nasc
    print(f'COM A IDADE {idade}:', end='')
    if idade <= 17:
        print('\033[31m NÃO PRECISA VOTA\033[m')
    elif idade <= 64:
        print('\033[31m VOTO OBRIGATÓRIO!\033[m')
    elif idade >= 65:
        print('\033[31m VOTO OPCIONAL\033[M')


voto()

# ou

from datetime import date


def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'COM A IDADE {idade}: \033[31m NÃO PRECISA VOTA\033[m'
    elif 16 <= idade < 18 or idade > 65:
        return f'COM A IDADE {idade}:\033[31m VOTO OPCIONAL\033[m'
    else:
        return f'COM A IDADE {idade}:\033[31m VOTO OBRIGATÓRIO!\033[m'


nasc = int(input('DIGITE SEU ANO DE NASCIMENTO: '))
print(voto(nasc))
