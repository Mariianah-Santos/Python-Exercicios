# PAGINA 1
def moeda(p='R$'):
    return p


def dobro(p):
    return p * 2


def metade(p):
    return p / 2


def aumento(p):
    return p + (p * 10/100)


def diminuir(p):
    return p - (p * 13 / 100)

def resumo(p=0, taxa=10, taxar=5):
    print('='*30)
    print('RESUMO DO VALOR'.center(30))
    print('=' * 30)
    print(f'PREÇO ANALISADO: {moeda():>7}{p}')
    print(f'DOBRO DO PREÇO: {moeda():>8}{dobro(p)}')
    print(f'METADE DO PREÇO É: {moeda():>5}{metade(p)}')
    print(f'COM TAXAS {taxa}% DE AUMENTO:{moeda()}{aumento(p)}')
    print(f'COM TAXAS {taxar}% DE REDUZAO:{moeda()}{diminuir(p)}')
    print('=' * 30)

# ou

def moeda(p='R$'):
    return p


def dobro(p):
    return p * 2


def metade(p):
    return p / 2


def aumento(p):
    return p + (p * 10/100)


def diminuir(p):
    return p - (p * 13 / 100)

def resumo(p=0, taxa=10, taxar=5):
    print('='*30)
    print('RESUMO DO VALOR'.center(30))
    print('=' * 30)
    print(f'PREÇO ANALISADO: \t{moeda():>7}{p}')
    print(f'DOBRO DO PREÇO: \t{moeda():>8}{dobro(p)}')
    print(f'METADE DO PREÇO É: \t{moeda():>5}{metade(p)}')
    print(f'COM TAXAS {taxa}% DE AUMENTO:\t{moeda()}{aumento(p)}')
    print(f'COM TAXAS {taxar}% DE REDUZAO:\t{moeda()}{diminuir(p)}')
    print('=' * 30)
# PAGINA 2
from tarefa import resumo
p = float(input('DIGITE O PREÇO: R$'))
resumo(p)
