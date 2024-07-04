# crie um codigo de alistamento militar.
# maior ou igula 18 ja pode se alistar. Menor que 18 não pode se alistar
from datetime import date

nascimento = int(input("Qaul ano você nasceu? "))
ano_atual = date.today().year
idade = ano_atual - nascimento
print("Sua idade é {}".format(idade))
if idade == 18:
    print(" JÁ PODE SE ALISTAR")
elif idade < 18:
    print("Voce ainda nao tem idadae para se alistar")
elif idade > 18:
    nova_idade = idade - 18
    print("VOCE JA PASSOU DA IDADE DE ALISTAMENTO. TERÁ QUE PAGAR UMA TAXA")
    print("Seu alistamento foi {} anos atrás".format(nova_idade))

