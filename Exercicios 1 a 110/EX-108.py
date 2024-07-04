# PAGINA 1
def moeda():
    return 'R$'


def dobro(p):
    return p * 2


def metade(p):
    return p / 2


def aumento(p):
    return p + (p * 10/100)


def diminuir(p):
    return p - (p * 13 / 100)

# PAGINA 2
import tarefa
preco = float(input('DIGITE O PREÇO R$ '))
print(f'A METADE DO {tarefa.moeda()}{preco} É IGUAL A {tarefa.moeda()}{tarefa.dobro(preco)}')
print(f'O DOBRO DE {tarefa.moeda()}{preco} É IGUAL {tarefa.moeda()}{tarefa.metade(preco)}')
print(f'O AUMENTO (10%) NO {tarefa.moeda()}{preco} É IGUL A {tarefa.moeda()}{tarefa.aumento(preco)}')
print(f'A DIMINUIÇÃO (13%) DE {tarefa.moeda()}{preco} É IGUAL A {tarefa.moeda()}{tarefa.diminuir(preco)}')
