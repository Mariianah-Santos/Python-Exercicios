# Pagina 1
def dobro(p):
    return p * 2


def metade(p):
    return p / 2


def aumento(p):
    return p + (p * 10/100)


def diminuir(p):
    return p - (p * 13 / 100)

# Pagina 2
import tarefa
preco = float(input('DIGITE O PREÇO R$ '))
print(f'A METADE DO {preco} É IGUAL A {tarefa.dobro(preco)}')
print(f'O DOBRO DE {preco} É IGUAL A {tarefa.metade(preco)}')
print(f'O AUMENTO (10%) NO {preco} É IGUL A {tarefa.aumento(preco)}')
print(f'A DIMINUIÇÃO (13%) DE {preco} É IGUAL A {tarefa.diminuir(preco)}')