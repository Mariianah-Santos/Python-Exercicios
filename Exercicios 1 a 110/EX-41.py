# crie um codigo para saber qual sua categoria no mundo de atlestimo 

from datetime import date
nascimento = int(input("informe se ano de nascimento => "))
ano_atual = date.today().year
idade = ano_atual - nascimento
if idade <= 9:
    print("CATEGORIA MIRIM")
elif idade <= 14:
    print("infatil")
elif idade <= 19:
    print("junior")
elif idade <= 25:
    print("SENIOR")
elif idade > 25:
    print("MASTER")

print(idade)
